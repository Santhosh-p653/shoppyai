
import os
import random
import gradio as gr
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from openai import OpenAI

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Float)
    category = Column(String)
    description = Column(String)
    image_url = Column(String)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    product_name = Column(String)
    status = Column(String)
    delivery_date = Column(String)

engine = create_engine("sqlite:///shoppy_ai.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if session.query(Product).count() == 0:
    products = [
        Product(
            name="Cosmic Sound Wireless Headphones",
            price=2999,
            category="Electronics",
            description="Active noise cancelling headphones.",
            image_url="🎧"
        ),
        Product(
            name="FitTrack Smart Fitness Band",
            price=1999,
            category="Electronics",
            description="Heart rate and sleep tracking.",
            image_url="⌚"
        ),
        Product(
            name="AeroStride Running Shoes",
            price=3499,
            category="Footwear",
            description="Lightweight running shoes.",
            image_url="👟"
        ),
        Product(
            name="HydroFlask Sleek Water Bottle",
            price=899,
            category="Lifestyle",
            description="Vacuum insulated bottle.",
            image_url="🍼"
        )
    ]
    session.add_all(products)
    session.commit()

if session.query(Order).count() == 0:
    orders = [
        Order(
            id=102345,
            customer_name="Santhosh",
            product_name="Cosmic Sound Wireless Headphones",
            status="Out for Delivery",
            delivery_date="Today 5 PM"
        ),
        Order(
            id=102346,
            customer_name="Santhosh",
            product_name="HydroFlask Sleek Water Bottle",
            status="Delivered",
            delivery_date="Yesterday"
        )
    ]
    session.add_all(orders)
    session.commit()

KNOWLEDGE_BASE = [
    "Items can be returned within 10 days of delivery.",
    "Refunds are processed within 5 to 7 business days.",
    "Defective electronics can be replaced within 48 hours.",
    "Customer data is encrypted and never sold.",
]

def retrieve_context(query):
    matches = []
    for item in KNOWLEDGE_BASE:
        if any(word.lower() in item.lower() for word in query.split()):
            matches.append(item)
    return "\n".join(matches[:4])

client = OpenAI(
    base_url="https://api.sambanova.ai/v1",
    api_key=os.environ["SAMBANOVA_API_KEY"]
)

def fetch_products_html():
    products = session.query(Product).all()
    html = """
    <div style="
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
        gap: 16px;
        padding: 8px 0;
    ">
    """
    for p in products:
        html += f"""
        <div style="
            background: #ffffff;
            border-radius: 10px;
            padding: 16px 12px;
            border: 1px solid #c8d0db;
            box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        ">
            <div style="font-size: 42px; text-align: center; margin-bottom: 10px;">
                {p.image_url}
            </div>
            <div style="
                font-size: 14px;
                font-weight: 700;
                color: #0d1b2a;
                margin-bottom: 6px;
                line-height: 1.3;
            ">{p.name}</div>
            <div style="
                color: #1a7f37;
                font-weight: 800;
                font-size: 16px;
                margin-bottom: 6px;
            ">₹{p.price}</div>
            <div style="
                font-size: 12px;
                color: #444f5a;
                line-height: 1.4;
            ">{p.description}</div>
            <div style="
                margin-top: 8px;
                display: inline-block;
                background: #eaf3ff;
                color: #2874f0;
                font-size: 11px;
                font-weight: 600;
                padding: 2px 8px;
                border-radius: 20px;
            ">{p.category}</div>
        </div>
        """
    html += "</div>"
    return html

def query_shoppy_brain(message, history):
    text = message.lower().strip()

    # BUY PRODUCT
    if text.startswith("buy "):
        product_name = message[4:]
        product = (
            session.query(Product)
            .filter(Product.name.ilike(f"%{product_name}%"))
            .first()
        )
        if not product:
            return "❌ Product not found."

        order_id = random.randint(200000, 999999)
        order = Order(
            id=order_id,
            customer_name="Santhosh",
            product_name=product.name,
            status="Processing",
            delivery_date="Within 3 Days"
        )
        session.add(order)
        session.commit()

        return f"""✅ Order Placed Successfully
Order ID: {order_id}
Product: {product.name}
Status: Processing
Expected Delivery: Within 3 Days"""

    # TRACK ORDER
    if text.startswith("track "):
        try:
            order_id = int(text.split()[-1])
            order = (
                session.query(Order)
                .filter(Order.id == order_id)
                .first()
            )
            if not order:
                return "❌ Order not found."

            return f"""📦 Order Tracking
Order ID: {order.id}
Product: {order.product_name}
Status: {order.status}
Delivery: {order.delivery_date}"""
        except:
            return "Invalid order id."

    # LLM FALLBACK
    context = retrieve_context(message)
    system_prompt = f"""You are Shoppy AI.
Policies: {context}
Answer using available information. If unknown, say support assistance is required."""

    messages = [{"role": "system", "content": system_prompt}]

    for h in history:
        if h["role"] in ["user", "assistant"]:
            messages.append(h)

    messages.append({"role": "user", "content": message})

    try:
        response = client.chat.completions.create(
            model="Meta-Llama-3.3-70B-Instruct",
            messages=messages,
            temperature=0.1,
            max_tokens=400
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

# ========================= UI =========================

CSS = """
/* Page background */
.gradio-container {
    background: #eef1f7 !important;
    font-family: 'Segoe UI', Arial, sans-serif !important;
}

/* Banner */
.flipkart-banner {
    background: linear-gradient(90deg, #2874f0 0%, #1a56c4 100%) !important;
    padding: 14px 20px !important;
    border-radius: 10px !important;
    margin-bottom: 8px !important;
    box-shadow: 0 3px 10px rgba(40,116,240,0.3) !important;
}

/* Make all text in left column visible */
.gr-markdown p, .gr-markdown li, .gr-markdown code {
    color: #0d1b2a !important;
    font-size: 14px !important;
}

/* Chatbot messages */
.message.user .bubble-wrap, .message.bot .bubble-wrap {
    font-size: 14px !important;
    color: #0d1b2a !important;
}

/* Textbox label */
label span {
    color: #0d1b2a !important;
    font-weight: 600 !important;
    font-size: 14px !important;
}

/* Textbox input text */
textarea, input[type="text"] {
    color: #0d1b2a !important;
    background: #ffffff !important;
    font-size: 14px !important;
    border: 1.5px solid #b0bbcc !important;
}

/* Clear button */
button.secondary {
    background: #ffffff !important;
    color: #2874f0 !important;
    border: 1.5px solid #2874f0 !important;
    font-weight: 600 !important;
}

button.secondary:hover {
    background: #2874f0 !important;
    color: #ffffff !important;
}

/* Section headers */
.gr-markdown h2 {
    color: #0d1b2a !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    margin-bottom: 12px !important;
}

/* Tip box background */
.gr-markdown {
    background: transparent !important;
}
"""

with gr.Blocks(theme=gr.themes.Soft(), css=CSS) as demo:

    with gr.Row(elem_classes=["flipkart-banner"]):
        gr.HTML("""
        <div style="
            color: #ffffff;
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        ">
            <div>
                <span style="font-size:22px; font-weight:800; letter-spacing:0.5px;">
                    Shoppy Plus ✦
                </span>
                <span style="
                    font-size:11px;
                    background:#ffffff30;
                    padding:2px 8px;
                    border-radius:20px;
                    margin-left:10px;
                    font-weight:500;
                ">RAG · AI Powered</span>
            </div>
            <span style="font-size:15px; font-weight:500; opacity:0.92;">
                AI Concierge Workspace
            </span>
        </div>
        """)

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("## 🌟 Trending Products")
            gr.HTML(value=fetch_products_html())
            gr.HTML("""
            <div style="
                background: #ffffff;
                border: 1px solid #c8d0db;
                border-radius: 10px;
                padding: 14px 16px;
                margin-top: 12px;
                box-shadow: 0 1px 4px rgba(0,0,0,0.06);
            ">
                <div style="
                    font-weight: 700;
                    font-size: 13px;
                    color: #2874f0;
                    margin-bottom: 8px;
                    text-transform: uppercase;
                    letter-spacing: 0.5px;
                ">💬 Try these commands</div>
                <div style="font-size: 13px; color: #0d1b2a; line-height: 2;">
                    <code style="background:#eaf3ff;color:#1a56c4;padding:2px 7px;border-radius:4px;font-size:12px;">buy headphones</code><br>
                    <code style="background:#eaf3ff;color:#1a56c4;padding:2px 7px;border-radius:4px;font-size:12px;">buy shoes</code><br>
                    <code style="background:#eaf3ff;color:#1a56c4;padding:2px 7px;border-radius:4px;font-size:12px;">track 102345</code><br>
                    <code style="background:#eaf3ff;color:#1a56c4;padding:2px 7px;border-radius:4px;font-size:12px;">track 102346</code><br>
                    <code style="background:#eaf3ff;color:#1a56c4;padding:2px 7px;border-radius:4px;font-size:12px;">What is your return policy?</code>
                </div>
            </div>
            """)

        with gr.Column(scale=1):
            chatbot = gr.Chatbot(
                type="messages",
                height=500,
                show_label=False,
                avatar_images=(None, "🛒"),
                bubble_full_width=False,
            )
            msg = gr.Textbox(
                label="Ask Shoppy AI",
                placeholder="Type a command or question...",
                lines=1,
            )
            clear = gr.Button("🗑️ Clear Chat", variant="secondary")

            def respond(user_message, chat_history):
                if chat_history is None:
                    chat_history = []
                reply = query_shoppy_brain(user_message, chat_history)
                chat_history.append({"role": "user", "content": user_message})
                chat_history.append({"role": "assistant", "content": reply})
                return "", chat_history

            msg.submit(respond, [msg, chatbot], [msg, chatbot])
            clear.click(lambda: [], outputs=chatbot)

demo.launch()
