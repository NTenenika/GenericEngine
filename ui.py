# ui.py

from constants import *

class UI:
  def __init__(self):
    self.elements = [] # This will hold all UI elements
  def add_element(self, element):
    self.elements.append(element)
  def update(self):
    for element in self.elements:
      element.update()
  def draw(self, surface):
    for element in self.elements:
      element.draw(surface)

# Abstract Class for UI Elements
class UIElement:
  def draw(self, surface):
    pass
  def update(self):
    pass