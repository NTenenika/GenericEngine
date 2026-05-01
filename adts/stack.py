# stack.py
class Stack:
  def __init__(self):
    self.array = []
    self.size : int = 0
  def push(self, n):
    self.array.append(n)
    self.size += 1
  # returns popped value
  def pop(self):
    popped = self.array.pop(-1)
    self.size -= 1
    return popped
  def peek(self):
    return self.array[-1]
  def index(self, i):
      return self.array[i]
  def elements(self):
      return self.array
  def clear(self):
    self.array.clear()
    self.size = 0
  def is_empty(self):
    if self.size == 0:
      return True
    else:
      return False
  def print(self):
    for n in self.array:
      print(n)
  def get_size(self):
    return self.size