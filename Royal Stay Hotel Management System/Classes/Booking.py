from Guest import Guest          # Import Guest class (used in association)
from Room import Room            # Import Room class (used in aggregat

class Booking:
    """
    Represents a reservation made by a guest for a room.
    Demonstrates:
      - Association with Guest (passed in)
      - Aggregation with Room (passed in externally)
      - Composition with Invoice (usually created inside Booking, not shown here)
    """

    def __init__(self, bookingId, guest, room, checkInDate, checkOutDate, totalPrice):
        """
        Constructor to initialize booking details.
        Guest and Room are passed in as objects from outside (association/aggregation).
        """
        self.__booking_id = bookingId                  # Private: unique ID for the booking
        self.__guest = guest                           # Association: Guest object
        self.__room = room                             # Aggregation: Room object
        self.__check_in_date = checkInDate             # Private: check-in date as string
        self.__check_out_date = checkOutDate           # Private: check-out date as string
        self.__total_price = totalPrice                # Private: total price of the booking


    # Getter and Setter for booking ID
    def getBookingId(self):
        """
        Returns the booking ID.
        """
        return self.__booking_id

    def setBookingId(self, bookingId):
        """
        Sets the booking ID.
        """
        self.__booking_id = bookingId


    # Getter and Setter for guest object
    def getGuest(self):
        """
        Returns the Guest object linked to this booking.
        """
        return self.__guest

    def setGuest(self, guest):
        """
        Sets the Guest object for this booking.
        """
        self.__guest = guest


    # Getter and Setter for room object
    def getRoom(self):
        """
        Returns the Room object associated with this booking.
        """
        return self.__room

    def setRoom(self, room):
        """
        Sets the Room object for this booking.
        """
        self.__room = room


    # Getter and Setter for check-in date
    def getCheckInDate(self):
        """
        Returns the check-in date.
        """
        return self.__check_in_date

    def setCheckInDate(self, date):
        """
        Sets the check-in date.
        """
        self.__check_in_date = date


    # Getter and Setter for check-out date
    def getCheckOutDate(self):
        """
        Returns the check-out date.
        """
        return self.__check_out_date

    def setCheckOutDate(self, date):
        """
        Sets the check-out date.
        """
        self.__check_out_date = date


    # Getter and Setter for total price
    def getTotalPrice(self):
        """
        Returns the total price of the booking.
        """
        return self.__total_price

    def setTotalPrice(self, price):
        """
        Sets the total price (with float validation).
        """
        try:
            self.__total_price = float(price)         # Try converting to float
        except ValueError:
            print("Invalid total price.")             # Catch invalid input like strings


    # Display all booking details
    def displayBookingInfo(self):
        """
        Prints all the booking details including guest and room.
        """
        print(f"Booking ID: {self.__booking_id}")
        print(f"Guest: {self.__guest}")               # Will call Guest.__str__()
        print(f"Room: {self.__room}")                 # Will call Room.__str__()
        print(f"Check-In: {self.__check_in_date} | Check-Out: {self.__check_out_date}")
        print(f"Total Price: {self.__total_price} AED")


    # String representation of the booking
    def __str__(self):
        """
        Returns a short summary string for the booking.
        Uses the guest's name via guest.getName().
        """
        return f"Booking {self.__booking_id} for Guest {self.__guest.getName()}"

