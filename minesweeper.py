def play(dim_size=10, num_bombs=10):
    # Step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs)

    # Step 2: show the user the board and ask for where they want to dig
    # Step 3a: if location is a bomb, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least
    #          next to a bomb
    # Step 4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!
    safe = True 

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        # 0,0 or 0, 0 or 0,    0
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))  # '0, 3'
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location. Try again.")
            continue

        # if it's valid, we dig
        safe = board.dig(row, col)
        if not safe:
            # dug a bomb ahhhhhhh
            break # (game over rip)

    # 2 ways to end loop, lets check which one
    if safe:
        print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!")
    else:
        print("SORRY GAME OVER :(")
        # let's reveal the whole board!
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__': # good practice :)
    play()
