import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_maze(maze):
    clear_screen()
    for row in maze:
        print("".join(row))

def move_user(maze, user_position, direction):
    x, y = user_position

    if direction == "UP" and maze[x-1][y] == ".":
        maze[x][y] = "."
        x -= 1
    elif direction == "DOWN" and maze[x+1][y] == ".":
        maze[x][y] = "."
        x += 1
    elif direction == "LEFT" and maze[x][y-1] == ".":
        maze[x][y] = "."
        y -= 1
    elif direction == "RIGHT" and maze[x][y+1] == ".":
        maze[x][y] = "."
        y += 1

    user_position = (x, y)
    maze[x][y] = "U"

    return user_position

def main():
    username = input("Ingrese su nombre de usuario: ")
    maze = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", "#", "#", "#", "#", ".", "#", "#"],
        ["#", ".", ".", ".", "#", ".", ".", "#", "#"],
        ["#", ".", "#", ".", "#", ".", "#", "#", "#"],
        ["#", ".", "#", ".", ".", ".", ".", ".", "."],
        ["#", "#", "#", "#", "#", "#", "#", "#", "."],
        ["#", "#", "#", "#", "#", "#", ".", ".", "."]
    ]

    user_position = (1, 1)
    maze[user_position[0]][user_position[1]] = "U"

    while True:
        print_maze(maze)
        print(f"Bienvenido, {username}! Use las flechas para moverse (Q para salir): ")

        direction = input()
        if direction.upper() == "Q":
            break

        user_position = move_user(maze, user_position, direction.upper())

if __name__ == "__main__":
    main()
