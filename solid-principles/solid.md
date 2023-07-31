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