def is_perfect_square(number):
    x = number // 2
    y = set ([x])
    while x*x != number:
        x = (x + (number // x)) //2
        if x in y:
            return False
        y.add(x)
    return True
print(is_perfect_square(9))
print(is_perfect_square(100))
print(is_perfect_square(225))
print(is_perfect_square(500))    