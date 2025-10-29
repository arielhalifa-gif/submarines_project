import board as b, game as g
def parse_coords(raw: str, *, one_based: bool = True) -> tuple[int, int] | None:
    # פנקציה שמקבלת סטרינג וממירה לשני מספרים שלמים
    coords = raw.split()
    return int(coords[0]), int(coords[1])


def print_status(state: dict) -> None:
    # מדפיס לוח ציבורי (render_public) + יריות שנותרו + צוללות שנותרו.
    print(b.render_public(state["ships"], state["shots"]))
    print(g.shots_left(state))
    print(b.count_remaining_ships(state["ships"], state["shots"]))


def print_end(state: dict, won: bool) -> None:
    if won:
        print(f"congrats you have won")
    else:
        print(f"you lose \n dont worry you will get it next time")
    print(b.render_reveal(state["ships"], state["shots"]))
