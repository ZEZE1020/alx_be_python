# daily_reminder.py

def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    reminder = f"'{task}' is a {priority} priority task"
    
    match priority:
        case 'high':
            reminder += " that requires immediate attention"
        case 'medium':
            reminder += ". Consider completing it soon"
        case 'low':
            reminder += ". Consider completing it when you have free time"
        case _:
            reminder = "Invalid priority level entered."

    if time_bound == 'yes':
        reminder += " today!"

    print(f"Reminder: {reminder}")

if __name__ == "__main__":
    main()
