def shortest_palindrome(s):
    prefix = 0
    suffix = 0

    base = 29
    last_index = 0
    power = 1
    mod = 10 ** 9 + 7

    for index, char in enumerate(s):
        char = (ord(char) + ord('a') + 1)

        prefix = (prefix * base) % mod
        prefix = (prefix + char) % mod
        suffix = (suffix + char * power) % mod
        power = (power * base) % mod

        if prefix == suffix:
            last_index = index
        
    suffix = s[last_index + 1:]
    return suffix[::-1]+s

S = str(input())
print(shortest_palindrome(S))

