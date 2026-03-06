class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")
        if self.text:
            lines.append(' ' * ((indent + 1) * self.indent_size) + self.text)
        for element in self.elements:
            lines.append(element.__str(indent + 1))
        lines.append(f"{i}</{self.name}>")
        return '\n'.join(lines)
    
    def __str__(self):
        return self.__str(0)
    
    @staticmethod
    def create(name):
        return HtmlBuilder(name)

    
class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def __create_child_element(self, child_name, child_text):
        child = HtmlElement(child_name, child_text)
        self.__root.elements.append(child)

    def add_child(self, child_name, child_text):
        self.__create_child_element(child_name, child_text)

    def add_child_fluent(self, child_name, child_text):
        self.__create_child_element(child_name, child_text)
        return self

    def __str__(self):
        return str(self.__root)

if __name__ == '__main__':
    builder = HtmlBuilder('ul')
    builder.add_child('li', 'hello')
    builder.add_child('li', 'world')
    print('Ordinary Builder:')
    print(builder)
    # ---
    builder = HtmlElement.create('ul')
    builder.add_child_fluent('li', 'hello').add_child_fluent('li', 'world')
    print('Fluent Builder:')
    print(builder)