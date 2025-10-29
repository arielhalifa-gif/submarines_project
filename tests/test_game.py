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