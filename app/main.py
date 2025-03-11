import json
from Questions.Question import Question  # ✅ Correct import

# Load JSON file
with open("Questions/questions.json", "r") as file:
    data = json.load(file)

# Extract questions
questions_list = []

for item in data["questions"]:
    # Create Question object
    question_obj = Question(
        question=item.get("question"),
        category=item.get("category"),
        format=item.get("type"),  # Assuming "type" refers to format
        subcategory=item.get("subCategory", None),
        answer=item.get("answer", None),
        options=item.get("options", []),
        examples=item.get("examples", []),
        hints=item.get("hints", []),
        explanation=item.get("explanation", None),
        image=item.get("image", None),
    )
    questions_list.append(question_obj)

# Print out all questions and answers
for q in questions_list:
    print(f"Q: {q.question}")
    print(f"A: {q.answer}\n")

while True:
    1==1