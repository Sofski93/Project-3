from random import randint

# Define the Battleship class
class Battleship:
    def __init__(self):
        """
        Choose grid size and initialize the grids
        Determine the ships sizes based on the grid size
        """
        while True:
            try:
                self.grid_size = int(input(
                    green + " Choose grid size 6 or 10: "
                ))
                if self.grid_size not in [6, 10]:
                    raise ValueError
                break
            except ValueError:
                print(
                    red + " Invalid grid size.\
 Please choose 6 or 10." + end_color
                )
        self.player_grid = [
            ["~"] * self.grid_size for _ in range(self.grid_size)
        ]
        self.computer_grid = [
            ["~"] * self.grid_size for _ in range(self.grid_size)
        ]
        self.player_ships_positions = set()
        self.computer_ships_positions = set()
        self.player_attempts = set()
        self.computer_attempts = set()
        if self.grid_size == 10:
            self.ships_sizes = [1, 2, 3, 4, 5]
        else:
            self.ships_sizes = [1, 2, 3]

    def print_grids(self):
        """
        Print the player's grid and the computer's grid
        """
        print("Player's Grid:")
        self.print_grid(self.player_grid)
        print("Computer's Grid:")
        self.print_grid(self.computer_grid, hide_ships=True)

    def print_grid(self, grid, hide_ships=False):
        """
        Print the grid with column numbers
        Print the grid with row Letters
        """
        print(
            green + "   " + "  ".join(str(i) for i in range(self.grid_size)) +
            end_color
        )
        for i, row in enumerate(grid):
            print(green + chr(65 + i) + end_color + "  " + "  ".join(
                blue + "~" + end_color if cell ==
                "~" or (cell == "⛴" and hide_ships) else
                cell for cell in row))
        print()

    def place_ships(self, grid, ship_positions):
        """
        Place ships on the grid randomly horizontally or vertically
        """
        for size in self.ships_sizes:
            while True:
                orientation = random.choice(["horizontal", "vertical"])
                if orientation == "horizontal":
                    row = random.randint(0, self.grid_size - 1)
                    col = random.randint(0, self.grid_size - size)
                    if all(grid[row][col + i] == "~" for i in range(size)):
                        for i in range(size):
                            grid[row][col + i] = "⛴"
                            ship_positions.add((row, col + i))
                        break
                else:
                    row = random.randint(0, self.grid_size - size)
                    col = random.randint(0, self.grid_size - 1)
                    if all(grid[row + i][col] == "~" for i in range(size)):
                        for i in range(size):
                            grid[row + i][col] = "⛴"
                            ship_positions.add((row + i, col))
                        break

    def player_guess(self):
        """
        Allow the player to make a move
        check if the move is valid
        """
        while True:
            try:
                row, col = input(
                    "Enter your guess Row  and Column (e.g. A5): "
                ).upper()
                row = ord(row) - 65
                col = int(col)
                if (row, col) in self.player_attempts:
                    print(
                        red + "You have alredy tried this spot! Try again." +
                        end_color
                    )
                elif (
                    row < 0 or row >= self.grid_size or col < 0 or col >=
                    self.grid_size
                ):
                    print(
                        red + "Invalid guess you off-grid! Try again." +
                        end_color
                    )
                else:
                    self.player_attempts.add((row, col))
                    if (row, col) in self.computer_ships_positions:
                        print(red + "Hit!" + end_color)
                        self.computer_grid[row][col] = "#"
                        self.computer_ships_positions.remove((row, col))
                    else:
                        print(yellow + "Miss!" + end_color)
                        self.computer_grid[row][col] = "x"
                    break
            except ValueError:
                print(
                    red + "Invalid input!\
                          Enter row letter and column number." +
                    end_color
                    )

    def computer_guess(self):
        """
        Computer makes a random move
        desplay hit or miss message
        """
        row = random.randint(0, self.grid_size - 1)
        col = random.randint(0, self.grid_size - 1)
        while (row, col) in self.computer_attempts:
            row = random.randint(0, self.grid_size - 1)
            col = random.randint(0, self.grid_size - 1)
        self.computer_attempts.add((row, col))
        if (row, col) in self.player_ships_positions:
            print(
                red + f"Computer hit your ship at ({chr(65 + row)}, {col})!" +
                end_color
            )
            self.player_grid[row][col] = "#"
            self.player_ships_positions.remove((row, col))
        else:
            print(
                yellow +
                f"Computer missed at ({chr(65 + row)}, {col})!" +
                end_color
            )
            self.player_grid[row][col] = "x"

    def play(self):
        """
        enter player name
        display welcome message
        display rules of the game
        ask player to accept the mission
        place ships for player and computer
        loop through the game until one player wins
        Print outcome of the game
        """
        print()
        self.player_name = input(green + " Please enter your name: ")

        print()
        welcome_message = f" Welcome to Battleship Captain\
 {self.player_name}!\n----------------------\n"
        for char in welcome_message:
            print(green + char, end='', flush=True)
            time.sleep(0.05)
        rules = """ Rules of Engagement:
 You will be playing against the computer.
 Each of you will have a grid with ships.
 The goal is to sink all of the opponent's ships by
 guessing their positions on the grid.
 If you hit a ship, it will be marked with #.
 If you miss, it will be marked with x.
 The battle continues until all ships of one player are sunk.
 -------------------------------
 """
        for char in rules:
            print(char, end='', flush=True)
            time.sleep(0.05)
        promt = "Do you accept the mission?\
 Press 'S' to accept or any key to decline: "
        for char in promt:
            print(green + char + end_color, end='', flush=True)
            time.sleep(0.05)
        accept_mission = input()
        if accept_mission.lower() != 'y':
            print("Mission declined. Exiting the game." + end_color)
            return
        self.place_ships(self.player_grid, self.player_ships_positions)
        self.place_ships(self.computer_grid, self.computer_ships_positions)
        turns = 0
        while self.player_ships_positions and self.computer_ships_positions:
            self.print_grids()
            self.player_guess()
            self.computer_guess()
            if not self.computer_ships_positions:
                break
            turns += 1
        if self.player_ships_positions:
            print("Congratulations {self.player_name}!
            )
        else:
            print(" You lost the game " )


# Run the game
game = Battleship()
game.play()
