class Guest:
    """
    Represents a hotel guest with personal information and loyalty points.
    Also stores their reservation history.
    """

    def __init__(self, name, email, phoneNumber, loyaltyPoints=0):
        """
        Constructor to initialize guest attributes.
        All attributes are private or protected for encapsulation.
        """
        self.__name = name                          # Private: guest's full name
        self.__email = email                        # Private: guest's email
        self.__phone_number = phoneNumber           # Private: phone number
        self.__loyalty_points = loyaltyPoints       # Private: loyalty points (default is 0)
        self._reservation_history = []              # Protected: list to store booking history (association)


    # Getter and Setter for name
    def getName(self):
        """
        Returns the guest's name.
        """
        return self.__name

    def setName(self, name):
        """
        Sets the guest's name.
        """
        self.__name = name


    # Getter and Setter for email
    def getEmail(self):
        """
        Returns the guest's email.
        """
        return self.__email

    def setEmail(self, email):
        """
        Sets the guest's email address.
        """
        self.__email = email


    # Getter and Setter for phone number
    def getPhoneNumber(self):
        """
        Returns the guest's phone number.
        """
        return self.__phone_number

    def setPhoneNumber(self, number):
        """
        Sets the guest's phone number.
        """
        self.__phone_number = number


    # Getter and Setter for loyalty points
    def getLoyaltyPoints(self):
        """
        Returns the guest's current loyalty points.
        """
        return self.__loyalty_points

    def setLoyaltyPoints(self, points):
        """
        Sets the guest's loyalty points.
        Includes a try-except block for input validation.
        """
        try:
            self.__loyalty_points = int(points)     # Convert to int and assign
        except ValueError:
            print("Points must be an integer.")     # Handle invalid input like text


    # Getter and Setter for reservation history
    def getReservationHistory(self):
        """
        Returns the list of bookings (reservation history).
        """
        return self._reservation_history

    def setReservationHistory(self, history):
        """
        Replaces the reservation history with a new list of bookings.
        """
        self._reservation_history = history


    # Display method to show guest info
    def displayGuestInfo(self):
        """
        Prints formatted guest information including loyalty points.
        """
        print(f"Name: {self.__name} | Email: {self.__email} | Phone: {self.__phone_number} | Loyalty Points: {self.__loyalty_points}")


    # String representation for guest
    def __str__(self):
        """
        Returns a short string summary of the guest.
        """
        return f"{self.__name} ({self.__email})"
