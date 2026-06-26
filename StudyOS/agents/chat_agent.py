from services.ai_service import generate_study_content


class ChatAgent:

    def ask_question(self, pdf_text, question):

        try:

            prompt = f"""
You are an AI tutor.

Answer ONLY using the uploaded study notes.

If the answer is not present, reply:

"I couldn't find this information in the uploaded PDF."

Question:

{question}
"""

            answer = generate_study_content(
                pdf_text,
                prompt
            )

            return answer

        except Exception:

            # ---------- Offline Mode ----------

            paragraphs = pdf_text.split("\n\n")

            question_words = question.lower().split()

            best_paragraph = ""

            highest_score = 0

            for paragraph in paragraphs:

                score = 0

                lower = paragraph.lower()

                for word in question_words:

                    if word in lower:

                        score += 1

                if score > highest_score:

                    highest_score = score

                    best_paragraph = paragraph

            if best_paragraph:

                return (
                    "⚠️ AI unavailable.\n\n"
                    "Offline Answer:\n\n"
                    + best_paragraph
                )

            return (
                "⚠️ AI unavailable.\n\n"
                "No relevant information found."
            )