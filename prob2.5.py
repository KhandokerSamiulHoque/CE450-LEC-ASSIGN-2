def intscts(f, x):

  def g(function):
    return f(x) == function(x)
  return g


def square(n):
  return n ** 2

def triple(n):
  return 3 * n


def increment(n):

  return n + 1


def identity(n):

  return n


def main():

  f_case = input("Enter square, triple, increment or identity for 1st case: ")
  x = int(input("Enter x: "))
  g_case = input("Enter square, triple, increment or identity for 2nd case: ")
  try:
    f = {
      "square": square,
      "triple": triple,
      "increment": increment,
      "identity": identity,
    }[f_case]
  except KeyError:
    print(f"Invalid function name. Please enter one of the following: square, triple, increment, identity.")
    exit()

  try:
    g = {
      "square": square,
      "triple": triple,
      "increment": increment,
      "identity": identity,
    }[g_case]
  except KeyError:
    print(f"Invalid function name. Please enter one of the following: square, triple, increment, identity.")
    exit()

  x_val = intscts(f, x)
  print(x_val(g))

if __name__ == "__main__":
  main()
