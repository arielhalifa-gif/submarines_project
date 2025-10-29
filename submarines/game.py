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

# מקבלת קואורדינטות
# מוודאים שהירי תקין
# משנים את מצב היריות באחד
# כל מקרה אחר False
def shoot(state: dict, x: int, y: int) -> tuple[bool, str]:
    if validate_shooting(state, x, y):
        if state["ships"][x][y] == 1:
            state["shots_used"] += 1
            state["shots"][x][y] = True
            return True, "is hit"
        return False, "you mist" #תקין אבל לא פגע
    return False, "invalid please try again"


def is_won(state: dict) -> bool:
    # בודק אם כל הספינות נורו
    # אם הערך שחוזר מהפונקצייה של כמה ספינות נותרו שווה 0
    ships_left = b.count_remaining_ships(state["ships"], state["shots"])
    if ships_left == 0:
        return True
    return False



def is_lost(state: dict) -> bool:
    if state["shots_used"] >= state["max_shots"]:
        return True
    return False


def shots_left(state: dict) -> int:
    left = state["max_shots"] - state["shots_used"] #כמות היריות שנותרו
    return left
