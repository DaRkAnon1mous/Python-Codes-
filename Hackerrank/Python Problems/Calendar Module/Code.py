from datetime import datetime

def get_day_of_week():
    # Take input from the user in "DD MM YYYY" format
    date_input = input()
    
    try:
        # Parse the input date string into a datetime object
        date_object = datetime.strptime(date_input, "%m %d %Y")
        
        # Get the day of the week in uppercase
        day_of_week = date_object.strftime("%A").upper()
        
        # Print the result
        print(day_of_week)
    except ValueError:
        # Handle invalid input format
        print("Invalid date format. Please enter the date in 'DD MM YYYY' format (e.g., 08 05 2015).")

# Run the function
get_day_of_week()
