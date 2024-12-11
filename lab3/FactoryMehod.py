from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        return f"Creator: Working with {product.operation()}"


class CreatorA(Creator):
    def factory_method(self):
        return ProductA()


class CreatorB(Creator):
    def factory_method(self):
        return ProductB()


class Product(ABC):
    @abstractmethod
    def operation(self):
        pass


class ProductA(Product):
    def operation(self):
        return "Result of ConcreteProductA"


class ProductB(Product):
    def operation(self):
        return "Result of ConcreteProductB"


creator = CreatorA()
print(creator.some_operation())
