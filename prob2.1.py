def abndnt(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()

    for i in range(len(divisors)):
        for j in range(i, len(divisors)):
            if divisors[i] * divisors[j] == n:
                print(divisors[i], "*", divisors[j])
    div_sum = sum(divisors) - n
    return div_sum > n

pos_num = int(input("Enter a positive integer: "))
abndnt_state = abndnt(pos_num)
print(abndnt_state)