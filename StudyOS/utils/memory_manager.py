import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
MEMORY_FILE = os.path.join(DATA_DIR, "memory.json")


def load_memory():

    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(MEMORY_FILE):

        memory = {
            "summaries": [],
            "quizzes": [],
            "plans": [],
            "topics": [],
            "quiz_scores": [],
            "weak_topics": []
        }

        with open(MEMORY_FILE, "w") as f:
            json.dump(memory, f, indent=4)

        return memory

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(memory):

    os.makedirs(DATA_DIR, exist_ok=True)

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)