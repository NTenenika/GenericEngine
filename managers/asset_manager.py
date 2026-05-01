# asset_manager.py
from collections import OrderedDict as odict

# this is for performance reasons
# you can make this as big or small as you need
kCAPACITY : int = 20
kWIDTH : int = 16
kHEIGHT : int = 16

from pygame import image as pg
from pygame import sprite as sp
from pygame import draw as draw
from pygame import Rect as Rect

class Asset(sp.Sprite):
  def __init__(self, name : str, filename : str, width : int = kWIDTH, height : int = kHEIGHT, x : int = 0, y : int = 0, color = (0, 0, 0)):
    sp.Sprite.__init__(self)
    self.name : str = name # just to find the asset in dictionaries
    self.image = pg.load(filename).convert_alpha()
    draw.rect(self.image, color, Rect(x, y, width, height)) # color doesn't matter
    self.rect = self.image.get_rect()

class AssetManager:
  def __init__(self, assets : list = None, capacity : int = kCAPACITY):
    self.assets : odict = odict()
    self.capacity : int = capacity
    self.sprites = sp.Group()
    if assets != None:
      for asset in assets:
        self.assets[asset.name] = asset
        self.sprites.add(asset)

  def get_asset(self, name : str):
    if name in self.assets:
      return self.assets[name]

    filename = "sprites/" + name + ".png"
    self.assets[name] = Asset(name, filename)
    self.assets.move_to_end(name)
    if len(self.assets) > self.capacity:
      self.sprites.remove(self.assets[-1])
      self.assets.popitem(last = False)

    return self.assets[name]