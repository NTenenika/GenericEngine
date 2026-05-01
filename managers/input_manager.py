# input_manager.py

from pygame import event as event
from pygame import key as key

class Input:
  def __init__(self, input_, name, flag = False):
    self.flag : bool = flag
    self.input = input_
    self.name : str = name
  def pressed(self):
    self.flag = True
  def unpressed(self):
    self.flag = False
  def print(self):
    print(self.name)
# to add an input you do this:
# jump = Input(pg.K_SPACE, "Jump")
# kINPUTS = [jump]

class InputManager:
  def __init__(self, inputs):
    self.inputs = []
    if isinstance(inputs, list):
      self.inputs = inputs
    elif isinstance(inputs, dict):
      for name, val in inputs.items():
        new_input = Input(val, name)
        self.inputs.append(new_input)
        new_input.print()
  def update(self):
    event.get_keyboard_grab()
    keys_held = key.get_pressed()
    for i in self.inputs:
      if keys_held[i.input]:
        i.pressed()
      else:
        i.unpressed()