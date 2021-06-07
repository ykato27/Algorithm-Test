"""文字列を逆順で出力する問題.

Input
'python'

Output
'nohtyp'
"""


def reverse_integer(word: str) -> str:
    string = str(word)

    if len(string) == 0:
        raise ValueError("適切な文字を入力してください")
    else:
        return str(string[::-1])


if __name__ == "__main__":
    print(reverse_integer("python"))
    print(reverse_integer("123"))
