from abc import ABC, abstractmethod


class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_part_a(self):
        pass

    @abstractmethod
    def build_part_b(self):
        pass

    @abstractmethod
    def get_result(self):
        pass


class ConcreteBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product()

    def build_part_a(self):
        self._product.add("PartA")

    def build_part_b(self):
        self._product.add("PartB")

    def get_result(self):
        result = self._product
        self.reset()
        return result


class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return f"Product parts: {', '.join(self.parts)}"


class Director:
    def __init__(self, builder: Builder):
        self._builder = builder

    def construct_full_product(self):
        self._builder.build_part_a()
        self._builder.build_part_b()


builder = ConcreteBuilder()
director = Director(builder)

director.construct_full_product()
product = builder.get_result()
print(product.list_parts())
