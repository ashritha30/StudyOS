import streamlit as st

from agents.knowledge_agent import extract_text_from_pdf
from utils.security import is_safe_input
from agents.study_agent import StudyAgent
from agents.quiz_agent import QuizAgent
from agents.gpa_agent import GPAAgent
from agents.router_agent import RouterAgent
from agents.ProgressAgent import ProgressAgent
from agents.summary_agent import SummaryAgent
from utils.memory_manager import load_memory
from agents.chat_agent import ChatAgent
import pandas as pd
import random




# -----------------------------
# Agent Objects
# -----------------------------
quiz_agent = QuizAgent()
gpa_agent = GPAAgent()
router = RouterAgent()
summary_agent = SummaryAgent()

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="StudyOS",
    page_icon="📚",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📚 StudyOS")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Upload PDF",
        "Security",
        "Summary",
        "Study Planner",
        "Ask Your Notes",
        "Quiz Generator",
        "GPA Advisor",
        "Progress Tracker",
        "Student Memory",
        "Dashboard"
        
    ]
)

current_agent = router.route(page)

st.sidebar.success(
    f"Active Agent: {current_agent}"
)

# -----------------------------
# Home Page
# -----------------------------
if page == "Home":

    st.title("📚 StudyOS")

    st.subheader("AI Student Companion")

    st.write(
        """
        Welcome to StudyOS.

        A Multi-Agent Academic Assistant designed to help students:

        • Upload Notes/PDFs
        • Generate Study Plans
        • Create Quizzes
        • Track GPA
        • Improve Learning Productivity
        """
    )

    st.markdown("---")
    st.subheader("🤖 AI Agent Router")

    user_request = st.text_input(
        "Describe what you want to do:"
    )

    if st.button("Route Request"):

        result = router.route(user_request)

        st.success(
            f"Selected Agent: {result}"
        )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📄 Knowledge Agent")
        st.info("📚 Study Agent")

    with col2:
        st.info("❓ Quiz Agent")
        st.info("🎓 GPA Agent")
# -----------------------------
# Upload PDF Page
# -----------------------------
elif page == "Upload PDF":

    st.title("📄 Upload PDF")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        # File size validation
        if uploaded_file.size > 5 * 1024 * 1024:

            st.error(
                "File too large. Maximum 5MB allowed."
            )

        else:

            text = extract_text_from_pdf(
                uploaded_file
            )

            st.session_state["pdf_text"] = text

            st.success(
                "PDF Uploaded Successfully"
            )

            st.text_area(
                "Extracted Content",
                text,
                height=300
            )
        
# -----------------------------
# Security Layer
# -----------------------------
elif page == "Security":

    st.title("🔒 Security Features")

    st.success(
        "Prompt Injection Protection Enabled"
    )

    st.success(
        "Input Validation Enabled"
    )

    st.success(
        "File Size Validation Enabled"
    )

    st.info(
        "StudyOS blocks unsafe instructions and suspicious inputs."
    )
 # -----------------------------
# Summary
# -----------------------------
elif page == "Summary":

    st.title("📄 PDF Summary")

    pdf_text = st.session_state.get(
        "pdf_text",
        ""
    )

    if not pdf_text:

        st.warning(
            "Upload PDF First"
        )

    else:

        summary = (
            summary_agent.generate_summary(
                pdf_text
            )
        )

        st.success(
            "Summary Generated"
        )

        st.text_area(
            "Summary",
            summary,
            height=300
        )
