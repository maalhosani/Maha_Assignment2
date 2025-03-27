class Invoice:
    """
    Represents an invoice generated for a specific booking.
    Demonstrates composition: An Invoice depends on a Booking.
    """

    def __init__(self, invoiceId, booking, charges, totalAmount):
        """
        Constructor to initialize invoice details.
        Includes composition: Invoice is tightly tied to a Booking.
        """
        self.__invoice_id = invoiceId             # Private: unique invoice ID
        self.__booking = booking                  # Composition: Booking object (Invoice belongs to a Booking)
        self.__charges = charges                  # Private: dictionary of individual charges
        self.__total_amount = totalAmount         # Private: total amount due for the invoice


    # Getter and Setter for invoice ID
    def getInvoiceId(self):
        """
        Returns the invoice ID.
        """
        return self.__invoice_id

    def setInvoiceId(self, invoiceId):
        """
        Sets the invoice ID.
        """
        self.__invoice_id = invoiceId

    # Getter and Setter for booking object
    def getBooking(self):
        """
        Returns the Booking object associated with this invoice.
        """
        return self.__booking

    def setBooking(self, booking):
        """
        Sets a new Booking object for the invoice.
        """
        self.__booking = booking


    # Getter and Setter for charges
    def getCharges(self):
        """
        Returns the dictionary of charges (e.g., {'Room': 500, 'Cleaning': 50}).
        """
        return self.__charges

    def setCharges(self, charges):
        """
        Sets the dictionary of charges.
        """
        self.__charges = charges


    # Getter and Setter for total amount
    def getTotalAmount(self):
        """
        Returns the total invoice amount.
        """
        return self.__total_amount

    def setTotalAmount(self, amount):
        """
        Sets the total amount for the invoice.
        Includes error handling to ensure input is numeric.
        """
        try:
            self.__total_amount = float(amount)   # Convert input to float
        except ValueError:
            print("Total amount must be a number.")  # Print error message for invalid input


    # Display method to show invoice information
    def displayInvoiceInfo(self):
        """
        Displays all invoice details including charges and total.
        """
        print(f"Invoice ID: {self.__invoice_id}")
        print(f"Booking: {self.__booking}")              # Uses __str__() of Booking class
        print(f"Charges: {self.__charges}")              # Prints dictionary of charges
        print(f"Total Amount: {self.__total_amount} AED")


    # String representation of the invoice
    def __str__(self):
        """
        Returns a short string summary of the invoice.
        """
        return f"Invoice {self.__invoice_id} | Total: {self.__total_amount} AED"

