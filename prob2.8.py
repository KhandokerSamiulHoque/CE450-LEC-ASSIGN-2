def cyc(g1, g2, g3):
    def int_arg_func(n):
        def main_func(x):
            if n == 0:
                return x
            elif n == 1:
                return g1(x)
            elif n == 2:
                return g2(g1(x))
            elif n == 3:
                return g3(g2(g1(x)))
            else:
                result = x
                for _ in range(n // 3):
                    result = g1(result)
                    result = g2(result)
                    result = g3(result)
                if n % 3 == 1:
                    result = g1(result)
                elif n % 3 == 2:
                    result = g2(result)
                return result
        return main_func
    return int_arg_func


def add_one(x):
    return x + 1

def times_two(x):
    return x * 2

def add_three(x):
    return x + 3

my_cyc = cyc(add_one, times_two, add_three)

h = my_cyc(0)
print(h(5))

h = my_cyc(2)
print(h(1))

h = my_cyc(3)
print(h(2))

h = my_cyc(4)
print(h(2))

h = my_cyc(6)
print(h(1))