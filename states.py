# states.py
from game import *

class States:
  def __init__(self, game):
    self.game = game
  def update(self, dt, events):
    pass
  def draw(self, surface):
    pass
  def enter_state(self):
    pass
  def exit_state(self):
    pass

class StartState(States):
  def __init__(self, game):
    States.__init__(self, game)
    # basically what goes in here are any
    # start state specific variables are needed
    # like a menu or fonts or anything

  def update(self, dt, events):
    # for events in events:
    #   # any conditions
    #   self.game.pop_state()
    # # the only reason pop would be used is if you won't
    # # get back to this state
    #   self.game.push_state(Generic_State(self.game, #data))
    pass
  def draw(self, surface):
    pass

# class Generic_State(States):
#   def __init__(self, game):
#     States.__init__(self, game)
#     # state specific variables
#     # you can also draw stuff to the screen here