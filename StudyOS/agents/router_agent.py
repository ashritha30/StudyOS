



class RouterAgent:

    def route(self, query):

        query = query.lower()

        if "upload" in query or "pdf" in query:
            return "📄 Knowledge Agent"

        elif "summary" in query:
            return "📝 Summary Agent"

        elif "quiz" in query or "mcq" in query:
            return "❓ Quiz Agent"

        elif "study" in query or "plan" in query:
            return "📚 Study Agent"

        elif "gpa" in query:
            return "🎓 GPA Agent"

        elif "progress" in query:
            return "📈 Progress Agent"

        elif "memory" in query:
            return "🧠 Memory Agent"

        elif "dashboard" in query:
            return "📊 Dashboard Agent"

        elif "security" in query:
            return "🔒 Security Agent"

        elif "ask" in query or "question" in query:
            return "💬 Chat Agent"

        else:
            return "🤖 Router Agent"