def is_palindrome(s):
    s = list(s)
    midpoint = len(s) // 2
    for i in range(0, midpoint):
        print(f'Comparing {s[i]} and {s[-i-1]}')
        if s[i] != s[-i-1]:
            return False
    return True


def is_palindrome_recursive(s):
    s = list(s)
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome_recursive(s[1:-1])


if __name__ == "__main__":
    print(is_palindrome('tacocat'))
