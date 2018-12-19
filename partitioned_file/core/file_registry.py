class FileRegistry(object):
    def __init__(self):
        self._items = list()

    @property
    def items(self):
        return self._items

    def add(self, item):
        return self.__add__(item)

    def __add__(self, item):
        if item not in self._items:
            self._items.append(item)

    def __iter__(self):
        for i in self.items:
            yield i
