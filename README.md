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

### Application

https://santhosh11042007-shoppyai.hf.space

### Hugging Face Space

https://huggingface.co/spaces/santhosh11042007/shoppyai

---

## Overview

Shoppy AI explores how Large Language Models can be integrated with traditional software systems.

Instead of functioning as a standalone chatbot, the assistant interacts with structured business data stored in a database while leveraging AI reasoning to answer customer questions and support common e-commerce workflows.

Users can:

* Browse products
* Place orders
* Track deliveries
* Ask support questions
* Retrieve policy information
* Interact using natural language

---

## Architecture

```text
User
 │
 ▼
Gradio Interface
 │
 ▼
Application Layer
 │
 ├── Product Catalog
 ├── Order Management
 ├── Order Tracking
 ├── Policy Retrieval
 │
 ▼
SQLite Database
 │
 ▼
Context Retrieval Layer
 │
 ▼
SambaNova API
 │
 ▼
Meta Llama 3.3 70B Instruct
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

### DevOps

* GitHub
* GitHub Actions
* Hugging Face Spaces
* Environment Variables & Secrets

---

## Features

### Product Discovery

Browse available products through a simple interactive interface.

### Order Placement

Example:

```text
buy headphones
```

### Order Tracking

Example:

```text
track 102345
```

### Customer Support

Example:

```text
What is your return policy?
```

The assistant retrieves relevant policy information before generating a response.

---

## Engineering Journey

This project was built to understand how production AI applications combine traditional software engineering with modern language models.

Key concepts explored:

* Conversational AI design
* LLM integration
* Retrieval-Augmented Generation
* Database-backed AI applications
* Prompt engineering
* API integration
* CI/CD automation
* Deployment workflows
* Secure secret management

The focus was not only on generating responses but on building an application where AI interacts with structured business operations such as ordering, tracking, and customer support.

---

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── README.md
├── shoppy_ai.db
└── .github
    └── workflows
        └── deploy.yml
```

---

## Future Improvements

* Vector database integration
* Semantic retrieval
* Product recommendation engine
* Multi-agent customer support
* Analytics dashboard
* Inventory forecasting
* Hybrid search architecture

---

## Deployment

This project is automatically deployed using GitHub Actions.

Workflow:

```text
GitHub
   │
   ▼
GitHub Actions
   │
   ▼
Hugging Face Spaces
   │
   ▼
Live Application
```

Every push to the main branch automatically updates the deployed application.

---

## Author

Built as part of a practical AI engineering journey focused on:

* Large Language Models
* Retrieval-Augmented Generation
* AI Application Development
* MLOps
* Production AI Systems
* Full-Stack AI Engineering