# -----------------------------
# Study Planner Page
# -----------------------------
elif page == "Study Planner":

    st.title("📚 Study Planner")

    st.info(
        "Study plan will be generated from uploaded PDF content."
    )

    days = st.number_input(
        "Number of Days",
        min_value=1,
        value=7
    )

    if st.button("Generate Study Plan"):

        pdf_text = st.session_state.get(
            "pdf_text",
            ""
        )

        if not pdf_text:

            st.warning(
                "Please upload a PDF first."
            )

        elif not is_safe_input(pdf_text):

            st.error(
                "Unsafe content detected."
            )

        else:

            study_agent = StudyAgent()

            plan = study_agent.generate_plan(
                pdf_text,
                days
            )

            st.success(
                "Study Plan Generated"
            )

            st.text_area(
                "Generated Plan",
                plan,
                height=300
            )
# -----------------------------
# Ask Your Notes
# -----------------------------
elif page == "Ask Your Notes":

    st.title("💬 Ask Your Notes")

    st.info(
        "Ask any question about the uploaded PDF."
    )

    question = st.text_input(
        "Enter your question"
    )

    if st.button("Ask AI"):

        pdf_text = st.session_state.get(
            "pdf_text",
            ""
        )

        if not pdf_text:

            st.warning(
                "Please upload a PDF first."
            )

        elif not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            chat_agent = ChatAgent()

            answer = chat_agent.ask_question(
                pdf_text,
                question
            )

            st.success("Answer")

            st.write(answer)
# -----------------------------
# Quiz Generator Page
# -----------------------------
elif page == "Quiz Generator":

    st.title("❓ Quiz Generator")

    st.info(
        "Quiz will be generated from uploaded PDF content."
    )

    if st.button("Generate Quiz"):

        pdf_text = st.session_state.get(
            "pdf_text",
            ""
        )

        if not pdf_text:

            st.warning(
                "Please upload a PDF first."
            )

        elif not is_safe_input(pdf_text):

            st.error(
                "Unsafe content detected."
            )

        else:

            quiz = quiz_agent.generate_quiz(
                pdf_text
            )

            st.success(
                "Quiz Generated Successfully"
            )

            st.text_area(
                "Generated Quiz",
                quiz,
                height=350
            )

# -----------------------------
# GPA Advisor Page
# -----------------------------
elif page == "GPA Advisor":

    st.title("🎓 GPA Advisor")

    current_cgpa = st.number_input(
        "Current CGPA",
        min_value=0.0,
        max_value=10.0,
        value=7.0
    )

    target_cgpa = st.number_input(
        "Target CGPA",
        min_value=0.0,
        max_value=10.0,
        value=8.0
    )

    completed_semesters = st.number_input(
        "Completed Semesters",
        min_value=1,
        max_value=8,
        value=4
    )

    total_semesters = st.number_input(
        "Total Semesters",
        min_value=1,
        max_value=8,
        value=8
    )

    if st.button("Analyze GPA Path"):

        result = gpa_agent.calculate_path(
            current_cgpa,
            target_cgpa,
            completed_semesters,
            total_semesters
        )

        if result["status"] == "success":

            st.success(
                result["message"]
            )

            st.write(
                f"Required GPA: {result['required_gpa']}"
            )

        else:

            st.error(
                result["message"]
            )
 # -----------------------------
