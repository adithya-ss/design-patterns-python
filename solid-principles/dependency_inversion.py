from enum import Enum
from abc import ABC, abstractmethod


class Relationship(Enum):
    PARENT = 1
    CHILD = 2
    SIBLING = 3


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


# This is the low-level module that manages the relationships between people. It implements the RelationshipBrowser 
# interface,
class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))
    
    def add_sibling(self, sibling1, sibling2):
        self.relations.append((sibling1, Relationship.SIBLING, sibling2))
        self.relations.append((sibling2, Relationship.SIBLING, sibling1))
    
    def find_all_children_of(self, name):
        """
        Find all children of a person with the given name.
        """
        # This approach is better than the one in ResearchWithoutDIP because it abstracts away the details of how the 
        # relationships are stored.
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


# High-level module
# This module breaks the Dependency Inversion Principle because it depends on the low-level module (Relationships) directly.
# If the type of relations changes from list to something else, we would have to change the Research class as well, 
# which is not ideal.
class ResearchWithoutDIP:
    def __init__(self, relationships):
        relations = relationships.relations
        for r in relations:
            if r[0].name == 'John' and r[1] == Relationship.PARENT:
                print(f"John has a child named {r[2].name}")

# This is still a high-level module, but it now depends on the abstraction (RelationshipBrowser) rather than the concrete 
# implementation (Relationships).
class ResearchWithDIP:
    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f"John has a child named {p}")

if __name__ == '__main__':
    parent = Person('John')
    child1 = Person('Chris')
    child2 = Person('Matt')

    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    research = ResearchWithoutDIP(relationships)
    research_with_dip = ResearchWithDIP(relationships)
    