class FileRegistry(object):
    def __init__(self, items=[]):
        self._items = items

    @property
    def items(self):
        return self._items

    def add(self, item):
        return self.__add__(item)

    def __add__(self, item):
        self.items.append(item)

    def __iter__(self):
        for i in self.items:
            yield i