# Progress Tracker
# -----------------------------
elif page == "Progress Tracker":

    st.title("📈 Progress Tracker")

    completed = st.number_input(
        "Completed Study Days",
        min_value=0,
        value=3
    )

    total = st.number_input(
        "Total Study Days",
        min_value=1,
        value=7
    )

    progress_agent = ProgressAgent()

    value = progress_agent.get_progress(
        completed,
        total
    )

    percentage = int(value * 100)

    st.progress(value)

    st.write(
        f"### 🎯 Progress: {percentage}%"
    )

    st.markdown("---")

    # -------------------------
    # Progress Statistics
    # -------------------------

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "✅ Completed",
            completed
        )

    with col2:
        st.metric(
            "📅 Remaining",
            total - completed
        )

    st.markdown("---")

    # -------------------------
    # Study Checklist
    # -------------------------

    st.subheader("📋 Study Checklist")

    st.checkbox(
        "📄 PDF Uploaded",
        value=completed >= 1,
        disabled=True
    )

    st.checkbox(
        "📝 Summary Generated",
        value=completed >= 2,
        disabled=True
    )

    st.checkbox(
        "❓ Quiz Completed",
        value=completed >= 3,
        disabled=True
    )

    st.checkbox(
        "📚 Study Plan Followed",
        value=completed >= 4,
        disabled=True
    )

    st.checkbox(
        "🎓 GPA Checked",
        value=completed >= 5,
        disabled=True
    )

    st.markdown("---")

    # -------------------------
    # Weekly Study Streak
    # -------------------------

    st.subheader("🔥 Study Streak")

    st.metric(
        "Current Streak",
        f"{completed} Days"
    )

    st.markdown("---")

    # -------------------------
    # Daily Goal
    # -------------------------

    st.subheader("🎯 Today's Goal")

    if percentage < 40:

        st.warning(
            "Complete today's study plan and generate a quiz."
        )

    elif percentage < 80:

        st.info(
            "Great progress! Continue revising your notes."
        )

    else:

        st.success(
            "Excellent! You're on track for your study goals."
        )

    st.markdown("---")

    # -------------------------
    # Motivation
    # -------------------------

    import random

    quotes = [

        "Consistency is more important than perfection.",

        "Small daily improvements lead to big results.",

        "Study today so your future self will thank you.",

        "Success begins with one focused study session.",

        "Every completed topic brings you closer to your goal."

    ]

    st.subheader("💡 Daily Motivation")

    st.success(
        random.choice(quotes)
    )
    
# -----------------------------
# Student Memory
# -----------------------------
elif page == "Student Memory":

    st.title("🧠 Student Memory")

    from utils.memory_manager import load_memory

    memory = load_memory()

    st.success(
        """
Welcome to Student Memory!

All your generated summaries, quizzes and study plans
are stored here for quick revision.
"""
    )

    st.markdown("---")

    # Search
    search = st.text_input(
        "🔍 Search your memory",
        placeholder="Search keyword..."
    )

    st.markdown("---")

    # -----------------------
    # Latest Summary
    # -----------------------
    st.subheader("📝 Latest Summary")

    if memory["summaries"]:

        latest_summary = memory["summaries"][-1]

        if search == "" or search.lower() in latest_summary.lower():

            with st.expander("View Summary", expanded=True):

                st.text_area(
                    "Summary",
                    latest_summary,
                    height=220
                )

                st.download_button(
                    "⬇ Download Summary",
                    latest_summary,
                    file_name="summary.txt"
                )

    else:

        st.info("No summary available.")

    st.markdown("---")

    # -----------------------
    # Latest Quiz
    # -----------------------
    st.subheader("❓ Latest Quiz")

    if memory["quizzes"]:

        latest_quiz = memory["quizzes"][-1]

        if search == "" or search.lower() in latest_quiz.lower():

            with st.expander("View Quiz"):

                st.text_area(
                    "Quiz",
                    latest_quiz,
                    height=250
                )

                st.download_button(
                    "⬇ Download Quiz",
                    latest_quiz,
                    file_name="quiz.txt"
                )

    else:

        st.info("No quiz available.")

    st.markdown("---")

    # -----------------------
    # Latest Study Plan
    # -----------------------
    st.subheader("📅 Latest Study Plan")

    if memory["plans"]:

        latest_plan = memory["plans"][-1]

        if search == "" or search.lower() in latest_plan.lower():

            with st.expander("View Study Plan"):

                st.text_area(
                    "Study Plan",
                    latest_plan,
                    height=250
                )

                st.download_button(
                    "⬇ Download Study Plan",
                    latest_plan,
                    file_name="study_plan.txt"
                )

    else:

        st.info("No study plan available.")

    st.markdown("---")

    # -----------------------
    # Memory Statistics
    # -----------------------

    st.subheader("📊 Memory Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Summaries",
            len(memory["summaries"])
        )

    with col2:
        st.metric(
            "Quizzes",
            len(memory["quizzes"])
        )

    with col3:
        st.metric(
            "Study Plans",
            len(memory["plans"])
        )

    st.markdown("---")

    # -----------------------
    # Clear Memory
    # -----------------------

    st.subheader("🗑 Memory Management")

    if st.button("Clear All Memory"):

        memory["summaries"] = []
        memory["quizzes"] = []
        memory["plans"] = []

        from utils.memory_manager import save_memory

        save_memory(memory)

        st.success("Memory Cleared Successfully!")

        st.rerun()

