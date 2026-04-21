# main.py
from constants import *
from asyncio import run
from states import Game, StartState

pg.init()
engine = Game()

initial_state = StartState(engine)
engine.enter_state(initial_state)

# # Web version
# async def main():
#   await engine.run_web()
#
# run(main())

# # App version (ig)
# def main():
#   engine.run()
# if __name__ == '__main__':
#   main()