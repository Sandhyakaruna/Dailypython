def check_window_seat():
    # Constants
    TOTAL_ROWS = 11
    
    # Input number of seats per row
    seats_per_row = int(input("Enter the number of seats per row\n"))
    
    # Validate number of seats per row
    if seats_per_row <= 0:
        print("Invalid Input")
        return
    
    # Input seat number
    seat_number = int(input("Enter the seat number\n"))
    
    # Validate seat number
    total_seats = TOTAL_ROWS * seats_per_row
    if seat_number <= 0 or seat_number > total_seats:
        print("Invalid Seat Number")
        return
    
    # Check if the seat number is a window seat
    if seat_number % seats_per_row == 0:
        print("Window Seat")
    else:
        print("Not a Window Seat")

# Call the function
check_window_seat()
