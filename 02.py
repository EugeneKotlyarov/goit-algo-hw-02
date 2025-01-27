from collections import deque


def is_palindrome(input_string):
    # ТЗ: бути нечутливою до регістру та пробілів
    char_deque = deque("".join(input_string.lower().split()))

    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


# Test


def main():
    test_strings = [
        "кит на морі романтик",
        "nureses nur",
    ]

    for test in test_strings:
        print(f"'{test}' is a palindrome: {is_palindrome(test)}")


if __name__ == "__main__":
    main()
