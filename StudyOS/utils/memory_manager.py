import json
import os

MEMORY_FILE = "data/memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        # return {
        #     "summaries": [],
        #     "quizzes": [],
        #     "plans": []
        # }
        return {
    "summaries": [],
    "quizzes": [],
    "plans": [],
    "topics": [],
    "quiz_scores": [],
    "weak_topics": []
}

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)