# -----------------------------
# Student Memory
# -----------------------------
elif page == "Student Memory":

    st.title("🧠 Student Memory")

    from utils.memory_manager import load_memory

    memory = load_memory()

    st.success(
        """
Welcome to Student Memory!

All your generated summaries, quizzes and study plans
are stored here for quick revision.
"""
    )

    st.markdown("---")

    # Search
    search = st.text_input(
        "🔍 Search your memory",
        placeholder="Search keyword..."
    )

    st.markdown("---")

    # -----------------------
    # Latest Summary
    # -----------------------
    st.subheader("📝 Latest Summary")

    if memory["summaries"]:

        latest_summary = memory["summaries"][-1]

        if search == "" or search.lower() in latest_summary.lower():

            with st.expander("View Summary", expanded=True):

                st.text_area(
                    "Summary",
                    latest_summary,
                    height=220
                )

                st.download_button(
                    "⬇ Download Summary",
                    latest_summary,
                    file_name="summary.txt"
                )

    else:

        st.info("No summary available.")

    st.markdown("---")

    # -----------------------
    # Latest Quiz
    # -----------------------
    st.subheader("❓ Latest Quiz")

    if memory["quizzes"]:

        latest_quiz = memory["quizzes"][-1]

        if search == "" or search.lower() in latest_quiz.lower():

            with st.expander("View Quiz"):

                st.text_area(
                    "Quiz",
                    latest_quiz,
                    height=250
                )

                st.download_button(
                    "⬇ Download Quiz",
                    latest_quiz,
                    file_name="quiz.txt"
                )

    else:

        st.info("No quiz available.")

    st.markdown("---")

    # -----------------------
    # Latest Study Plan
    # -----------------------
    st.subheader("📅 Latest Study Plan")

    if memory["plans"]:

        latest_plan = memory["plans"][-1]

        if search == "" or search.lower() in latest_plan.lower():

            with st.expander("View Study Plan"):

                st.text_area(
                    "Study Plan",
                    latest_plan,
                    height=250
                )

                st.download_button(
                    "⬇ Download Study Plan",
                    latest_plan,
                    file_name="study_plan.txt"
                )

    else:

        st.info("No study plan available.")

    st.markdown("---")

    # -----------------------
    # Memory Statistics
    # -----------------------

    st.subheader("📊 Memory Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Summaries",
            len(memory["summaries"])
        )

    with col2:
        st.metric(
            "Quizzes",
            len(memory["quizzes"])
        )

    with col3:
        st.metric(
            "Study Plans",
            len(memory["plans"])
        )

    st.markdown("---")

    # -----------------------
    # Clear Memory
    # -----------------------

    st.subheader("🗑 Memory Management")

    if st.button("Clear All Memory"):

        memory["summaries"] = []
        memory["quizzes"] = []
        memory["plans"] = []

        from utils.memory_manager import save_memory

        save_memory(memory)

        st.success("Memory Cleared Successfully!")

        st.rerun()



