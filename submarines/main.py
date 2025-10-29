import game as g, io1
# פונקציה ראשית
# מאתחלים את המשחק
# לולאה עד שהמשחק נגמר

def play(size: int = 6, n_ships: int = 6, max_shots: int = 10, *, one_based: bool = True) -> None:
    state_main = g.init_game(size, n_ships, max_shots)
    game_over = False
    while not game_over:
        print("please enter your game")
        str_coord = input()
        tpl_coords_int =io1.parse_coords(str_coord)
        