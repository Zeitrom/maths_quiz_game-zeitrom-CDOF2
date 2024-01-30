import random
import time

class QuizGame:
    def __init__(self, num_questions=10):
        self.num_questions = num_questions
        self.score = 0

    def generate_question(self):
        operand1 = random.randint(-100, 100)
        operand2 = random.randint(-100, 100)
        operator = random.choice(['+', '-', '*', '/'])

        if operator == '+':
            correct_answer = operand1 + operand2
        elif operator == '-':
            correct_answer = operand1 - operand2
        elif operator == '*':
            correct_answer = operand1 * operand2
        elif operator == '/':
            # Ensure the division is valid and not resulting in fractional answers
            if operand2 != 0 and operand1 % operand2 == 0:
                correct_answer = operand1 // operand2
            else:
                # If division is not valid, generate a new question
                return self.generate_question()

        return {
            'text': f"What is {operand1} {operator} {operand2}?",
            'correct_option': correct_answer
        }

    def ask_question(self, time_limit=10):
        question = self.generate_question()
        print(question['text'])

        while True:
            try:
                user_answer = float(input("Your answer: "))
                break  # Break out of the loop if the input is successfully converted to float
            except ValueError:
                print("Invalid input. Please enter a valid numeric answer.")

        start_time = time.time()
        end_time = time.time()

        time_taken = end_time - start_time
        if time_taken > time_limit:
            print(f"Time's up! The correct answer was {question['correct_option']}.")
        else:
            self.check_answer(question, user_answer)

    def check_answer(self, question, user_answer):
        if user_answer == question['correct_option']:
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer was {question['correct_option']}.")
        print(f"Your current score: {self.score}\n")

    def play(self):
        for _ in range(min(self.num_questions, 10)):
            self.ask_question()
        print(f"Game Over! Your final score: {self.score}")

# Create an instance of the QuizGame and start playing
quiz = QuizGame(num_questions=10)
quiz.play()
