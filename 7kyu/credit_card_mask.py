def maskify(cc):
  mask_str = ''
  for elem in cc[:-4:]:
    mask_str+='#'
  solution = mask_str + cc[-4::]
  return solution


print maskify('0566023650236502')
