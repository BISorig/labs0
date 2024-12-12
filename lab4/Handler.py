from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, next_handler=None):
        self._next_handler = next_handler

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            return f"Handled by ConcreteHandlerA"
        else:
            return super().handle(request)


class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            return f"Handled by ConcreteHandlerB"
        else:
            return super().handle(request)


handler_chain = ConcreteHandlerA(ConcreteHandlerB())
result = handler_chain.handle("B")
print(result)
