from dataclasses import dataclass
from typing import Hashable, Any


@dataclass
class Node:
    key: Hashable
    value: Any


class Dictionary:
    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.hash_table: list[Node | list | None] = [None] * self.capacity
        self.size = 0
        self.load_factor = 0.67

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        return str(self.hash_table)

    def calculate_index(self, key: Hashable) -> int:
        index = hash(key) % self.capacity
        while self.hash_table[index] and self.hash_table[index].key != key:
            index = (index + 1) % self.capacity
        return index

    def __setitem__(self, key: Hashable, value: Any) -> None:
        if self.size >= self.load_factor * self.capacity:
            self.resize()
        index = self.calculate_index(key)
        if self.hash_table[index] is None:
            self.size += 1
        self.hash_table[index] = Node(key, value)

    def __getitem__(self, key: Hashable) -> Any:
        index = self.calculate_index(key)
        if self.hash_table[index] is None:
            raise KeyError(key)
        return self.hash_table[index].value

    def resize(self) -> None:
        old_hash_table = self.hash_table
        self.__init__(self.capacity * 2)
        for node in old_hash_table:
            if node is not None:
                self.__setitem__(node.key, node.value)
