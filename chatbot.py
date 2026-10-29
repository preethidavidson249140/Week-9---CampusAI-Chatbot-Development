
import csv
import logging
from datetime import datetime
from pathlib import Path
import ollama

# Project configuration
MODEL = "gemma3:1b"
DATASET_DIR = Path(__file__).parent / "dataset"
DATASET_DIR.mkdir(exist_ok=True)

HISTORY_FILE = DATASET_DIR / "chat_history.csv"
LOG_FILE = DATASET_DIR / "chatbot_logs.txt"

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Create CSV file with headers
if not HISTORY_FILE.exists() or HISTORY_FILE.stat().st_size == 0:
    with open(HISTORY_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "User Question", "Chatbot Response"])

# Conversation history for context awareness
conversation_history = [
    {
        "role": "system",
        "content": (
            "You are CampusAI, a helpful educational assistant. "
            "Answer student questions clearly and accurately. "
            "Explain concepts with simple examples. "
            "If you are unsure, say so rather than inventing facts."
        )
    }
]

def save_conversation(question, response):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(HISTORY_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, question, response])

    logging.info("Question: %s | Response: %s", question, response)


def generate_response(question):
    conversation_history.append({
        "role": "user",
        "content": question
    })

    try:
        result = ollama.chat(
            model=MODEL,
            messages=conversation_history,
            options={
                "num_predict": 150,
                "num_ctx": 2048
            }
        )

        answer = result["message"]["content"]

        conversation_history.append({
            "role": "assistant",
            "content": answer
        })

        save_conversation(question, answer)
        return answer

    except Exception as error:
        conversation_history.pop()
        logging.error("Chatbot error: %s", error)
        return f"Error: {error}"


def main():
    print("=" * 50)
    print("CAMPUSAI - EDUCATIONAL CHATBOT")
    print("Powered by Ollama and Gemma 3 (1B)")
    print("Type 'exit' to stop chatting.")
    print("=" * 50)

    while True:
        try:
            question = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nCampusAI: Goodbye!")
            break

        if question.lower() == "exit":
            print("CampusAI: Goodbye!")
            break

        if not question:
            print("CampusAI: Please enter a question.")
            continue

        answer = generate_response(question)
        print(f"\nCampusAI: {answer}")


if __name__ == "__main__":
    main()
