class Payment:
    """
    Represents a payment made for an invoice.
    Demonstrates association with the Invoice class.
    """

    def __init__(self, paymentId, invoice, paymentMethod, status):
        """
        Constructor to initialize payment details.
        Invoice is passed as an object (association relationship).
        """
        self.__payment_id = paymentId                    # Private: unique ID for the payment
        self.__invoice = invoice                         # Association: invoice object this payment is linked to
        self.__payment_method = paymentMethod            # Private: method of payment (e.g., Card, Cash)
        self.__status = status                           # Private: status of payment (e.g., Completed, Pending)


    # Getter and Setter for payment ID
    def getPaymentId(self):
        """
        Returns the payment ID.
        """
        return self.__payment_id

    def setPaymentId(self, paymentId):
        """
        Sets the payment ID.
        """
        self.__payment_id = paymentId


    # Getter and Setter for associated invoice
    def getInvoice(self):
        """
        Returns the associated Invoice object.
        """
        return self.__invoice

    def setInvoice(self, invoice):
        """
        Sets the associated Invoice object.
        """
        self.__invoice = invoice


    # Getter and Setter for payment method
    def getPaymentMethod(self):
        """
        Returns the payment method used (e.g., Credit Card, Cash).
        """
        return self.__payment_method

    def setPaymentMethod(self, method):
        """
        Sets the payment method.
        """
        self.__payment_method = method


    # Getter and Setter for payment status
    def getStatus(self):
        """
        Returns the payment status (e.g., Completed, Failed).
        """
        return self.__status

    def setStatus(self, status):
        """
        Sets the payment status.
        """
        self.__status = status


    # Display method to show payment information
    def displayPaymentInfo(self):
        """
        Prints the payment ID, method, and status.
        """
        print(f"Payment ID: {self.__payment_id}")
        print(f"Payment Method: {self.__payment_method} | Status: {self.__status}")


    # String representation of the payment
    def __str__(self):
        """
        Returns a short string summary of the payment.
        """
        return f"Payment {self.__payment_id} | Status: {self.__status}"

