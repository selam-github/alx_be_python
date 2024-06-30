task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
        case "high":
                    reminder = f"'{task}' is a high priority task"
                            if time_bound == "yes":
                                            reminder += " that requires immediate attention today!"
                                                    else:
                                                                    reminder += ". Make sure to complete it as soon as possible."
                                                                        case "medium":
                                                                                    reminder = f"'{task}' is a medium priority task"
                                                                                            if time_bound == "yes":
                                                                                                            reminder += " that you should aim to complete today."
                                                                                                                    else:
                                                                                                                                    reminder += ". Try to complete it soon."
                                                                                                                                        case "low":
                                                                                                                                                    reminder = f"'{task}' is a low priority task"
                                                                                                                                                            if time_bound == "yes":
                                                                                                                                                                            reminder += " that you should address by the end of the day."
                                                                                                                                                                                    else:
                                                                                                                                                                                                    reminder += ". Consider completing it when you have free time."
                                                                                                                                                                                                        case _:
                                                                                                                                                                                                                    reminder = f"'{task}' has an unknown priority level."

                                                                                                                                                                                                                    # Print the customized reminder
                                                                                                                                                                                                                    print("Reminder:", reminder)
