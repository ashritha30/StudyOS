# def calculate_required_gpa(
#     current,
#     target,
#     completed,
#     total
# ):

#     remaining = total - completed

#     if remaining <= 0:
#         return None

#     required = (
#         (target * total)
#         - (current * completed)
#     ) / remaining

#     return round(required, 2)

from skills.gpa_skill import (
    calculate_required_gpa
)


class GPAAgent:

    def calculate_path(
        self,
        current,
        target,
        completed,
        total
    ):

        required = calculate_required_gpa(
            current,
            target,
            completed,
            total
        )

        if required is None:

            return {
                "status": "error",
                "message":
                "No semesters remaining."
            }

        return {
            "status": "success",
            "required_gpa": required,
            "message":
            f"Maintain {required} GPA for the remaining semesters."
        }