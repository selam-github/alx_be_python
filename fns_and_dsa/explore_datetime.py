# explore_datetime.py
import datetime
def display_current_datetime():
    current_datetime = datetime.datetime.now()  
    current_date = current_datetime.date() #Save the current date in a variable current_date
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        print("Current date and time:", formatted_datetime)


def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add: "))
    current_date = datetime.date.today()
    future_date = current_date + datetime.timedelta(days=number_of_days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
        display_current_datetime()
            calculate_future_date()
        

