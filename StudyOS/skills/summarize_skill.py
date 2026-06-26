

# def summarize_text(text):

#     lines = text.split("\n")

#     topics = []

#     remove_words = [
#         "dept",
#         "cse",
#         "soe",
#         "dsu",
#         "page",
#         "copyright",
#         "semester",
#         "hours"
#     ]

#     for line in lines:

#         line = line.strip()

#         if len(line) < 10:
#             continue

#         lower = line.lower()

#         skip = False

#         for word in remove_words:
#             if word in lower:
#                 skip = True

#         if skip:
#             continue

#         topics.append(line)

#     return list(dict.fromkeys(topics))[:10]




# def summarize_text(text):

#     lines = text.split("\n")

#     topics = []

#     remove_words = [
#         "dept",
#         "cse",
#         "soe",
#         "dsu",
#         "page",
#         "copyright",
#         "semester",
#         "hours"
#     ]

#     for line in lines:

#         line = line.strip()

#         if len(line) < 15:
#             continue

#         lower = line.lower()

#         skip = False

#         for word in remove_words:

#             if word in lower:
#                 skip = True
#                 break

#         if skip:
#             continue

#         topics.append(line)

#     topics = list(dict.fromkeys(topics))

#     summary = "📌 Key Topics\n\n"

#     for topic in topics[:5]:
#         summary += f"• {topic}\n"

#     summary += "\n📖 Important Concepts\n\n"

#     for topic in topics[5:8]:
#         summary += f"• {topic}\n"

#     summary += (
#         "\n🎯 Exam Tip\n\n"
#         "Revise the above concepts and practice MCQs "
#         "before the exam."
#     )

#     return summary


def summarize_text(text):

    lines = text.split("\n")

    topics = []

    remove_words = [
        "dept",
        "cse",
        "soe",
        "dsu",
        "page",
        "copyright",
        "semester",
        "hours"
    ]

    for line in lines:

        line = line.strip()

        if len(line) < 15:
            continue

        lower = line.lower()

        skip = False

        for word in remove_words:

            if word in lower:
                skip = True
                break

        if skip:
            continue

        topics.append(line)

    topics = list(dict.fromkeys(topics))

    return topics