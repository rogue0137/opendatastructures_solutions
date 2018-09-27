import sys
import pandas # add to readme

job = (sys.argv[1])


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])


exercise_one = Stack()
exercise_one.push(1)
exercise_one.push(2)
exercise_one.push(3)
print(exercise_one)

