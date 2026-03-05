from abc import ABC, abstractmethod


class MachineWithoutISP():
    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(MachineWithoutISP):
    def print(self, document):
        # Implementation for printing
        print("MFP: Printing document...")

    def fax(self, document):
        # Implementation for faxing
        print("MFP: Faxing document...")

    def scan(self, document):
        # Implementation for scanning
        print("MFP: Scanning document...")


class OldFashionedPrinter(MachineWithoutISP):
    def print(self, document):
        # Implementation for printing
        print("OFP: Printing document...")

    def fax(self, document):
        pass  
        # This is option 01: Do nothing, but this is not ideal as it violates the principle of least surprise.
        # The implementer could forget that the OldFashionedPrinter does not support faxing and scanning, leading 
        # to unexpected behavior.

    def scan(self, document):
        raise NotImplementedError("OFP: This printer does not support scanning!")
        # This is option 02: Raise an exception to indicate that the operation is not supported. 
        # This clearly communicates to the user that the functionality is not available, adhering to the principle 
        # of least surprise.
        # However, it still violates the Interface Segregation Principle because the OldFashionedPrinter is forced 
        # to implement methods that it does not use.

# ******************************************************************************** #

# Instead of having a single interface (Machine) that includes all functionalities, we can segregate the interfaces 
# like below:
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        raise NotImplementedError
    

class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        raise NotImplementedError
    

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Printer, Fax, Scanner):
    """
    A multi-function printer that can print, fax, and scan documents.
    """
    def print(self, document):
        print("MFP: Printing document...")

    def fax(self, document):
        print("MFP: Faxing document...")

    def scan(self, document):
        print("MFP: Scanning document...")


class Photocopier(Printer, Scanner):
    """
    A photocopier that can print and scan documents, but does not support faxing.
    """
    # This now adheres to the Interface Segregation Principle because it only implements the interfaces that it needs.
    def print(self, document):
        print("PC: Printing document...")

    def scan(self, document):
        print("PC: Scanning document...")
    

class OldFashionedPrinter(Printer):
    """
    An old-fashioned printer that only supports printing documents.
    """
    # This also adheres to the Interface Segregation Principle because it only implements the Printer interface.
    def print(self, document):
        print("OFP: Printing document...")

# ******************************************************************************** #
# Another approach to implement a multi-function device is to use composition instead of inheritance.
# Compositions allow us to create a multi-function device that can delegate the responsibilities to the appropriate 
# components, adhering to the Interface Segregation Principle.

# Compositions are often more flexible than inheritance because they allow us to change the behavior of the 
# multi-function device at runtime by swapping out the components.
# For example, we could create a multi-function device that can print and fax documents, but does not support 
# scanning, by using a Printer and a Fax component, and leaving out the Scanner component.

class MultiFunctionDevice(Printer, Fax, Scanner):
    @abstractmethod
    def print(self, document):
        raise NotImplementedError
    @abstractmethod
    def fax(self, document):
        raise NotImplementedError
    @abstractmethod
    def scan(self, document):
        raise NotImplementedError


class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer: Printer, fax: Fax, scanner: Scanner):
        self.printer = printer
        self.fax = fax
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def fax(self, document):
        self.fax.fax(document)

    def scan(self, document):
        self.scanner.scan(document)