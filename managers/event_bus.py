# event_bus.py

kEVENTS = {
  # "name" : func()
}

class EventBus:
  def __init__(self):
    self.events = {}

  def listen(self, event : str, callback):
    if event not in self.events:
      self.events[event] = []
    self.events[event].append(callback)

  def unlisten(self, event : str, callback):
    if event in self.events and callback in self.events[event]:
      self.events[event].remove(callback)

  def broadcast(self, event : str, *args, **kwargs):
    if event in self.events:
      for callback in self.events[event]:
        callback(*args, **kwargs)

  def clear(self):
    self.events = {}