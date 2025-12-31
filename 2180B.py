# https://codeforces.com/problemset/problem/2180/B

def solve():
    no_str = int(input())
    str_input = list(input().split())
    ans = ""

    for it in str_input:
        if not ans:
            ans = it
        else:
            front = it + ans
            back = ans + it

            ans = min(front, back)

    print(ans)


def main():
    # with open("input.txt", "r") as f:
    #     data = f.read().split()
    #
    # it = iter(data)
    #
    # try:
    #     test_cases = int(next(it))
    # except StopIteration:
    #     return # no input

    test_cases = int(input())

    for _ in range(test_cases):
        solve()


main()