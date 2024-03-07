Conway's Game of Life
--------------------

My attempt at Conway's game of life using the turtle + tkinter module that ships with python.

The rules are:
- Any cell with <2 neighbours dies (turns black)
- Any cell with 2 or 3 neighbours lives (turns white)
- Any cell with >3 neighbours dies (turns black)
- Any cell with 3 neighbours comes alive (turns white)

This version of the game is very slow and a 20 x 20 grid is all my box can manage. This is because I'm being lazy and can't
be bothered to impliment a bunch of rules to dictate how objects should spawn in and when they should be deleted meaning it runs very poorly.

Currently this program creates all the possible cells on launch and then just edits their colour based upon the status of its neighbours. 
This means we have a bunch of calculation for what should be dormant objects happening on every iteration of the main loop the logic is
contained within. 

That aside it's pretty fun to see how these 4 simple rules and 2 cell states can generate objects that move and reporoduce. 
