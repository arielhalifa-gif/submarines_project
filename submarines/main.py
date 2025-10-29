import game as g, io1, placement as p, board as b
# פונקציה ראשית
# מאתחלים את המשחק
# לולאה עד שהמשחק נגמר

def play(size: int = 6, n_ships: int = 6, max_shots: int = 10, *, one_based: bool = True) -> None:
    state_main = g.init_game(size, n_ships, max_shots)
    print(state_main)
    p.place_random_ships(state_main["ships"], n_ships)
    game_over = False
    while not game_over:
        print("please enter your game")
        str_coord = input()
        tpl_coords_int =io1.parse_coords(str_coord)
        while not g.validate_shooting(state_main, tpl_coords_int[0], tpl_coords_int[1]):
            print("please enter your game")
            str_coord = input()
            tpl_coords_int =io1.parse_coords(str_coord)
        tpl_shooting = g.shoot(state_main, tpl_coords_int[0], tpl_coords_int[1])
        if tpl_shooting[0]:
            print(tpl_shooting[1])
            if g.is_won(state_main):
                game_over = True
                won = True
                print("you win")
        else:
            if g.is_lost(state_main):
                game_over = True
                won = False
                print("you lose")
        io1.print_status(state_main)
    io1.print_end(state_main, won)


if __name__ == "__main__":
    play(8, 5, 15)