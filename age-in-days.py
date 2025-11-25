from datetime import datetime, date

def main():
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
        print("Invalid date. Please enter a valid year, month, and day.")
        return

    today = date.today()
    delta = today - birth_date

    if delta.days < 0:
        print("Birth date is in the future. Please check your input.")
        return

    print(f"\nHello {name}! You are {delta.days} days old.")

if __name__ == "__main__":
    main()
