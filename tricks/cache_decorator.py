from functools import lru_cache


@lru_cache(maxsize=5)   # 5 most recent values that have been called
# @cache    # only available version 3.9 and onward
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    for i in range(500):
        print(i, fib(i))
    print("done")


if __name__ == '__main__':
    main()