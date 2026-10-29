
import csv
import time
from datetime import datetime
from pathlib import Path
import ollama

BASE_DIR = Path(__file__).parent
DATASET_DIR = BASE_DIR / "dataset"

QUESTIONS_FILE = DATASET_DIR / "sample_questions.csv"
RESPONSES_FILE = DATASET_DIR / "responses.csv"

MODEL = "gemma3:1b"

def test_chatbot():
    with open(QUESTIONS_FILE, "r", encoding="utf-8-sig", newline="") as file:
        questions = list(csv.DictReader(file))

    if not questions:
        print("No sample questions found.")
        return

    print("Starting CampusAI chatbot testing...")
    print(f"Total questions: {len(questions)}")

    with open(RESPONSES_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Timestamp",
            "Question_ID",
            "Category",
            "Question",
            "Response",
            "Response_Time_Seconds",
            "Status"
        ])

        for index, row in enumerate(questions, start=1):
            question = row["Question"]
            category = row["Category"]

            print(f"\nTesting {index}/{len(questions)}")
            print(f"Question: {question}")

            start_time = time.perf_counter()

            try:
                result = ollama.chat(
                    model=MODEL,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are CampusAI, a helpful educational "
                                "assistant. Give accurate and clear answers "
                                "with simple examples."
                            )
                        },
                        {
                            "role": "user",
                            "content": question
                        }
                    ],
                    options={
                        "num_predict": 150,
                        "num_ctx": 2048
                    }
                )

                response = result["message"]["content"]
                status = "Success"

            except Exception as error:
                response = str(error)
                status = "Error"

            elapsed = round(time.perf_counter() - start_time, 2)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            writer.writerow([
                timestamp,
                row["Question_ID"],
                category,
                question,
                response,
                elapsed,
                status
            ])

            file.flush()

            print(f"Status: {status}")
            print(f"Response time: {elapsed} seconds")
            print(f"Response: {response[:200]}")

    print("\nTesting completed!")
    print(f"Results saved to: {RESPONSES_FILE}")


if __name__ == "__main__":
    test_chatbot()
