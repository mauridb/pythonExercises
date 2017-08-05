def digital_root(n):
  string = str(n)
  solution = sum([int(number) for number in string])
  return solution


print digital_root(79878097)
print digital_root(15)
print digital_root(7)
