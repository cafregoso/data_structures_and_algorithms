import random

# Your previous Plain Text content is preserved below:

# Pad for Carlos Alvarez - Software Engineer, API


def robot_walk(x: int, y: int) -> list[list]:
    """Return a grid with valid moves for the robot"""

    random_size = random.randint(1, 100)
    answer = []
    valid_moves = [(0, 1), (1, 0), (0, -1), (-1, 0),
                   (1, 1), (-1, -1), (-1, 1), (1, -1)]

    matrix = [['' for _ in range(5)] for _ in range(5)]
    robot_start = [x, y]

    for row in matrix:
        print(row)
    print(robot_start)
    for step in valid_moves:
        if robot_start[0] + step[0] < random_size and robot_start[1] + step[1] < random_size:
            matrix[robot_start[0] + step[0]][robot_start[1] + step[1]] = "E"
        answer.append([robot_start[0] + step[0],
                        robot_start[1] + step[1]])
    # return answer

if __name__ == "__main__":
    print(robot_walk(3, 3))