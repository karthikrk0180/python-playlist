# Constants
DAYS_IN_YEAR = 365.25
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60

# Input handler
def get_input():
    while True:
        try:
            age_in_years = float(input("Enter your age in years (e.g., 21.6): "))
            if age_in_years <= 0:
                print("⚠️  Age must be greater than 0. Please try again.")
                continue
            return age_in_years
        except ValueError:
            print("❌ Invalid input! Please enter a number like 23.5 — no text or symbols.")

# Calculation functions
def calculate_days(age):
    return age * DAYS_IN_YEAR

def calculate_hours(age):
    return calculate_days(age) * HOURS_IN_DAY

def calculate_minutes(age):
    return calculate_hours(age) * MINUTES_IN_HOUR

# Display functions
def display_menu():
    print("\n🧮 Let's calculate how long you've lived on Earth!")
    print("1. Show total Days")
    print("2. Show total Hours")
    print("3. Show total Minutes")
    print("4. Enter a new age")
    print("5. Exit the Application")

def main():
    age_in_years = get_input()

    while True:
        display_menu()
        choice = input("👉 Enter your choice (1-5): ").strip()

        match choice:
            case '1':
                days = calculate_days(age_in_years)
                print(f"\n📆 You have lived for approximately {round(days, 2)} days.")
            case '2':
                hours = calculate_hours(age_in_years)
                print(f"\n⏰ You have lived for approximately {round(hours, 2)} hours.")
            case '3':
                minutes = calculate_minutes(age_in_years)
                print(f"\n⏱️ You have lived for approximately {round(minutes, 2)} minutes.")
            case '4':
                print("\n🔄 Re-entering age...")
                age_in_years = get_input()
            case '5':
                print("\n👋 Thank you for using the Minutes Alive Calculator. Stay curious!")
                break
            case _:
                print("❗ Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
