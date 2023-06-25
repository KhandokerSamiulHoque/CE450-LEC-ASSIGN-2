def adder(f1, f2):

  def var_func(x):
    try:
      return f1(x) + f2(x)
    except (TypeError, ValueError):
      print("Invalid input, Please enter only number ")
  return var_func

def identity(n):
  return n

def square(n):
  return n ** 2


while True:
  try:
    x = int(input("Enter the number: "))
    break
  except ValueError:
    print("Invalid input, Please enter only number")

a1 = adder(identity, square)
print(a1(x))

a2 = adder(a1, identity)
print(a2(x))

a3 = adder(a1, a2)
print(a3(x))