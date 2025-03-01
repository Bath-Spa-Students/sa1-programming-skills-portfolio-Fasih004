#Asking the capital of France
answer = input("What is the capital of France? ")
if answer == "Paris":
    print("Correct! The capital of France is Paris.")
else:
    print("Wrong! The capital of France is Paris.")


#Advanced Requirement Task

#Quiz for 10 European countries ignoring capitalization
questions = {
    "Sweden": "Stockholm",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Russia": "Moscow",
    "United Kingdom": "London",
    "Norway": "Oslo",
    "Denmark": "Copenhagen",
    "Monaco": "Monaco",
    "Ireland": "Dublin",
    "Hungary": "Budapest",
    
}

score = 0

for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ")
    if answer.lower() == capital.lower():
        print("Thats Right!")
        score += 1
    else:
        print(f"Incorrect :( The capital of {country} is {capital}.")

print(f"Quiz over, Your score is {score}/{len(questions)}.")