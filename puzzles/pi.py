def pi(n):
    k = 0
    sign = 1
    deno = 1
    for _ in range(n):
        k += sign * 4 / deno
        sign *= -1
        deno += 2
    return k

print(pi(1000000))
