#Storing the information in a dictionary
biography = {
    "name": "Fasih Ur Rehman",  
    "hometown": "Islamabad",  
    "age": 20
}

#Print the values on separate lines 
print(f"Name: {biography['name']} \nHometown: {biography['hometown']} \nAge: {biography['age']}")

#Advanced Requirement Task

#Have the user input thier name, hometown, and age
name = input("Enter your name: ")  
hometown = input("Enter your hometown: ")

 #Ensure age is a valid integer
while True:
    age_input = input("Enter your age: ")
    try:
        age = int(age_input)  
        break
    except ValueError:
        print("Enter a valid integer.")

#Storing the information in a dictionary
biography = {
    "name": name,
    "hometown": hometown,
    "age": age
}

#Print the values on separate lines
print(f"Name: {biography['name']}\nHometown: {biography['hometown']}\nAge: {biography['age']}")