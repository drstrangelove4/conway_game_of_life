John Conway's Game of Life
--------------------

My attempt at Conway's game of life using the turtle + tkinter module that ships with python.
https://en.wikipedia.org/wiki/Conway's_Game_of_Life

The rules are:
- Any cell with <2 neighbours dies (turns black)
- Any cell with 2 or 3 neighbours lives (stays white)
- Any cell with >3 neighbours dies (turns black)
- Any cell with 3 neighbours comes alive (turns white)

Currently this program creates all the possible cells on launch, calculates the neighbours for each cell and then just edits their colour based upon the status of its neighbours. 
This means we have a bunch of logic for what should be dormant objects happening on every iteration of the main loop the logic is contained within.
