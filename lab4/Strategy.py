from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, data: list):
        pass


class StrategyA(Strategy):
    def execute(self, data: list):
        return sorted(data)


class StrategyB(Strategy):
    def execute(self, data: list):
        return sorted(data, reverse=True)


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data: list):
        return self._strategy.execute(data)


data = [1, 3, 2, 4, 5]
context = Context(StrategyA())
print("Strategy A:", context.execute_strategy(data))

context.set_strategy(StrategyB())
print("Strategy B:", context.execute_strategy(data))
