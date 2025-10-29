import random
def place_random_ships(ships: list[list[int]], n: int) -> None:
    while n > 0:
        index_i = random.randint(0, len(ships))
        index_j = random.randint(0, len(ships))
        if ships[index_i][index_j] == 0:
            ships[index_i][index_j] = 1
            n -= 1