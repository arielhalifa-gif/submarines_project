import board as b, random
def init_game(size: int, n_ships: int, max_shots: int, *, rng: random.Random | None = None) -> dict:
    # מקבל את הגודל הרצוי של הלוח מספר ספינות מקסימום יריות
    # מחזיר מילון עם כל הפריטים הניצרכים למשחק
    # אחרי הכוכבית זה אומר שלא חובה לקבל את הפרמטרים האלה
    ships_ = b.create_matrix(size)
    shoots_ = b.create_bool_matrix(size)
    return {"size": size,
            "ships": ships_, #int
            "shots": shoots_, #bool
            "n_ships": n_ships,
            "max_shots": max_shots,
            "shots_used": 0}



def validate_shooting(state: dict, x: int, y: int) -> bool:
    if b.in_bounds(state["size"], x, y):
        if state["shots"][x][y] == False:
            return True
    return False


def shoot(state: dict, x: int, y: int) -> tuple[bool, str]:
    if validate_shooting(state, x, y):
        if state["ships"][x][y] == 1:
            state["shots_used"] += 1
            state["shots"][x][y] = True
            return True, "is hit"
        