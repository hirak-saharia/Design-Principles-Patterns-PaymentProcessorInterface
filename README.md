# Design Principles & Patterns "Abstraction using ABCs" - PaymentProcessorInterface
A framework for processing payments using different payment processors (like PayPal and Stripe) by leveraging abstract base classes and methods. This ensures that any new PaymentProcessorInterface must implement the process_payment method, maintaining a consistent interface.


Let's break through the code from a design perspective, focusing on principles and patterns:

### 1. **Abstraction**:
The `PaymentProcessorInterface` class is an abstract base class (ABC). It defines a common interface for all payment processors without providing a concrete implementation. This allows us to define methods that must be created within any child classes built from the abstract class.

### 2. **Encapsulation**:
Each payment processing (e.g., `ProcessingByPayPall`, `ProcessingByStripe`) encapsulates the details of how a payment is processed. The `process_payment` method in each subclass contains the specific logic for processing payments via PayPal or Stripe, respectively. This hides the implementation details from the rest of the application.

### 3. **Polymorphism**:
Polymorphism allows objects of different classes to be treated as objects of a common super class. In this case, `ProcessingByPayPall` and `ProcessingByStripe` can both be used wherever a `PaymentProcessorInterface` is expected. The `processing_order` function demonstrates this by accepting any `PaymentProcessorInterface` instance and calling its `process_payment` method.

### 4. **Dependency Injection**:
The `processing_order` function takes a `PaymentProcessorInterface` instance as a parameter. This is an example of dependency injection, where the dependency (the payment processor) is passed into the function rather than being created inside it. This makes the function more flexible and easier to test.

### 5. **Single Responsibility Principle (SRP)**:
Each class has a single responsibility:
- `PaymentProcessorInterface` defines the interface for payment processing.
- `ProcessingByPayPall` handles PayPal-specific payment processing.
- `ProcessingByStripe` handles Stripe-specific payment processing.
- `processing_order` handles the order processing logic.

### 6. **Open/Closed Principle (OCP)**:
The design is open for extension but closed for modification. We can add new payment processors (e.g., `SquareProcessor`) without modifying the existing code. We just need to create a new subclass of `PaymentProcessorInterface` and implement the `process_payment` method.

### 7. **Liskov Substitution Principle (LSP)**:
Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program. Here, any instance of `PaymentProcessorInterface` can be replaced with an instance of `ProcessingByPayPall` or `ProcessingByStripe` without changing the behavior of the `processing_order` function.

### 8. **Interface Segregation Principle (ISP)**:
The `PaymentProcessorInterface` interface is simple and focused, requiring only the `process_payment` method. This ensures that subclasses are not forced to implement methods they do not use.

### 9. **Dependency Inversion Principle (DIP)**:
High-level modules (like `processing_order`) should not depend on low-level modules (like `ProcessingByPayPall` or `ProcessingByStripe`). Both should depend on abstractions (`PaymentProcessorInterface`). This is achieved by passing a `PaymentProcessorInterface` instance to the `processing_order` function.

### Conclusion:
This design leverages several key object-oriented principles and design patterns to create a flexible, maintainable, and scalable payment processing system. By using abstraction, encapsulation, polymorphism, and dependency injection, the code is well-structured and adheres to SOLID principles, making it easy to extend and maintain.
