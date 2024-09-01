def is_window_seat(seats_per_row, seat_number):
    if seats_per_row <= 0:
        print("Invalid Input")
        return
    
    # Total number of seats in the bus
    total_seats = 11 * seats_per_row
    
    if seat_number <= 0 or seat_number > total_seats:
        print("Invalid Seat Number")
        return

    position_in_row = (seat_number - 1) % seats_per_row + 1
    
    if position_in_row == 1 or position_in_row == seats_per_row:
        print("Window Seat")
    else:
        print("Not a Window Seat")

# Input from user
try:
    seats_per_row = int(input("Enter the number of seats per row\n"))
    seat_number = int(input("Enter the seat number\n"))
    is_window_seat(seats_per_row, seat_number)
except ValueError:
    print("Invalid Input")
