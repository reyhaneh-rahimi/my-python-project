from datetime import datetime, date

# -----------------------------------------
# Calculate age in years
# -----------------------------------------
def age_in_years():
    name = input("What is your name? ").strip()
    year_str = input("Enter your birth year (e.g., 1995): ").strip()

    try:
        birth_year = int(year_str)
    except ValueError:
        print("Invalid year. Use numbers only.")
        return

    current_year = datetime.now().year
    age = current_year - birth_year

    if age < 0:
        print("Birth year is in the future.")
        return

    print(f"\nHello {name}! You are approximately {age} years old.")

# -----------------------------------------
# Calculate age in days
# -----------------------------------------
def age_in_days():
    name = input("What is your name? ").strip()

    print("Enter your birth date:")
    year_str = input("  Year (e.g., 1995): ").strip()
    month_str = input("  Month (1-12): ").strip()
    day_str = input("  Day (1-31): ").strip()

    try:
        year = int(year_str)
        month = int(month_str)
        day = int(day_str)
        birth_date = date(year, month, day)
    except ValueError:
        print("Invalid date. Please enter correct year, month, and day.")
        return

    today = date.today()
    delta = today - birth_date

    if delta.days < 0:
        print("Birth date is in the future.")
        return

    print(f"\nHello {name}! You are {delta.days} days old.")

# -----------------------------------------
# MENU
# -----------------------------------------
def main():
    print("\nChoose an option:")
    print("1) Calculate age in YEARS")
    print("2) Calculate age in DAYS")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        age_in_years()
    elif choice == "2":
        age_in_days()
    else:
        print("Invalid option. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
2