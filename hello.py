import sys


def lexicographic_rank(permutation: list[int]) -> int:
    """Return the zero-based lexicographic rank of a permutation."""
    n = len(permutation)
    rank = 0

    for position in range(n):
        smaller_unused = sum(
            value < permutation[position] for value in permutation[position + 1 :]
        )
        rank += smaller_unused * factorial_value(n - position - 1)

    return rank


def factorial_value(value: int) -> int:
    result = 1
    for factor in range(2, value + 1):
        result *= factor
    return result


def main() -> None:
    values = list(map(int, sys.stdin.buffer.read().split()))
    if not values:
        return

    n = values[0]
    p = values[1 : n + 1]
    q = values[n + 1 : 2 * n + 1]
    print(abs(lexicographic_rank(p) - lexicographic_rank(q)))


if __name__ == "__main__":
    main()