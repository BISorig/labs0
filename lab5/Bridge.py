from abc import ABC, abstractmethod


class Implementor(ABC):
    @abstractmethod
    def operation_impl(self):
        pass


class ConcreteImplementorA(Implementor):
    def operation_impl(self):
        print("ConcreteImplementorA: Implementation.")


class ConcreteImplementorB(Implementor):
    def operation_impl(self):
        print("ConcreteImplementorB: Implementation.")


class Abstraction:
    def __init__(self, implementor: Implementor):
        self._implementor = implementor

    def operation(self):
        print("Abstraction: Base operation.")
        self._implementor.operation_impl()


class RefinedAbstraction(Abstraction):
    def operation(self):
        print("RefinedAbstraction: Extended operation.")
        self._implementor.operation_impl()


implementor = ConcreteImplementorA()
abstraction = RefinedAbstraction(implementor)
abstraction.operation()

implementor = ConcreteImplementorB()
abstraction = RefinedAbstraction(implementor)
abstraction.operation()
