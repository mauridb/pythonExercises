def find_missing_letter(chars):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  if type(chars) != list:     
    print 'ERR: not list passed'
  else:
    for i, elem in enumerate(alphabet):
      if elem.lower() != chars[i]:
        return elem
      
        

print find_missing_letter(['a','b','c','d','f'])
