import math
import random

def square_root_quiz():
    print("Welcome to Corbins  Square Root Quiz.")
    print("Type exit at any time to quit and see your final score.\n")
    
    score = 0
    questions_asked = 0
    
    while True:
        # Generate a random perfect square between 1 and 400
        answer = random.randint(1, 20)
        number = answer ** 2
        
        user_input = input(f"Level {questions_asked + 1}: What is the square root of {number}? ")
        
        # Check if user wants to exit
        if user_input.lower().strip() == 'exit':
            break
            
        try:
            # Convert user answer to float for comparison
            user_answer = float(user_input)
            questions_asked += 1
            
            # Check correctness using math.sqrt()
            if user_answer == math.sqrt(number):
                print("Correct! 🎉\n")
                score += 1
            else:
                print(f"Incorrect. The square root of {number} is {int(math.sqrt(number))}. 😢\n")
                
        except ValueError:
            print("Invalid input! Please enter a number.\n")
            continue

    # Game over stats
    print("\n--- Game Over ---")
    if questions_asked > 0:
        print(f"You answered {score} out of {questions_asked} questions correctly!")
    else:
        print("You did not answer any questions but thanks for playing")

# Run the game
if __name__ == "__main__":
    square_root_quiz()