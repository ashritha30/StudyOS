





# from skills.summarize_skill import summarize_text

# class SummaryAgent:

#     def generate_summary(self, pdf_text):

#         topics = summarize_text(pdf_text)

#         summary = "📌 Key Topics\n\n"

#         for topic in topics[:5]:
#             summary += f"• {topic}\n"

#         summary += "\n📖 Important Concepts\n\n"

#         for topic in topics[5:10]:
#             summary += f"• {topic}\n"

#         summary += (
#             "\n🎯 Exam Focus\n\n"
#             "Study the above concepts carefully.\n"
#             "Prepare short notes and practice MCQs.\n"
#         )

#         summary += (
#             "\n📝 Quick Revision Strategy\n\n"
#             "1. Read Concepts\n"
#             "2. Make Notes\n"
#             "3. Solve MCQs\n"
#             "4. Revise Before Exam\n"
#         )

#         return summary



# from services.ai_service import generate_study_content
# from skills.summarize_skill import summarize_text
# from utils.memory_manager import load_memory, save_memory
# class SummaryAgent:

#     def generate_summary(self, pdf_text):

#         try:

#             return generate_study_content(
#                 pdf_text,
#                 "Generate a concise study summary with key concepts."
#             )

#         except Exception:
#         # except Exception as e:

#         #     print(e)

#         #     topics = summarize_text(pdf_text)

#             topics = summarize_text(pdf_text)

#             summary = "📌 Key Topics\n\n"

#             for topic in topics[:5]:
#                 summary += f"• {topic}\n"

#             summary += (
#                 "\n⚠️ AI unavailable.\n"
#                 "Offline mode activated."
#             )

#         return summary

# from services.ai_service import generate_study_content
# from skills.summarize_skill import summarize_text
# from utils.memory_manager import load_memory, save_memory


# class SummaryAgent:

#     def generate_summary(self, pdf_text):

#         try:
#             summary = generate_study_content(
#                 pdf_text,
#                 "Generate a concise study summary with key concepts."
#             )

#         except Exception:

#             topics = summarize_text(pdf_text)

#             summary = "📌 Key Topics\n\n"

#             for topic in topics[:5]:
#                 summary += f"• {topic}\n"

#             summary += (
#                 "\n⚠️ AI unavailable.\n"
#                 "Offline mode activated."
#             )

#         # Save to memory
#         # memory = load_memory()
#         # memory["summaries"].append(summary)
#         # save_memory(memory)

#         # return summary
#         memory = load_memory()

#         memory["summaries"].append(summary)

#         memory["topics"] = topics

#         save_memory(memory)
#         return summary



from services.ai_service import generate_study_content
from skills.summarize_skill import summarize_text
from utils.memory_manager import load_memory, save_memory


class SummaryAgent:

    def generate_summary(self, pdf_text):

        # Extract topics (works for both AI and offline)
        topics = summarize_text(pdf_text)

        try:

            summary = generate_study_content(
                pdf_text,
                "Generate a concise study summary with key concepts."
            )

        except Exception:

            summary = "📌 Key Topics\n\n"

            for topic in topics[:5]:
                summary += f"• {topic}\n"

            summary += "\n📖 Important Concepts\n\n"

            for topic in topics[5:8]:
                summary += f"• {topic}\n"

            summary += (
                "\n\n🎯 Exam Tip\n\n"
                "Revise the above concepts and practice MCQs before the exam."
                "\n\n⚠️ AI unavailable. Offline mode activated."
            )

        # -------- Shared Memory --------
        memory = load_memory()

        memory["summaries"].append(summary)

        memory["topics"] = topics

        save_memory(memory)

        return summary