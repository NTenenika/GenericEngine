# game.py

from constants import *
from adts.stack import Stack
from asyncio import sleep


class Game:
  def __init__(self):
    self.states = Stack()
    self.window = pg.display.set_mode(kSCREEN_SIZE)
    pg.display.set_caption(kGAME_NAME)
  def get_window(self):
    return self.window

  def enter_state(self, state):
    self.push_state(state)

  def push_state(self, state):
    self.states.push(state)
    state.enter_state()

  def pop_state(self):
    if self.states:
      self.states.peek().exit_state()
      self.states.pop()

  def update(self, dt, events):
    self.states.peek().update(dt, events)

  def draw(self, surface):
    if not self.states.is_empty():
      self.states.peek().draw(surface)
# these next functions
# depend on if you're making it playable in the web or not
  async def run_web(self):
    pg.init()
    run = True
    clock = pg.time.Clock()

    while run:
      dt = clock.tick(kFPS) / 1000.0
      events = pg.event.get()

      for event in events:
        if event.type == pg.QUIT:
          run = False

      pg.display.flip()
      await sleep(0)
  def run(self):
    # capacity = 1
    # filename = "sprites/sprite.png"
    # char = [Asset("char", filename, capacity)]
    # am = AssetManager(list(char), capacity)
    run = True
    clock = pg.time.Clock()
    while run:
      dt = clock.tick(kFPS) / 1000.0
      events = pg.event.get()
      for event in events:
        if event.type == pg.QUIT:
          run = False

      # am.sprites.update()
      # self.window.fill(pg.Color("white"))
      # am.sprites.draw(self.window)
      pg.display.flip()
      clock.tick(kFPS)
    pg.quit()