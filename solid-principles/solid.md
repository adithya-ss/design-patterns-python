# Single Responsibility Principle
- Also called as 'Seperation of Concerns'
- A class should have a primary responsibility and should not have additional responsibilities

Antipatterns - Opposite of a particular pattern.
Ex: God object: Everything in the same class

# Open-closed Principle:
- When a new functionality is added, it should be extended not modified.
- OPEN for extension CLOSED for modification.
- Enterprise pattern: Specification
- Combinator: Combination of multiple structures

# Liskov Substitution Principle:
- Use properties instead of exposing attributes
- Whenever there is an interface taking some sort of a base class, we should be able to stick in any of its inheriters and expect nothing to break.
- Any inheritance model that adheres to the Liskov Substitution Principle will implicitly follow the Open/Closed principle.

# Interface Segregration Principle:
- Have interfaces with defined responsibilities/specific functions, instead of having a big list of features/functions which might not be used by other classes which implement it.
- We can also use compositions, to acheive the segreation of interfaces.

# Dependency Inversion Principle:
- This does not relate to dependency injection. Both are different.
- High level classes/modules should not depend on low-level modules, but should depend on the abstractions (Interfaces).
- In our example, for cases like unit testing, there is no need to go into something like a database. We could rather have an in-memory storage, by using the same interface to build another class - Data in-memory and exposed to the unit tests.
