
# 🤖 CampusAI – Student Assistant Chatbot

## LLM Week 9 – Chatbot Development

### Project Overview
CampusAI is an AI-powered educational chatbot developed
using Python, Streamlit, and Ollama.

The chatbot uses the Gemma 3 (1B) language model to answer
student questions and explain academic concepts.

## Features
- AI-powered question answering
- Interactive chatbot interface
- Conversation history within a session
- Context-aware responses
- Clear Chat functionality
- Local LLM inference
- No paid API required

## Technologies Used
- Python
- Streamlit
- Ollama
- Gemma 3 (1B)
- Visual Studio Code
- GitHub

## Project Structure

Week9_Chatbot_Development/
    app.py
    requirements.txt
    README.md

## Installation

1. Install Python and Ollama.
2. Download the AI model:

   ollama pull gemma3:1b

3. Install Python dependencies:

   python -m pip install -r requirements.txt

4. Run the chatbot:

   python -m streamlit run app.py

5. Open http://localhost:8501

## Sample Questions
- What is Artificial Intelligence?
- Explain Machine Learning.
- What is Python?
- What was my previous question?

## Learning Outcomes
- Developed an AI chatbot using Python.
- Integrated a local LLM with Ollama.
- Created an interactive Streamlit interface.
- Implemented conversation history.
- Learned how to test and deploy a chatbot locally.

## Limitations
- Requires Ollama installed on the user's computer.
- Requires the Gemma 3 (1B) model.
- Conversation history is limited to the current session.
- Responses may contain inaccuracies.

## Conclusion
CampusAI demonstrates how a locally hosted large
language model can be integrated with a Python
application to create an interactive educational chatbot.

## Assignment
LLM Week 9 – Chatbot Development
