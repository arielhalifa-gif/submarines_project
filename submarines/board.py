def create_matrix(size: int, fill: int = 0) -> list[list[int]]:
#  יוצר מטריצה בגודל size ומאותחל בערך הניתן fill
    board = []
    for i in range(size):
        temp = []
        for j in range(size):
            temp.append(fill)
        board.append(temp)
    return board


def create_bool_matrix(size: int, fill: bool = False) -> list[list[bool]]:
    # מאתחל לוח נפרד שנשתמש בו כדי לאשר את הלוח הראשי 
    # מטריצה מאותחלת לבוליאני
    bool_board = create_matrix(size, fill)
    return bool_board



def in_bounds(size: int, x: int, y: int) -> bool:
    # בודק אם הקוארדינתות בתוך הגבול של הלוח
    if x >= 0 and y >= 0:
        if x <= size and y <= size:
            return True
    return False


def count_remaining_ships(ships: list[list[int]], shots: list[list[bool]]) -> int:
    # סופר לפי שני המטריצות כמה תאים נשארו לפגיעה
    # נעבור על כל הספינות כדי לבדוק כמה יש
    # צריך לבדוק רק איפה שיש ירייה האם יש פגיעה ואם כן אז נוריד מהסה"כ של כל הספינות
    count_total_ships = 0
    count_shots = 0
    for i in range(len(ships)):
        for j in range(len(ships[i])):
            if ships[i][j] == 1:
                count_total_ships += 1
                if shots[i][j] == True:
                    count_shots += 1
    return count_total_ships - count_shots


def render_public(ships: list[list[int]], shots: list[list[bool]]) -> str:
    # יוצר סטרינג שמסכם האם יש ספינה ואם כן האם ירו ואם כן האם יש פגיעה לפי זה ממלאים את המטריצה
    for i in range(len(ships)):
        temp_visual = ""
        for j in range(len(ships[i])):
            if shots[i][j] == True:
                if ships[i][j] == 1:
                    temp_visual += f"{"V":3}"
                else:
                    temp_visual += f"{"x":3}"
            else:
                temp_visual += f"{"0":3}"
        temp_visual += "\n"
    return temp_visual



def render_reveal(ships: list[list[int]], shots: list[list[bool]]) -> str:
    for i in range(len(ships)):
        temp_visual_end = ""
        for j in range(len(ships[i])):
            if shots[i][j] == True:
                if ships[i][j] == 1:
                    temp_visual_end += f"{"V":3}"
                else:
                    temp_visual_end += f"{"x":3}"
            else:
                if ships[i][j] == 1:
                    temp_visual_end += f"{"1":3}"
                else:
                    temp_visual_end += f"{"0"}"
        temp_visual_end += "\n"
    return temp_visual_end



