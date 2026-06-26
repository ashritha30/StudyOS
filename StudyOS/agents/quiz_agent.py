



# from services.ai_service import generate_study_content
# from skills.summarize_skill import summarize_text
# from utils.memory_manager import load_memory, save_memory


# class QuizAgent:

#     def generate_quiz(self, pdf_text):

#         try:

#             quiz = generate_study_content(
#                 pdf_text,
#                 """
# Generate 10 multiple-choice questions.

# Include:
# - 4 options
# - Correct answer
# - Short explanation
# """
#             )

#         except Exception:

#             topics = summarize_text(pdf_text)

#             quiz = ""

#             for i, topic in enumerate(topics[:5]):

#                 quiz += f"""
# Q{i+1}. What is {topic}?

# A) Definition
# B) Example
# C) Application
# D) All of the Above

# Answer: D

# Explanation:
# This topic is important for exams.

# -----------------------------------
# """

#         memory = load_memory()
#         memory["quizzes"].append(quiz)
#         topics = memory["topics"]
#         save_memory(memory)

#         return quiz



from services.ai_service import generate_study_content
from skills.summarize_skill import summarize_text
from utils.memory_manager import load_memory, save_memory


class QuizAgent:

    def generate_quiz(self, pdf_text):

        memory = load_memory()

        # ----------------------------
        # Get topics from Summary Agent
        # ----------------------------
        topics = memory.get("topics", [])

        # Fallback if topics are not available
        if not topics:
            topics = summarize_text(pdf_text)

        try:

            quiz = generate_study_content(
                pdf_text,
                """
Generate 10 multiple-choice questions.

Include:
- 4 options
- Correct answer
- Short explanation
"""
            )

        except Exception:

            quiz = ""

            for i, topic in enumerate(topics[:5]):

                quiz += f"""
Q{i+1}. What is {topic}?

A) Definition
B) Example
C) Application
D) All of the Above

Answer: D

Explanation:
This topic is important for exams.

-----------------------------------
"""

        # Save Quiz
        memory["quizzes"].append(quiz)
        save_memory(memory)

        return quiz