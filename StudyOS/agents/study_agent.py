

# from services.ai_service import generate_study_content
# from skills.summarize_skill import summarize_text
# from utils.memory_manager import load_memory, save_memory

# class StudyAgent:

#     def generate_plan(self, pdf_text, days):

#         try:

#             return generate_study_content(
#                 pdf_text,
#                 f"""
#                 Create a detailed {days}-day study plan.

#                 Requirements:
#                 - Daily topics
#                 - Revision day
#                 - Practice MCQs
#                 - Exam preparation tips
#                 """
#             )

#         except Exception:

#             topics = summarize_text(pdf_text)

#             plan = ""

#             for day in range(days):

#                 topic = topics[day % len(topics)]

#                 plan += f"""
# Day {day+1}

# Topic:
# {topic}

# Duration:
# 2 Hours

# Tasks:
# • Read Notes
# • Make Short Notes
# • Practice Questions

# ----------------------------------

# """

#             plan += """
# Final Revision Day

# • Revise All Topics
# • Solve Quiz
# • Review Weak Areas
# """

#             return plan




# from services.ai_service import generate_study_content
# from skills.summarize_skill import summarize_text
# from utils.memory_manager import load_memory, save_memory


# class StudyAgent:

#     def generate_plan(self, pdf_text, days):

#         try:

#             plan = generate_study_content(
#                 pdf_text,
#                 f"""
# Create a detailed {days}-day study plan.

# Requirements:
# - Daily topics
# - Revision day
# - Practice MCQs
# - Exam preparation tips
# """
#             )

#         except Exception:

#             topics = summarize_text(pdf_text)

#             plan = ""

#             for day in range(days):

#                 topic = topics[day % len(topics)]

#                 plan += f"""
# Day {day+1}

# Topic:
# {topic}

# Duration:
# 2 Hours

# Tasks:
# • Read Notes
# • Make Short Notes
# • Practice Questions

# ----------------------------------
# """

#             plan += """
# Final Revision Day

# • Revise All Topics
# • Solve Quiz
# • Review Weak Areas
# """

#         memory = load_memory()
#         memory["plans"].append(plan)
#         topics = memory["topics"]
#         save_memory(memory)

#         return plan



from services.ai_service import generate_study_content
from skills.summarize_skill import summarize_text
from utils.memory_manager import load_memory, save_memory


class StudyAgent:

    def generate_plan(self, pdf_text, days):

        memory = load_memory()

        # --------------------------------
        # Read topics from Summary Agent
        # --------------------------------
        topics = memory.get("topics", [])

        # Fallback if Summary wasn't generated
        if not topics:
            topics = summarize_text(pdf_text)

        try:

            plan = generate_study_content(
                pdf_text,
                f"""
Create a detailed {days}-day study plan.

Requirements:
- Daily topics
- Revision day
- Practice MCQs
- Exam preparation tips
"""
            )

        except Exception:

            plan = ""

            for day in range(days):

                topic = topics[day % len(topics)]

                plan += f"""
Day {day+1}

Topic:
{topic}

Duration:
2 Hours

Tasks:
• Read Notes
• Make Short Notes
• Practice Questions

----------------------------------

"""

            plan += """
Final Revision Day

• Revise All Topics
• Solve Quiz
• Review Weak Areas
"""

        memory["plans"].append(plan)

        save_memory(memory)

        return plan