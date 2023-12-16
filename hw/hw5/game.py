import maze

class Game():
    '''Holds the game solving logic. Initialize with a fully initialized maze'''

    def __init__(self, maze):
        self._maze = maze
        self.best_score = -1
        self.best_path = []

    # Creating simple methods (like the next two) to abstract core parts 
    #   of your algorithm helps increase the readability of your code.
    #   You will find these two useful in your solution.

    def _is_move_available(self, row, col, path):
        '''If (row, col) is already in the solved path then it is not available'''
        return (row, col) not in path

    def _is_puzzle_solved(self, row, col):
        '''Is the given row,col the finish square?'''
        return self._maze.get_finish() == (row, col)


    ########################################################
    # TODO - Main recursive method. Add your algorithm here.
    def find_route(self, currow=None, curcol=None, curscore=0, curpath=None):
        # initialize the starting coordinates and places the starting coordinates in the path
        if currow is None: currow = self._maze.get_start()[0]
        if curcol is None: curcol = self._maze.get_start()[1]
        if curpath is None: curpath = [self._maze.get_start()]

        # if the current move is invalid, returns -1 score and empty path
        if self._is_move_available(currow, curcol, curpath) == False: 
            return (-1, [])
        elif self._maze.is_move_in_maze(currow, curcol) == False: 
            return (-1, [])
        elif self._maze.is_wall(currow, curcol) == True: 
            return (-1, [])

        # if the current move is the finish, returns the score of the current path
        elif self._is_puzzle_solved(currow, curcol) == True: 
            return (int(curscore), curpath)

        # if the current move is valid and not the finish, updates the current score and repeats the algorithm for the 4 adjacent squares
        else:
            curscore += self._maze.make_move(currow, curcol, curpath)
            for i in [(currow, curcol-1), (currow-1, curcol), (currow, curcol+1), (currow+1, curcol)]:
                newpath = self.find_route(*i, curscore, curpath)
                if newpath[0] > self.best_score:
                    self.best_score = newpath[0]
                    self.best_path = curpath
        
        # after trying all possible routes, returns the highest score and the path that gives that score
        return (self.best_score, self.best_path+[self._maze.get_finish()])


# This block of code will be useful in debugging your algorithm. But you still need
#  to create unittests to thoroughly testing your code.
if __name__ == '__main__':
    # Here is how you create the maze. Pass the row,col size of the grid.
    grid = maze.Maze(3, 4)
    # You have TWO options for initializing the Value and Walls squares.
    # (1) init_random() and add_random_walls()
    #     * Useful when developing your algorithm without having to create 
    #         different grids
    #     * But not easy to use in testcases because you cannot preditably
    #         know what the winning score and path will be each run
    # (2) _set_maze()
    #     * You have to create the grid manually, but very useful in testing
    #       (Please see the test_game.py file for an example of _set_maze())
    grid.init_random(0,9) # Initialze to a random board
    grid.add_random_walls(0.2)   # Make a certian percentage of the maze contain walls

    # AFTER you have used one of the two above methods of initializing 
    #   the Values and Walls, you must set the Start Finish locations. 
    start = (0,2)
    finish = (1,1)
    grid.set_start_finish(start, finish)

    # Printing the starting grid for reference will help you in debugging.
    print(grid)           # Print the maze for visual starting reference

    # Now instatiate your Game algorithm class
    game = Game(grid)     # Pass in the fully initialize maze grid

    # Now initiate your recursize solution to solve the game!
    # Start from the start row, col... zero score and empty winning path
    score, path = game.find_route(start[0], start[1], 0, list())
    print(f"The winning score is {score} with a path of {path}")