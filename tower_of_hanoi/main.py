# Tower of Hanoi


def hanoi(n, src, dest, support):
    if n < 1:
        return

    hanoi(n - 1, src, support, dest)
    print(src + "->" + dest)
    hanoi(n - 1, support, dest, src)


def get_hanoi_movement(n, src, dest, support):
    result = []

    def _hanoi(n, src, dest, support):
        if n < 1:
            return

        _hanoi(n - 1, src, support, dest)
        result.append((n, src, dest))
        _hanoi(n - 1, support, dest, src)

    _hanoi(n, src, dest, support)
    return result


if __name__ == "__main__":
    hanoi(3, "a", "b", "c")
    for r in get_hanoi_movement(3, "a", "b", "c"):
        print(r)
