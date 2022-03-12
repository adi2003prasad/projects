# TODO: Complete the get_ruler function
def get_ruler(kingdom):
    ruler = ''
    vowels = ['a', 'e', 'i', 'o', 'u']

    rulers = ['Alice', 'Bob', 'nobody']
    a = kingdom[-1]
    if (a == 'y'):
        ruler += rulers[2]
    elif(a.lower in vowels):
        ruler += rulers[0]
    else:
        ruler += rulers[1]

    # TODO: Add logic to determine the ruler of the kingdom
    # It should be either 'Alice', 'Bob' or 'nobody'.
    return ruler


def main():
    # Get the number of test cases
    ans = []
    T = int(input())
    for t in range(T):
        # Get the kingdom
        kingdom = input()
        ans.append([kingdom, get_ruler(kingdom)])

    for x in range(len(ans)):
        print('Case #%d: %s is ruled by %s.' %
              (x + 1, ans[x][0], ans[x][1]))


if __name__ == '__main__':
    main()