# -----------------------------
# Dashboard
# -----------------------------
elif page == "Dashboard":

    st.title("📊 StudyOS Dashboard")

    from utils.memory_manager import load_memory
    import pandas as pd

    memory = load_memory()

    summary_count = len(memory["summaries"])
    quiz_count = len(memory["quizzes"])
    plan_count = len(memory["plans"])

    total_activities = (
        summary_count
        + quiz_count
        + plan_count
    )

    # ---------------------------------
    # Welcome Card
    # ---------------------------------
    st.success(
        """
Welcome to StudyOS Analytics Dashboard!

Track your learning progress, generated summaries,
quizzes, study plans, and overall study activity.
"""
    )

    st.markdown("---")

    # ---------------------------------
    # Metrics
    # ---------------------------------
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📝 Summaries",
            summary_count
        )

    with col2:
        st.metric(
            "❓ Quizzes",
            quiz_count
        )

    with col3:
        st.metric(
            "📚 Study Plans",
            plan_count
        )

    with col4:
        st.metric(
            "🔥 Activities",
            total_activities
        )

    st.markdown("---")

    # ---------------------------------
    # Agent Usage Analytics
    # ---------------------------------
    st.subheader("📈 Agent Usage Analytics")

    df = pd.DataFrame({

        "Agent": [

            "Summary",

            "Quiz",

            "Study Plan"

        ],

        "Count": [

            summary_count,

            quiz_count,

            plan_count

        ]

    })

    st.bar_chart(
        df.set_index("Agent")
    )

    st.markdown("---")

    # ---------------------------------
    # Performance Insights
    # ---------------------------------
    st.subheader("🏆 Performance Insights")

    most_used = max(
        {
            "Summary": summary_count,
            "Quiz": quiz_count,
            "Study Plan": plan_count
        },
        key=lambda x: {
            "Summary": summary_count,
            "Quiz": quiz_count,
            "Study Plan": plan_count
        }[x]
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "⭐ Most Used Agent",
            most_used
        )

    with col2:

        st.metric(
            "📚 Study Sessions",
            total_activities
        )

    st.markdown("---")

    # ---------------------------------
    # Statistics
    # ---------------------------------
    st.subheader("📊 Learning Statistics")

    st.write(
        f"📄 Summaries Generated : **{summary_count}**"
    )

    st.write(
        f"❓ Quizzes Generated : **{quiz_count}**"
    )

    st.write(
        f"📚 Study Plans Generated : **{plan_count}**"
    )

    st.write(
        f"🔥 Total Activities : **{total_activities}**"
    )

    st.markdown("---")

  # ---------------------------------
# Smart Study Recommendation
# ---------------------------------
    import random

    st.subheader("💡 Smart Study Recommendation")

    beginner_tips = [
    "📚 Start by generating a summary before attempting quizzes.",
    "📝 Upload one chapter at a time for better understanding.",
    "🎯 Create a study plan before starting revision.",
    "📖 Read the summary first, then solve MCQs."
     ]

    intermediate_tips = [
    "🧠 Revise today's summary before moving to the next topic.",
    "❓ Solve at least 10 MCQs after every study session.",
    "📅 Follow your study plan consistently to improve retention.",
    "📚 Focus more on topics you find difficult."
    ]

    advanced_tips = [
    "🏆 Excellent progress! Challenge yourself with more quizzes.",
    "🎯 Revise weak topics before your next revision cycle.",
    "📖 Teach a concept to someone else to improve understanding.",
    "🚀 Maintain consistency to achieve your target GPA."
     ]

    if total_activities < 5:
        st.warning(random.choice(beginner_tips))

    elif total_activities < 15:
        st.info(random.choice(intermediate_tips))

    else:
        st.success(random.choice(advanced_tips))

    st.markdown("---")

# ---------------------------------
# Daily Motivation
# ---------------------------------
    st.subheader("🎯 Daily Motivation")

    quotes = [
    "Success is the sum of small efforts repeated every day.",
    "Consistency beats intensity.",
    "Every page you study today reduces stress tomorrow.",
    "Learning never exhausts the mind.",
    "Dream big. Study smart. Stay consistent."
    ]

    st.success(random.choice(quotes))