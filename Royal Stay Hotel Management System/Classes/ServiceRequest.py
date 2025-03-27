from Guest import Guest  # Import Guest class to associate service requests with guests

class ServiceRequest:
    """
    Represents a service request made by a hotel guest.
    Examples: housekeeping, transportation, room service.
    Demonstrates association with the Guest class.
    """

    def __init__(self, requestId, guest, serviceType, status):
        """
        Constructor to initialize all service request details.
        Guest object is passed in (association relationship).
        """
        self.__request_id = requestId            # Private: unique ID for the service request
        self.__guest = guest                     # Association: Guest object who made the request
        self.__service_type = serviceType        # Private: type of service (e.g., Housekeeping)
        self.__status = status                   # Private: status of request (e.g., Pending, Completed)


    # Getter and Setter for request ID
    def getRequestId(self):
        """
        Returns the request ID.
        """
        return self.__request_id

    def setRequestId(self, requestId):
        """
        Sets the request ID.
        """
        self.__request_id = requestId


    # Getter and Setter for guest
    def getGuest(self):
        """
        Returns the Guest object associated with the request.
        """
        return self.__guest

    def setGuest(self, guest):
        """
        Sets the Guest object for this request.
        """
        self.__guest = guest


    # Getter and Setter for service type
    def getServiceType(self):
        """
        Returns the type of service requested (e.g., housekeeping, food).
        """
        return self.__service_type

    def setServiceType(self, serviceType):
        """
        Sets the service type.
        """
        self.__service_type = serviceType


    # Getter and Setter for status
    def getStatus(self):
        """
        Returns the current status of the service request.
        """
        return self.__status

    def setStatus(self, status):
        """
        Sets the status of the request.
        Example values: 'Pending', 'Completed', 'In Progress'
        """
        self.__status = status


    # Display method to show full request info
    def displayServiceRequestInfo(self):
        """
        Displays detailed information about the service request.
        Includes guest name using guest.getName().
        """
        print(f"Request ID: {self.__request_id}")
        print(f"Guest: {self.__guest.getName()}")         # Calls the guest's getter
        print(f"Service: {self.__service_type} | Status: {self.__status}")


    # String representation for easy printing
    def __str__(self):
        """
        Returns a summary of the service request.
        """
        return f"ServiceRequest {self.__request_id} | Type: {self.__service_type} | Status: {self.__status}"

