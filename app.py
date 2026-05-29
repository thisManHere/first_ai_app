import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="first_ai_app",
    layout="centered",
)

st.markdown("""
<style>
  .hero {
    background: purple;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
  }

  .bubble-user {
    background: blue;
    color: white;
    border-radius: 12px;
    padding: 0.75rem;
    margin-left: auto;
    width: fit-content;
  }

  .bubble-assistant {
    background: lightgrey;
    color: black;
    border-radius: 12px;
    padding: 0.75rem;
    width: fit-content;
  }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### pip install streamlit google-generativeai⚙️ Settings")

    api_key = st.text_input(
        "Google API Key",
        type="password",
        placeholder="Paste your Google API key here",
        help="Get your key at aistudio.google.com",
    )

    temperature = st.slider("Temperature", 0.0, 1.0, 0.7,
        help="Higher = more creative")

    st.divider()

    if st.button("🗑️ Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

st.markdown("""
<div class="hero">
  <h1>🤖 My AI App</h1>
  <p>Powered by Google Gemini · Ask me anything</p>
</div>
""", unsafe_allow_html=True)


# Session state
 
if "messages" not in st.session_state:
    st.session_state.messages = []


# Render chat

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown('<div class="label label-user">You</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bubble-user">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="label">Gemini</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bubble-assistant">{msg["content"]}</div>', unsafe_allow_html=True)
 
if not st.session_state.messages:
    st.markdown("<p style='text-align:center;color:#94a3b8;margin-top:2rem'>👋 Type a message below to start!</p>", unsafe_allow_html=True)


# Input and Send

col1, col2 = st.columns([6, 1])
with col1:
    user_input = st.text_input("message", placeholder="Ask anything…", label_visibility="collapsed")
with col2:
    send = st.button("Send ➤", type="primary", use_container_width=True)

# Handle send

if send and user_input.strip():
    if not api_key:
        st.error("⚠️ Please enter your Google API Key in the sidebar.")
        st.stop()
 
    st.session_state.messages.append({"role": "user", "content": user_input.strip()})

    with st.spinner("Gemini is thinking…"):
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            history = [
                {"role": m["role"], "parts": [m["content"]]}
                for m in st.session_state.messages[:-1]
            ]
            chat = model.start_chat(history=history)
            response = chat.send_message(
                user_input.strip(),
                generation_config={"temperature": temperature}
            )
            reply = response.text
        except Exception as e:
            st.error(f"❌ Error: {e}")
            st.session_state.messages.pop()
            st.stop()
 
    st.session_state.messages.append({"role": "model", "content": reply})
    st.rerun()