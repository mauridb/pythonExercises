def xo(s):
  # method that count if in string there is the same 'x' and 'o'
  pattern = ['x','o']
  tmp = [elem if elem in pattern else '' for elem in s.lower()]
  currency = []
  for elem in pattern:
    currency.append(tmp.count(elem))
  if currency[0]==currency[1]:
    return True
  else:
    return False


print xo('ooxx')
print xo('oox!0')
print xo('xxxoo')
