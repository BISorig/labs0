from abc import ABC, abstractmethod


class Target:
    def request(self):
        return "Target: Default behavior."


class Adaptee:
    def specific_request(self):
        return "Adaptee: Specific behavior."


class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self._adaptee = adaptee

    def request(self):
        return self._adaptee.specific_request()


adaptee = Adaptee()
adapter = Adapter(adaptee)
print(adapter.request())
