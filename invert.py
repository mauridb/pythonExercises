# check if list of number
def check_if_list_number(l):
  list_checked = [True if type(elem) == int else False for elem in l]
  if False in list_checked:
    return False
  return True
    
    
def invert(lst):
  if type(lst) != list:
    print 'ERR: not list passed'
  else:
    if check_if_list_number(lst):
      # solution is if else list comprehension
      solution = [ -number if number > 0 else abs(number) for number in lst]
      return solution


print invert([1,2,3,4,5,6])
print invert([-1,-2,-3,-4,-5,-6])
print invert([-1,2,-3,-4,5,-6])
print invert([-1,2,-3,0,5,-6])

