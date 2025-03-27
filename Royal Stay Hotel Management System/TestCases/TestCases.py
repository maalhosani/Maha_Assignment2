# Import all required classes from their respective files
from Guest import Guest
from Room import Room
from Hotel import Hotel
from Booking import Booking
from Invoice import Invoice
from Payment import Payment
from TypesOfPayments import TypesOfPayments
from ServiceRequest import ServiceRequest

print("TEST CASES START:")
print()


# Test 1: Guest Account Creation
print("Test 1: Guest Account Creation")

try:
    # Create two guests with name, email, phone, and loyalty points
    guest1 = Guest("Reem", "Reem@example.com", 1234567890, 50)
    guest2 = Guest("Maha", "maha@example.com", 9876543210, 120)
except Exception as e:
    # Handle errors if any values are incorrect
    print("Error during guest creation:", e)
else:
    # Display guest info if no exception occurred
    guest1.displayGuestInfo()
    guest2.displayGuestInfo()
finally:
    print()  # Line spacing for clarity


# Test 2: Searching for Available Rooms
print("Test 2: Searching for Available Rooms")

# Create 3 room objects
room1 = Room(101, "Single", 250.0, True)
room2 = Room(102, "Suite", 500.0, False)
room3 = Room(103, "Single", 250.0, True)

# Create hotel and add the rooms (composition)
hotel = Hotel("Royal Stay", "Dubai")
hotel.addRoom(room1)
hotel.addRoom(room2)
hotel.addRoom(room3)

# Search and display only available single rooms
print("Searching for available 'Single' rooms:")
for room in hotel.getRooms():
    if room.getRoomType() == "Single" and room.getAvailability():
        room.displayRoomInfo()
print()


# Test 3: Making a Room Reservation
print("Test 3: Making a Room Reservation")

try:
    # Create bookings between guests and rooms with dates and prices
    booking1 = Booking("B001", guest1, room1, "2025-04-01", "2025-04-03", 500)
    booking2 = Booking("B002", guest2, room3, "2025-04-02", "2025-04-04", 500)

    # Store the bookings in guest reservation history
    guest1.setReservationHistory([booking1])
    guest2.setReservationHistory([booking2])
except Exception as e:
    # Catch any issues with booking creation
    print("Error during booking:", e)
else:
    # Display booking details if successful
    booking1.displayBookingInfo()
    print()
    booking2.displayBookingInfo()
finally:
    print()  # Add space after test


# Test 4: Booking Confirmation Notification
print("Test 4: Booking Confirmation Notification")

# Print booking confirmation using getters
print(f"Booking confirmed for {guest1.getName()} with ID {booking1.getBookingId()}")
print(f"Booking confirmed for {guest2.getName()} with ID {booking2.getBookingId()}")
print()


# Test 5: Invoice Generation for a Booking
print("Test 5: Invoice Generation")

# Create invoices with individual charges for each booking
charges1 = {"Room Charge": 500.0, "Cleaning Fee": 50.0}
invoice1 = Invoice("I001", booking1, charges1, 550.0)

charges2 = {"Room Charge": 500.0, "Mini Bar": 75.0}
invoice2 = Invoice("I002", booking2, charges2, 575.0)

# Display the invoice details
invoice1.displayInvoiceInfo()
print()
invoice2.displayInvoiceInfo()
print()


# Test 6: Processing Different Payment Methods
print("Test 6: Payment Processing")

# Test credit card payment (Visa) and cash payment
payment1 = TypesOfPayments("P001", invoice1, "Card", "Completed", "Visa", "")
payment2 = TypesOfPayments("P002", invoice2, "Cash", "Pending", "", "Cash Accepted")

# Display base payment info + additional type details
payment1.displayPaymentInfo()
payment1.displayPaymentTypes()
print()
payment2.displayPaymentInfo()
payment2.displayPaymentTypes()
print()


# Test 7: Displaying Reservation History
print("Test 7: Displaying Reservation History")

# Loop through reservation history for each guest
for booking in guest1.getReservationHistory():
    booking.displayBookingInfo()
    print()
for booking in guest2.getReservationHistory():
    booking.displayBookingInfo()
print()


# Test 8: Cancellation of a Reservation
print("Test 8: Cancellation of Reservation")

# First cancellation: Guest1 and Room1
guest1.setReservationHistory([])  # Clear guest1's bookings
room1.setAvailability(True)       # Set room1 as available
print(f"Reservation for guest {guest1.getName()} cancelled.")
print(f"Room {room1.getRoomNumber()} is now available: {room1.getAvailability()}")
print()

# Second cancellation: Guest2 and Room3
guest2.setReservationHistory([])  # Clear guest2's bookings
room3.setAvailability(True)       # Set room3 as available
print(f"Reservation for guest {guest2.getName()} cancelled.")
print(f"Room {room3.getRoomNumber()} is now available: {room3.getAvailability()}")
print()



# Test 9: Guest Service Request
print("Test 9: Guest Service Request")

try:
    # Create two different service requests for two guests
    request1 = ServiceRequest("R001", guest2, "Room Cleaning", "Pending")
    request2 = ServiceRequest("R002", guest1, "Transportation to Airport", "Completed")

    # Display service request info
    print("Displaying guest requests:")
    request1.displayServiceRequestInfo()
    print()
    request2.displayServiceRequestInfo()
except Exception as e:
    # Catch and print any error
    print("Error handling service request:", e)
print()


# Test 10: Direct Payment Class Test (Parent of TypesOfPayments)
print("Test 10: Direct Payment Class Test")

try:
    # First base payment using the Payment class
    payment_base1 = Payment("P000", invoice1, "Debit Card", "Confirmed")
    payment_base1.displayPaymentInfo()  # Should print ID, method, and status

    print()

    # Second base payment using another payment method
    payment_base2 = Payment("P003", invoice2, "Apple Pay", "Failed")
    payment_base2.displayPaymentInfo()  # Should print ID, method, and status
except Exception as e:
    # If any error occurs during Payment creation or display
    print("Error in base Payment class:", e)

print()

