# timer.py
from pygame import time as time
from pygame import event as event

kTIMER_EVENT = event.custom_type()
class Timer:
  def __init__(self, timer = 0):
    self.timer = timer
  def delta_time(self, dt):
    self.timer += dt
    return self.timer # optionally: , FONT.render(f"{' ' * 3}{self.timer:.2f}", True, "white")
  def tick_time(self, start):
    self.timer = (time.get_ticks() - start) * 0.001
    return self.timer # optionally: , FONT.render(f"{' ' * 4}{self.timer:.2f}", True, "white")
