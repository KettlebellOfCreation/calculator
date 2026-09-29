import re



def parser(s: str):
    if not isinstance(s, str):
        s = str(s)

    s = s.strip().replace(",", ".")

    m = re.fullmatch(
        r"(-?\d+(?:\.\d+)?)\s*([+\-*/])\s*(-?\d+(?:\.\d+)?)",
        s,
    )
    if not m:
        raise ValueError(f"Неверный формат: {s!r}")

    a: float = float(m.group(1))
    op = m.group(2)
    b: float = float(m.group(3))

    if op == "+":
        return calc_sum(a, b)
    if op == "-":
        return difference(a, b)
    if op == "*":
        return product(a, b)
    if b == 0:
        raise ZeroDivisionError("Деление на ноль")
    return a / b


def product(a: float, b: float):
    return a * b

def division(a: float, b: float):
    if b == 0:
        print("Error: Division by Zero")
    else:
        return a / b

def calc_sum(a: float, b: float):
    return a + b

def difference(a: float, b: float):
    return a - b


parser("10 - 1")
