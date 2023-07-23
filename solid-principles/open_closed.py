from enum import Enum


class Color(Enum):
    """
    Enum for colors
    """
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    """
    Enum for sizes
    """
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    """
    Main product class
    """
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    """
    To support open-closed, this class should be open only for extension.
    Ex: If a similar filter feature is required for size instead of colors, a new method filter_by_size should not be created in the same class.
    """
    def filter_by_color(self, products, color):
        """
        Method to filter the product based on their color
        """
        for product in products:
            if product.color == color:
                yield product
    
    # def filter_by_size(self, products, size):
    #     """
    #     The addition of this method would break the open-closed principle.
    #     """
    #     for product in products:
    #         if product.size == size:
    #             yield product
    
    # def filter_by_color(self, products, color, size):
    #     """
    #     The addition of this method would break the open-closed principle.
    #     """
    #     for product in products:
    #         if product.color == color and product.size == size:
    #             yield product


class Specification:
    """
    Base class whose methods are supposed to be overriden
    """
    def is_satisfied(self, item):
        """
        Method to override.
        """
        pass

    def __and__(self, other):
        """
        Overloading the and operator - BINARY AND (&)
        """
        return AndSpecification(self, other)


class Filter:
    """
    Base class whose methods are supposed to be overriden
    """
    def filter(self, items, spec):
        """
        Method to override.
        """
        pass


class ColorSpecification(Specification):
    """
    Specification class for color
    """
    def __init__(self, color):
        self.color = color
    
    def is_satisfied(self, item):
        """
        Overriden method to check for color
        """
        return item.color == self.color


class SizeSpecification(Specification):
    """
    Specification class for size
    """
    def __init__(self, size):
        self.size = size
    
    def is_satisfied(self, item):
        """
        Overriden method to check for size
        """
        return item.size == self.size


class AndSpecification(Specification):
    """
    Combinator class - Color and Size
    """
    def __init__(self, *args):
        self.args = args
    
    def is_satisfied(self, item):
        """
        Overriden method to check for color and size
        """
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))   


class CleanFilter(Filter):
    def filter(self, items, spec):
        """
        Overriden method to filter product based on the specification
        """
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    tshirt = Product('Lacoste Shirt TS001', Color.GREEN, Size.LARGE)
    jeans = Product('Levis Pant LP002', Color.BLUE, Size.MEDIUM)
    shoe = Product('Adidas Shoes AS003', Color.BLUE, Size.LARGE)
    hat = Product('Nike Hat NH004', Color.RED, Size.SMALL)

    products = [tshirt, jeans, shoe, hat]

    # OLD APPROACH
    product_filter = ProductFilter()
    print("Blue products are (OLD APPROACH - Specification not used):")
    for product in product_filter.filter_by_color(products=products, color=Color.BLUE):
        print(f" - {product.name} is blue")

    # SPECIFICATION PATTERN
    clean_filter = CleanFilter()
    print('Blue products are (NEW APPROACH - Specification used):')
    green_spec = ColorSpecification(Color.BLUE)
    for product in clean_filter.filter(items=products, spec=green_spec):
        print(f" - {product.name} is blue")

    print('Small products are (NEW APPROACH - Specification used):')
    small_spec = SizeSpecification(Size.SMALL)
    for product in clean_filter.filter(items=products, spec=small_spec):
        print(f" - {product.name} is small")

    print('Products which are blue and large are (NEW APPROACH - Specification used):')
    # blue_large = AndSpecification(ColorSpecification(Color.BLUE), SizeSpecification(Size.LARGE))
    # Alternative approach
    blue_large = ColorSpecification(Color.BLUE) & SizeSpecification(Size.LARGE)
    for product in clean_filter.filter(items=products, spec=blue_large):
        print(f" - {product.name} is blue and large")
