def fancy_prnt(n):
    def replace(m):
        if not isinstance(m, int) or m <= 0:
            raise ValueError("Invalid input, Please enter a positive integer.")
        for num in range(m):
            if num % n == 0:
                print("Buzz!")
            else:
                print(num)
    return replace

try:
    n = int(input("Enter n: "))
    range_end = int(input("Enter the the range (input-1): "))
    replace = fancy_prnt(n)
    replace(range_end)
except ValueError as error:
    print(error)