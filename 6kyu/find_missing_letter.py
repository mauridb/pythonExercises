def find_missing_letter(chars):
  chars.sort()
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  if type(chars) != list:     
    print 'ERR: not list passed'
  elif len(chars) >= 2:
    if alphabet == ''.join(chars): 
      return 'is the same'
    start_point = alphabet.index(chars[0].lower())
    if start_point > 1:
      alphabet = alphabet[start_point::]
    for i, elem in enumerate(alphabet):
      if start_point > 1:
        elem = elem.upper()
      if elem != chars[i]:
        return elem
  else:
    return 'need a list of at least 2 elements'
      
        
# first case
print 'CASE 1:', find_missing_letter(['a','b','c','d','f'])
# second case
print 'CASE 2:', find_missing_letter(['O','Q','R','S','T'])
# third case
print 'CASE 3:', find_missing_letter(['b','c','d','e','f'])
# fourth case
print 'CASE 4: ',find_missing_letter(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
# fifth case
print 'CASE 5: ',find_missing_letter(['a'])
