from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass


class Factory1(AbstractFactory):
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()


class Factory2(AbstractFactory):
    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()


class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self):
        pass


class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self):
        pass


class ProductA1(AbstractProductA):
    def operation_a(self):
        return "ProductA1"


class ProductB1(AbstractProductB):
    def operation_b(self):
        return "ProductB1"


class ProductA2(AbstractProductA):
    def operation_a(self):
        return "ProductA2"


class ProductB2(AbstractProductB):
    def operation_b(self):
        return "ProductB2"


factory = Factory1()
product_a = factory.create_product_a()
product_b = factory.create_product_b()

print(product_a.operation_a())
print(product_b.operation_b())
