import sys

def solve():
    no_days, hike_days = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))

    counter = 0
    ans = 0
    rest_day = False

    for raining_day in nums:
        # raining_day = int(next(it))

        # it rains or it's restday
        if raining_day or rest_day:
            rest_day = False
            counter = 0
            continue

        counter += 1
        if counter == hike_days:
            counter = 0
            rest_day = True
            ans += 1

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
    #     return  # no input

    test_cases = int(sys.stdin.readline())

    for _ in range(test_cases):
        solve()

main()
