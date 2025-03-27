class Room:
    """
    Represents a hotel room with details like room number, type, price per night, and availability status.
    This class is part of the Hotel-Booking system.
    """

    def __init__(self, roomNumber, roomType, pricePerNight, isAvailable=True):
        """
        Constructor to initialize the room attributes.
        It uses private variables to enforce encapsulation.
        Includes a try-except block to catch data type errors.
        """
        try:
            self.__room_number = int(roomNumber)              # Private: Room number must be an integer
            self.__room_type = roomType                       # Private: Room type as string (e.g., Single, Double)
            self.__price_per_night = float(pricePerNight)     # Private: Convert price to float
            self.__is_available = bool(isAvailable)           # Private: Availability status (True/False)
        except ValueError:
            print("Invalid data type for Room attributes.")   # Handle invalid input errors gracefully


    # Getter and Setter for room number

    def getRoomNumber(self):
        """
        Returns the room number.
        """
        return self.__room_number

    def setRoomNumber(self, roomNumber):
        """
        Sets the room number (expects an integer).
        """
        try:
            self.__room_number = int(roomNumber)              # Validate input before setting
        except ValueError:
            print("Room number must be an integer.")          # Error if user enters a non-integer value


    # Getter and Setter for room type
    def getRoomType(self):
        """
        Returns the room type (e.g., Single, Double, Suite).
        """
        return self.__room_type

    def setRoomType(self, roomType):
        """
        Sets the room type as a string.
        """
        self.__room_type = roomType                           # No conversion needed; accepts string


    # Getter and Setter for price per night
    def getPricePerNight(self):
        """
        Returns the price per night for the room.
        """
        return self.__price_per_night

    def setPricePerNight(self, price):
        """
        Sets the price per night (expects a float value).
        """
        try:
            self.__price_per_night = float(price)             # Convert and set price
        except ValueError:
            print("Price must be a number.")                  # Handle invalid input like string


    # Getter and Setter for availability
    def getAvailability(self):
        """
        Returns True if the room is available, else False.
        """
        return self.__is_available

    def setAvailability(self, status):
        """
        Sets the availability status (expects boolean).
        """
        self.__is_available = bool(status)                    # Cast to boolean just in case


    # Display method to show room details
    def displayRoomInfo(self):
        """
        Prints the string representation of the room using __str__().
        """
        print(self.__str__())


    # Custom string output for room info
    def __str__(self):
        """
        Returns a string with all room details formatted.
        """
        return f"Room {self.__room_number} | Type: {self.__room_type} | Price: {self.__price_per_night} AED | Available: {self.__is_available}"
