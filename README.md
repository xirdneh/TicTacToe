# TIC TAC TOE implementation with minimax alpha-beta optimization.
###TODO: 
* Implement tests.
* Debug mode:
  * Print branch that is searching.
  * Print alfa and beta values.
  * Make it human readable for learning purposes.
* Is the heuristic value calculation the best one?
* Sort tree?

##Usage:
run the `main.py` without any parameters to fire up the menu:

```bash
Select an option
1 - PC vs PC, 2 - PC vs Hooman: 
```
Select `1` if you want the program to play itself **It will always end up as a tie**.

Select `2` if you want to play the computer **Best you can do is to end up in a tie**.

###Computer VS Computer
After every move the player makes it will show the possible moves, the move selected and the board with the new move on it.

Press enter to see each new move until it ties with itself.

###Playing vs the computer
When playing the computer it will print a list of valid moves. In order to make a move type in the coordinates and press enter

```bash
>>> 2,1
```
After every move it will show the board changed.

**Every print of the board will stay in the screen for reference**

##Testing Scenarios:
There a .txt file called `test_baords.txt` which has a bunch of testing scenarios.

The few first ones are of an end state of the board.

The rest are on a non-end state of the board.

If the test board is a non-end state it will print the different possibilities of each player to win and then the total heuristic.
