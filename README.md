# 🤖 LLM Powered Chatbot using LangChain + Hugging Face

An interactive conversational AI chatbot built using **LangChain**, **Hugging Face LLMs**, and **Streamlit**.  
This project demonstrates the integration of open-source Large Language Models (LLMs) with a modern chat interface supporting multi-turn conversations and session-based memory handling.

---

# 🚀 Features

- 💬 Interactive chatbot interface using Streamlit
- 🧠 Multi-turn conversation support
- 🔗 LangChain integration
- 🤗 Hugging Face LLM inference endpoint support
- ⚡ Real-time response generation
- 🧩 Modular code architecture
- 🔒 Environment variable support using `.env`
- 🛠 Beginner-friendly and extensible foundation for RAG and AI agents

---

# 🧰 Tech Stack

- Python
- LangChain
- Hugging Face
- Streamlit
- Transformers
- PyTorch
- dotenv

---

# 📂 Project Structure

```bash
├── app.py              # Streamlit frontend and chat interface
├── chatbot.py          # LLM loading and model orchestration
├── requirements.txt    # Project dependencies
├── .env                # API tokens (not uploaded to GitHub)
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/llm-chatbot.git
cd llm-chatbot
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root directory.

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

You can generate a Hugging Face token from:

https://huggingface.co/settings/tokens

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 🖥 Application Preview

The chatbot provides:

- User-friendly conversational interface
- Real-time AI responses
- Session-based message history
- Open-source LLM interaction

---

# 🧠 Model Used

Current configuration uses:

- Meta Llama 3.1 8B Instruct
- Mistral 7B Instruct

via Hugging Face Inference API.

---

This project is developed for educational and learning purposes to explore:
- LLM applications
- LangChain orchestration
- Conversational AI systems
- Open-source model integration

---

# 👨‍💻 Author

## Dewang Moghe

- LinkedIn: https://www.linkedin.com/in/dewang-moghe
- GitHub: https://github.com/Devm2512

---

# ⭐ If you found this project useful, consider giving it a star!
