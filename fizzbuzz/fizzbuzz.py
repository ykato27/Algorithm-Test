"""
FizzBuzz
1から整数を数える
3で割り切れる = Fizz
5で割り切れる = Buzz
3でも5でも割り切れる = FizzBuzz
"""


def fizzbuzz_1(n: int):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")


def fizzbuzz_2(n: int):
    i = 1
    while i <= n:
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
        i += 1


if __name__ == "__main__":
    fizzbuzz_1(30)
    fizzbuzz_2(30)
