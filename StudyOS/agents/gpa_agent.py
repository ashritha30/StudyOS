from utils.memory_manager import load_memory, save_memory
class GPAAgent:

    def calculate_path(
        self,
        current_cgpa,
        target_cgpa,
        completed_semesters,
        total_semesters
    ):

        remaining = total_semesters - completed_semesters

        required = (
            target_cgpa * total_semesters
            - current_cgpa * completed_semesters
        ) / remaining

        if required > 10:

            advice = """
Target is very difficult.

• Increase semester SGPA significantly
• Focus on scoring subjects
• Reduce backlogs
"""

        elif required >= 8.5:

            advice = """
Target is achievable with strong effort.

• Maintain daily study schedule
• Score well in internals
• Practice previous papers
"""

        else:

            advice = """
Target is realistic.

• Continue consistent preparation
• Revise weekly
• Maintain attendance and assignments
"""

        return {
            "status": "success",
            "required_gpa": round(required, 2),
            "message": advice
        }