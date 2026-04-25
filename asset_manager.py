# asset_manager.py
from collections import OrderedDict as odict

kCAPACITY : int = 20

import pygame.image as pg
class Asset:
  def __init__(self, filename, name : str):
    self.filename = filename # filename is an image
    self.name : str = name

class AssetManager:
  def __init__(self, assets : list = None, capacity : int = kCAPACITY):
    self.assets : odict = odict()
    self.capacity : int = capacity
    if assets != None:
      for asset in assets:
        self.assets[asset.name] = asset
  def get_asset(self, name : str):
    if name in self.assets:
      return self.assets[name]

    filename = pg.load("sprites/" + name + ".png").convert_alpha()
    self.assets[name] = Asset(filename, name)
    self.assets.move_to_end(name)
    if len(self.assets) > self.capacity:
      self.assets.popitem(last = False)

    return self.assets[name]