from Room import Room  # Import Room class for aggregation

class Hotel:
    """
    Represents a hotel that contains multiple rooms.
    Demonstrates aggregation: Hotel has a list of Room objects passed from outside.
    """

    def __init__(self, name, location):
        """
        Constructor to initialize the hotel's name and location.
        Also initializes an empty list to store Room objects.
        """
        self.__name = name                    # Private: name of the hotel
        self.__location = location            # Private: location of the hotel
        self._rooms = []                      # Protected: list of Room objects (aggregation relationship)


    # Getter and Setter for hotel name
    def getName(self):
        """
        Returns the name of the hotel.
        """
        return self.__name

    def setName(self, name):
        """
        Sets the name of the hotel.
        """
        self.__name = name

    # Getter and Setter for hotel location

    def getLocation(self):
        """
        Returns the location of the hotel.
        """
        return self.__location

    def setLocation(self, location):
        """
        Sets the location of the hotel.
        """
        self.__location = location

    # Getter for room list
    def getRooms(self):
        """
        Returns the list of Room objects associated with the hotel.
        """
        return self._rooms

    # Add a Room object to the hotel's list of rooms

    def addRoom(self, room):
        """
        Adds a Room object to the hotel.
        Ensures only valid Room instances are accepted (aggregation).
        """
        if isinstance(room, Room):              # Check if the object is an instance of Room
            self._rooms.append(room)           # Append room to the room list
        else:
            print("Only Room objects can be added.")  # Error message if invalid type is added


    # Display method to print hotel and room details
    def displayHotelInfo(self):
        """
        Prints hotel details and displays information for each associated room.
        """
        print(f"Hotel: {self.__name} | Location: {self.__location}")  # Print basic hotel info
        for room in self._rooms:  # Loop through all rooms and display their info
            room.displayRoomInfo()


    # String representation of the Hotel
    def __str__(self):
        """
        Returns a formatted string with hotel name and location.
        """
        return f"{self.__name} located in {self.__location}"

