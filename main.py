from datetime import datetime

def main():
    name = input("What is your name? ").strip()
    year_str = input("Enter your birth year (e.g., 1995): ").strip()

    # Validate year
    try:
        birth_year = int(year_str)
    except ValueError:
        print("Invalid birth year. Please enter numbers only (e.g., 1995).")
        return

    current_year = datetime.now().year
    age = current_year - birth_year

    if age < 0:
        print("Birth year is in the future. Please check your input.")
        return

    print(f"\nHello {name}! You are approximately {age} years old.")

if __name__ == "__main__":
    main()
