# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import collections
import re


def find_gcd(x, y):
    while y:
        x, y = y, x % y

    return x


def is_vowel(ch):
    return ch in ['a', 'e', 'i', 'o', 'u']


def count_vowels(string):
    count = 0
    for i in range(len(string)):

        # Check for vowel
        if is_vowel(string[i]):
            count += 1
    return count


def go_snake(matrix, i, j, m, n):
    if i >= m or j >= n:
        return
    for p in range(i, n):
        print(matrix[i][p], end='')
    for p in range(i + 1, m):
        print(matrix[p][n - 1], end='')
    if (m - 1) != i:
        for p in range(n - 2, j - 1, -1):
            print(matrix[m - 1][p], end='')
    if (n - 1) != j:
        for p in range(m - 2, i, -1):
            print(matrix[p][j], end='')
    go_snake(matrix, i + 1, j + 1, m - 1, n - 1)


def is_palindrome(number):
    j = len(number) - 1
    for i in range(0, int(j/2)):
        if number[i] != number[j]:
            return False
        j = j - 1

    return True


def one():
    print("Give me numbers for gcd")
    numbers = list(map(int, input("Enter a multiple value: ").split()))
    num1 = numbers[0]
    num2 = numbers[1]
    gcd = find_gcd(num1, num2);
    for i in range(2, len(numbers)):
        gcd = find_gcd(gcd, numbers[2])

    print("GCD : ")
    print(gcd)


def two():
    print("Give me a string")
    string = str(input()).lower()
    print("Your string has " + str(count_vowels(string)) + " vowels ")


def three():
    print("Give me 2 strings with enter between")
    string1 = str(input())
    string2 = str(input())
    print(string2.count(string1))


def four():
    print("Give me string written int UpperCamelCase and I will turn it into lowercase_with_underscores")
    string = str(input())
    print(re.sub(r'(?<!^)(?=[A-Z])', '_', string).lower())


def five():
    matrix = [['A', 'B', 'C'],
              ['H', 'I', 'D'],
              ['G', 'F', 'E']]

    go_snake(matrix, 0, 0, 3, 3)
    print()


def six():
    print("Give me a number to test if is a palindrome : ")
    number = str(input())
    print(is_palindrome(number))


def seven():
    print("Give me a string to extract the first number")
    string = str(input()).lower()
    string = re.sub('[a-z]', '_', string)
    number = 0
    for i in range(0,len(string)):
        if string[i] == '_':
            break
        number = number*10 + int(string[i])
    print(number)


def eight():
    print("Give me a number")
    number = str("{0:b}".format(int(input())))
    print(number)
    count = len([ones for ones in number if ones == '1'])
    print("Your number has " + str(count) + " of ones in his binary representation")


def nine():
    print("Give me a string")
    string = input().lower()
    d = collections.defaultdict(int)
    for c in string:
        d[c] += 1
    print(sorted(d.items(), key=lambda x: x[1], reverse=True)[0])


def ten():
    print("Give me a string")
    string = input()
    d = collections.defaultdict(int)
    for c in string:
        d[c] += 1
    print(d[' '] + 1)


def menu(argument):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        5: five,
        6: six,
        7: seven,
        8: eight,
        9: nine,
        10: ten,
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument)
    # Execute the function
    func()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("What you want me to do ? (1-11) :")
    input1 = int(input())
    while 1 <= input1 <= 10:
        menu(input1)
        print("What you want me to do ? (1-11) :")
        input1 = int(input())
