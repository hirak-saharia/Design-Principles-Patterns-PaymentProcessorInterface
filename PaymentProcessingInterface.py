"""1 - Importing Modules: Imports the ABC (Abstract Base Class) and abstractmethod from the abc module."""
from abc import ABC, abstractmethod

"""2 - Defining an Abstract Base Class:"""
"""
    PaymentProcessorInterface is an abstract base class that inherits from ABC.
     - The process_payment method is defined as an abstract method using the @abstractmethod decorator. This means any subclass of PaymentProcessorInterface must implement this method.
"""
class PaymentProcessorInterface(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass

""" 3 - Creating Subclasses---------"""
"""
    PayPalProcessor is a subclass of PaymentProcessorInterface.
        - It implements the process_payment method, printing a message indicating the payment is being processed via PayPal.
"""
class ProcessingByPayPall(PaymentProcessorInterface):
    def process_payment(self, amount: float) -> None:
        print(f" ${amount} has been processed via PayPall.")

""" 
    ProcessingByStripe is a subclass of PaymentProcessorInterface.
        - It implements the process_payment method, printing a message indicating the payment is being processed via Stripe.
"""
class ProcessingByStripe(PaymentProcessorInterface):
    def process_payment(self, amount: float) -> None:
        print(f" ${amount} has been processed via Stripe.")

"""4 - Processing an Order: 
    - The process_order function takes an amount and a processor (which must be an instance of PaymentProcessor or its subclass).
    - It calls the process_payment method on the provided processor, passing the amount.
"""
def processing_order(amount: float, processorInterface: PaymentProcessorInterface) -> None:
    processorInterface.process_payment(amount)

# usage
paypal_payment = ProcessingByPayPall()
stripe_payment = ProcessingByStripe()
processing_order(10.0, paypal_payment)
processing_order(10.0, stripe_payment)