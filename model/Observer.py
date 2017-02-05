class Observer(object):
    def __init__(self):
        self.listeners = set()

    
    def listen(self, func):
        self.listeners.add(func)


    def notify(self):
        for fun in self.listeners:
            fun()

