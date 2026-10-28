
import streamlit as st
import ollama

st.set_page_config(
    page_title="CampusAI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 CampusAI - Student Assistant")
st.write("Your AI-powered learning companion")

MODEL = "gemma3:1b"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask me anything...")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = ollama.chat(
                    model=MODEL,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are CampusAI, a helpful "
                                "student learning assistant. "
                                "Explain concepts clearly."
                            )
                        },
                        *st.session_state.messages
                    ]
                )

                answer = response["message"]["content"]
                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:
                st.error(f"Error: {e}")

if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
