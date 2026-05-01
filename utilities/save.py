# save.py

from json import load, dumps

# for this honestly you can put whatever you want
# these were just some ideas
class ProgressTracker:
  def __init__(self, tracker = {}):
    if tracker != {}:
      self.tracker = tracker
    else:
      self.tracker = {
        "level": 0,
        "achievements": [],
        "items": [],
        # "mob keys" are so cool
        # basically you can give npcs, enemies, items, etc
        # keys that when you obtain, kill, talk, etc
        # they give you keys
        # what you do with those keys is really up to you
        # IE: you can make enemies not show up anymore,
        # npcs have unique dialogue,
        # items not show up in the pool,
        # etc
        "mob_keys": {},
        "player_pos": (0, 0),
        "health": 0,
        "score": 0,
        "checkpoints": {}
      }

  def convert_to_json(self, save_data_name = 0):
    with open(f"local_save{save_data_name}.json", mode="w", encoding="utf-8") as self.tracker:
      dumps(self.tracker)
  def convert_from_json(self, save_data_name = 0):
    with open(f"local_save{save_data_name}.json", mode="r", encoding="utf-8") as read_file:
      self.tracker = load(read_file)
  # in the parameters, pass in the variables used
  def update(self):
    # in here you just assign
    # the keys to whatever values is in the param list
    pass