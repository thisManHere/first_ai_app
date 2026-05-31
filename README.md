# first_ai_app 🤖

A lightweight conversational AI chat interface built with Streamlit and powered by Google Gemini. Designed to be simple to run, easy to extend, and practical for real-world use.

---

## What it does

This app gives you a clean chat UI where you paste your Google Gemini API key, adjust the temperature, and start a multi-turn conversation with Gemini 1.5 Flash. It maintains full conversation history within the session so the model has context across messages.

---

## Real-life use cases

- **Daily assistant** — ask it to summarise articles, draft emails, or explain concepts while you work
- **Learning tool** — quiz yourself on any topic, get explanations, work through problems step by step
- **Rapid prototyping** — use it as a base to build domain-specific chatbots (customer support, HR FAQ, coding assistant) by adding a system prompt
- **API learning project** — a practical way to understand how LLM APIs, conversation history, and stateful web apps work together

---

## Stack

- [Streamlit](https://streamlit.io) — UI framework
- [Google Generative AI SDK](https://pypi.org/project/google-generativeai/) — Gemini API client
- Python 3.10+

---

## Getting started

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/first_ai_app.git
cd first_ai_app
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

**4. Get a Gemini API key**

Go to [aistudio.google.com](https://aistudio.google.com), generate a free API key, and paste it into the sidebar when the app opens.

---

## Project structure

```
first_ai_app/
├── app.py            # Main application
├── requirements.txt  # Dependencies
└── README.md
```

---

## Deployment

Deployed on **Streamlit Community Cloud**. Any push to `main` triggers an automatic redeploy.

To deploy your own fork:
1. Push to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo and set `app.py` as the entry point

---

## Roadmap

- [ ] Streaming responses
- [ ] System prompt editor in sidebar
- [ ] Model selector (Flash / Pro / 2.0)
- [ ] Chat history export (Markdown / PDF)
- [ ] Image upload support (Gemini is multi-modal)
- [ ] Dockerize for self-hosting

---

## License

MIT
