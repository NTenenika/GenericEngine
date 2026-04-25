# asset_manager.py

kPEAK = 20
import pygame.image as pg
class Asset:
  def __init__(self, filename, name : str):
    self.filename = filename # filename is an image
    self.name : str = name

class AssetManager:
  def __init__(self, assets : list = None):
    self.assets : dict = {}
    if assets != None:
      for asset in assets:
        self.assets[asset.name] = asset
  def get_asset(self, name : str):
    if name in self.assets:
      return self.assets[name]

    filename = pg.load("sprites/" + name + ".png").convert_alpha()
    self.assets[name] = Asset(filename, name)

    return self.assets[name]