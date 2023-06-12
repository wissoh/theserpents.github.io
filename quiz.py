class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer


def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        for i, option in enumerate(question.options):
            print(f"{i + 1}. {option}")

        user_answer = input("Enter your answer (1-4): ")
        if user_answer == question.answer:
            score += 1

        print()

    print("Quiz completed!")
    print(f"Your score: {score}/{len(questions)}")


# Create multiple-choice questions
question1 = Question("What is the capital of France?", ["1. London", "2. Paris", "3. Berlin", "4. Madrid"], "2")
question2 = Question("Which planet is known as the Red Planet?", ["1. Venus", "2. Mars", "3. Jupiter", "4. Saturn"], "2")
question3 = Question("What is the largest organ in the human body?", ["1. Heart", "2. Liver", "3. Skin", "4. Brain"], "3")
question4 = Question("Who painted the Mona Lisa?", ["1. Leonardo da Vinci", "2. Vincent van Gogh", "3. Pablo Picasso", "4. Claude Monet"], "1")

# Store the questions in a list
questions = [question1, question2, question3, question4]

# Run the quiz
run_quiz(questions)
