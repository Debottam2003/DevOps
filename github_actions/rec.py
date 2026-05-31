# Using a loop
# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# Using recursion
def recFunc(i):
    if i < 1:
        return
    else:
        print(i)
        i -= 1
        recFunc(i)


# recFunc(100)
# 100 ... 1

# ButterFly pattern
# *         *
# * *     * *
# * * * * * *
# * *     * *
# *         *

fact = 1
for i in range(1, 6):
    fact *= i

print(fact)


def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


print(f"{5}!:{fact(5)}")
# 5 * 4 * 3 * 2 * 1

# 5 * fact(4)
# 5 * (4 * fact(3))
# 5 * (4 * (3 * fact(2)))
# 5 * (4 * (3 * (2 * fact(1))))
# 5 * (4 * (3 * (2 * 1)))
# 5 * (4 * (3 * 2))
# 5 * (4 * 6)
# 5 * 24
# 120

print(f"{-5}!:{fact(-5)}")
print("{}!:{}".format(6, fact(6)))
