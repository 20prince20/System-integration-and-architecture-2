def print_even_numbers():
  for i in range(1, 100):
      if i % 2 == 0:
          print(i)
def print_odd_numbers():
  for i in range(1, 100):
      if i % 2 != 0:
          print(i)

value = input("odd or even?")
if value == "odd":
  print_odd_numbers()
else:
  print_even_numbers()
  
