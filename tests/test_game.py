def returning():
    str = ""
    for i in range(5):
        for j in range(5):
            str += f"{"4":3}"
        str += "\n"
    return str
print(returning())


for i in range(5):
    for j in range(5):
        print(f"{"4":3}", end="")
    print()


def parse_coords(raw: str, *, one_based: bool = True) -> tuple[int, int] | None:
    # פנקציה שמקבלת סטרינג וממירה לשני מספרים שלמים
    coords = raw.split()
    return int(coords[0]), int(coords[1])

print(parse_coords("5 8"))