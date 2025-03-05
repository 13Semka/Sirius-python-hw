from typing import Any

# не уверен, такой реализации вы ожидали, просто как будто бы тут переменная сайз бесполезная, т.к. в питоне 
# можно не задавать размер списка, если бы можно было указать размер, то тогда он был бы 2 * size,
# ну исходя из того, что мы возьмем середину списка и начнем добавлять оттуда, и если мы, к примеру, будет добавлять
# только справа элементы, при n = size добавлениях у нас все будет норм

class Queue:
    def __init__(self, size: int) -> None:
        self.size = size
        self._storage = []
    
    def append_right(self, x) -> bool: # o(1)
        try:
            self._storage.append(x)
            return True
        except:
            return False
        
    def append_left(self, x) -> bool: # o(1)    тут будет только o(n)...
        try:
            self._storage.insert(0, x)
            return True
        except:
            return False
    
    def delete_right(self) -> bool: # o(1)
        try:
            del self._storage[-1]
            return True
        except:
            return False

    def delete_left(self) -> bool: # o(1)
        try:
            del self._storage[0]
            return True
        except:
            return False

    def get_right(self) -> int: # o(1)
        try:
            return self._storage[-1]
        except:
            return -1
    
    def get_left(self) -> int: # o(1)
        try:
            return self._storage[0]
        except:
            return -1

    def is_empty(self) -> bool: # o(1)
        return len(self._storage) == 0

    def is_full(self) -> bool: # o(1)
        return len(self._storage) == self.size
    
