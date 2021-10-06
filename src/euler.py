def problem1():
    print(sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0]))


def problem2():
    fibs = [0, 1]
    previous_value = 0
    current_value = 1
    while current_value <= 4000000:
        new_value = previous_value + current_value
        previous_value = current_value
        current_value = new_value
        fibs.append(new_value)
    return sum([x for x in fibs if x % 2 == 0])


if __name__ == "__main__":
    print(problem2())
