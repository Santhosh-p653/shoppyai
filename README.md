---

title: Shoppy AI
emoji: 🛒
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: "5.34.2"
app_file: app.py
pinned: false
-------------

# Shoppy AI 🛒

An AI-powered e-commerce assistant that combines conversational AI, Retrieval-Augmented Generation (RAG), order management, and customer support into a single interactive application.

## 🚀 Live Demo

**Application:**
https://santhosh11042007-shoppyai.hf.space

**Hugging Face Space:**
https://huggingface.co/spaces/santhosh11042007/shoppyai

---

## Project Overview

Shoppy AI explores how Large Language Models can be integrated into real-world business workflows.

Instead of acting as a standalone chatbot, the assistant interacts with structured product and order data while leveraging AI reasoning to answer customer questions and provide support.

Users can:

* Browse products
* Place simulated orders
* Track deliveries
* Ask support questions
* Retrieve company policy information
* Interact using natural language

---

## System Architecture

```text
User
 │
 ▼
Gradio Interface
 │
 ▼
Application Layer
 │
 ├── Product Management
 ├── Order Tracking
 ├── Knowledge Retrieval
 │
 ▼
SQLite Database
 │
 ▼
RAG Context Builder
 │
 ▼
Llama 3.3 70B (SambaNova)
```

---

## Technology Stack

### Frontend

* Gradio

### Backend

* Python
* SQLAlchemy

### Database

* SQLite

### AI Components

* Retrieval-Augmented Generation (RAG)
* SambaNova API
* Meta Llama 3.3 70B Instruct

### Deployment & DevOps

* GitHub Actions
* Hugging Face Spaces
* Secret Management using Environment Variables

---

## Engineering Journey

This project was built to understand how modern AI systems are engineered beyond simple prompting.

Key areas explored include:

* Conversational AI design
* LLM integration
* Retrieval-Augmented Generation
* Database-driven applications
* Prompt engineering
* API integration
* CI/CD automation
* Cloud deployment workflows
* Secure credential management

A major objective was learning how structured business operations and large language models can work together within a production-style application architecture.

---

## Example Commands

### Purchase a Product

```text
buy headphones
```

### Track an Order

```text
track 102345
```

### Ask a Support Question

```text
What is your return policy?
```

---

## Key Learnings

* Building AI applications requires more than model calls.
* Structured data and LLMs complement each other.
* RAG improves reliability by grounding responses in business knowledge.
* Deployment pipelines are essential for maintaining production applications.
* Secret management should always be handled through environment variables rather than hardcoded credentials.

---

## Future Improvements

* Vector database integration
* Semantic search
* Product recommendation engine
* Multi-agent customer support
* Analytics dashboard
* Inventory forecasting
* Hybrid retrieval architecture

---

## Author

Built as part of a hands-on AI engineering journey focused on:

* Large Language Models
* Retrieval-Augmented Generation
* AI Application Development
* MLOps & Deployment
* Production AI Systems
* Full-Stack AI Engineering
