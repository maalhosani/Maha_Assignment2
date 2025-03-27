from Payment import Payment  # Import the base Payment class (for inheritance)

class TypesOfPayments(Payment):
    """
    Represents specific types of payment (credit card or cash).
    Inherits from the Payment class using single inheritance.
    """

    def __init__(self, paymentId, invoice, paymentMethod, status, creditCard, cash):
        """
        Constructor to initialize all attributes including inherited ones.
        Uses super() to initialize attributes from the parent Payment class.
        """
        super().__init__(paymentId, invoice, paymentMethod, status)  # Call parent constructor
        self._credit_card = creditCard     # Protected: credit card type (e.g., Visa, MasterCard)
        self._cash = cash                  # Protected: cash-related details (e.g., "Paid in cash")


    # Getter and Setter for credit card info
    def getCreditCard(self):
        """
        Returns the credit card information.
        """
        return self._credit_card

    def setCreditCard(self, creditCard):
        """
        Sets the credit card information.
        """
        self._credit_card = creditCard


    # Getter and Setter for cash info
    def getCash(self):
        """
        Returns the cash payment information.
        """
        return self._cash

    def setCash(self, cash):
        """
        Sets the cash payment information.
        """
        self._cash = cash


    # Display method for payment types
    def displayPaymentTypes(self):
        """
        Displays both credit card and cash details.
        """
        print(f"Credit Card: {self._credit_card} | Cash: {self._cash}")


    # String representation of payment type details
    def __str__(self):
        """
        Returns a string describing the specific payment types.
        """
        return f"TypesOfPayments | Credit Card: {self._credit_card} | Cash: {self._cash}"

