# Function for the Basic Task
def basic_task():
    print("\n--- Basic Task ---")
    right_password = "12345"
    while True:
        password = input("Enter the password: ")
        if password == right_password:
            print("Correct password entered.")
            break
        else:
            print("Incorrect password. Try again.")

# Function for the Optional Task
def optional_task():
    print("\n--- Optional Task ---")
    right_password = "12345"
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        password = input("Enter the password: ")
        if password == right_password:
            print("Correct password entered.")
            break
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print(f"Incorrect password. {remaining_attempts} attempts remaining.")
            else:
                print("Incorrect password. Maximum attempts reached. Authorities have been alerted.")
                break

# Main Program
if __name__ == "__main__":
    # Run the Basic Task
    basic_task()

    # Run the Optional Task
    optional_task()