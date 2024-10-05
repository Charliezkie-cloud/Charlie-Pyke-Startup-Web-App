import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_AI_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

def charlieGPT():
    if 'history' not in st.session_state:
        st.session_state['history'] = []

    prompt = st.chat_input("Say something")

    if prompt:
        chat_session = model.start_chat(
            history = st.session_state["history"]
        )
        response = chat_session.send_message(prompt)

        st.session_state["history"].append({
            "role": "user",
            "parts": [
                f"{prompt}"
            ]
        })

        st.session_state["history"].append({
            "role": "model",
            "parts": [
                f"{response.text}"
            ]
        })

        for chat in chat_session.history:
            if chat.role == "user":
                st.write(f"**Me**: {chat.parts[0].text}")
            elif chat.role == "model":
                st.write(f"**Charlie**: {chat.parts[0].text}")