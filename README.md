# 🤖 ASHIK: GPT

**End-to-End • Deployment-Ready • Fully Customizable Agentic AI Chat Platform**

ASHIK: GPT is a **hands-on, end-to-end AI chat application** built to help developers, AI engineers, and founders **learn, customize, and deploy real LLM-powered products** — not just demos.

This project provides a **clean UI, modular architecture, and configurable LLM setup**, making it ideal for experimentation as well as real-world AI product development.

---

## ✨ Key Features

* 🔁 **Multi-LLM support** (Groq integrated)
* 🧠 **Dynamic model selection** (e.g. LLaMA-3)
* 🔐 **Secure API key handling**
* 🧩 **Modular use-case / workstream architecture**
* 🎨 **Premium, product-grade UI**
* 🕸️ **Agentic AI–ready (LangGraph compatible)**
* 🚀 **End-to-end & deployment-ready**
* ⚙️ **Fully customizable**

---

## 🏗️ Architecture Overview

```
UI (Streamlit)
   ↓
User Controls & Config
   ↓
LLM Provider (Groq)
   ↓
Agent / Workflow Layer (LangGraph-ready)
   ↓
Response Rendering
```

This structure allows you to:

* Swap LLM providers
* Add new agent workflows
* Extend use cases without touching core UI logic

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit (custom styled UI)
* **Backend**: Python
* **LLMs**: Groq (LLaMA-3 models)
* **Agent Framework**: LangGraph (agentic AI)
* **Environment**: Virtualenv / Conda supported

---

## 🚀 Getting Started (Run Locally)

Follow these steps to run the project on your system.

---

### 1️⃣ Clone the Repository

```bash
git clone <YOUR_GITHUB_REPO_URL>
cd <project-folder>
```

---

### 2️⃣ Create & Activate Virtual Environment

#### 🔹 Using `venv` (recommended)

```bash
python -m venv venv
```

**Activate it:**

* **Windows**

```bash
venv\Scripts\activate
```

* **Mac / Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

Make sure all dependencies install successfully.

---

### 4️⃣ Set Environment Variables (Optional)

You can either:

* Enter your API key directly in the UI
  **OR**
* Set it as an environment variable

```bash
export GROQ_API_KEY=your_api_key_here   # Mac/Linux
set GROQ_API_KEY=your_api_key_here      # Windows
```

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

Once started, open your browser and go to:

```
http://localhost:8501
```

---

## 🎯 How to Use

1. Select **LLM Provider**
2. Choose the **Model**
3. Enter your **API Key**
4. Select a **Use Case / Workstream**
5. Start chatting 🚀

Everything is configurable from the UI — no code changes required for basic usage.

---

## 🧩 Customization Guide

You can easily:

* ➕ Add new LLM providers
* ➕ Add new models
* ➕ Create new use cases
* ➕ Plug in agent workflows (LangGraph)

Key configuration files:

```
src/
 └── langgraphagenticai/
     └── ui/
         └── uiconfigfile.py
```

---

## 🌍 Deployment

This project is **deployment-ready** and can be hosted on:

* Streamlit Cloud
* AWS / GCP / Azure
* Docker (recommended for production)

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

1. Fork the repo
2. Create a new branch
3. Make changes
4. Submit a pull request

---

## ⭐ Support the Project

If this helped you:

* ⭐ Star the repository
* 🧠 Build something on top of it
* 📣 Share it with others and tag me

Let’s move from **AI demos → AI products**.

---

## 📬 Contact

Built by **Ashik Kumar**
If you build something interesting using this, I’d love to see it 🚀

