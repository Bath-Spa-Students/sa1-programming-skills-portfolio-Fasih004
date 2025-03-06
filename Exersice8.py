# Simple Search Program
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Basic Task: Search for "Sam"
def basic_search():
    search_term = "Sam" 
    if search_term in names:
        print(f"'{search_term}' was found in the list.")
    else:
        print(f"'{search_term}' was not found in the list.")

# Optional Task: Allow user to input the search term
def optional_search():
    search_term = input("Enter the name to search for: ") 
    if search_term in names:
        print(f"'{search_term}' was found in the list.")
    else:
        print(f"'{search_term}' was not found in the list.")

if __name__ == "__main__":
    print("--- Basic Search ---")
    basic_search()  # Run the basic search task

    print("\n--- Optional Search ---")
    optional_search()  # Run the optional search task