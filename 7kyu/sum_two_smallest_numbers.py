def sum_two_smallest_numbers(numbers):
  if len(numbers) < 4:
    return 'NOT ENOUGH NUMBER, insert at least 4 number'
  else:
    if False in [False if type(elem) != int else True for elem in numbers]:
      return 'ERR: only integer elements'
    else:
      copy_list = numbers
      solution = []
      for i in range(2):
        solution.append(copy_list.pop(copy_list.index(min(copy_list))))
      return sum(solution)
       
      




print sum_two_smallest_numbers([5,7,8,34,18,56])
print sum_two_smallest_numbers([34,18,56,90,'f'])
print sum_two_smallest_numbers([34,18,56])
print sum_two_smallest_numbers([5,5,5,34,18,56])
print sum_two_smallest_numbers([78333,56323232,98098,24523])
