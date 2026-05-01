# kinematics.py

# from constants import kGRAVITY, kCOEFFICIENT
from pygame import math as pg
# either gravity defined here or in constants
kGRAVITY = 9.8
kCOEFFICIENT = 0.8 # 0 < coeff < 1
# I'm defining it here just in case the game doesn't need it,
# and you can just delete this file
class Gravity:
  def __init__(self):
    self.force = pg.Vector2(0, kGRAVITY)
  def apply(self, velocity_obj, dt):
    velocity_obj.vector += self.force * dt

class Friction:
  def __init__(self):
    self.coefficient = kCOEFFICIENT
  def apply(self, velocity_obj):
    velocity_obj.vector.x += self.coefficient

class Velocity:
  def __init__(self, x = 0, y = 0):
    self.vector = pg.Vector2(x, y)
  def set_x(self, x):
    self.vector.x = x
  def set_y(self, y):
    self.vector.y = y
  def get_x(self):
    return self.vector.x
  def get_y(self):
    return self.vector.y
  def update(self, dt):
    displacement = self.vector * dt
    return displacement.x, displacement.y
  def add_impulse(self, x, y):
    self.vector.x += x
    self.vector.y += y
  def set_velocity(self, ax, ay, dt):
    self.vector.x *= ax * dt
    self.vector.y += ay * dt