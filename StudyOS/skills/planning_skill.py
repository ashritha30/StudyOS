def create_plan(topic, days):

    plan = []

    for day in range(1, days + 1):

        plan.append(
            f"Day {day}: Study {topic}"
        )

    return "\n".join(plan)