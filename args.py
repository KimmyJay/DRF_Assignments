def assign_food_items(**order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  print(food)
  print(drinks)

# Example Call
assign_food_items(food='Pancakes, Poached Egg', drinks='Water')
#output
# Pancakes, Poached Egg
# Water



def print_animals(animal1, animal2, *args, animal4, **kwargs):
  print(animal1, animal2)
  print(args)
  print(animal4)
  print(kwargs)

# Example Call
print_animals('Snake', 'Fish', 'Guinea Pig', 'Owl', animal4='Cat', animal5='Dog')
#output
#Snake Fish
#('Guinea Pig', 'Owl')
#Cat
#{'animal5': 'Dog'}

my_num_list = [3, 6, 9]
numbers  = {'num1': 3, 'num2': 6, 'num3': 9}

def sum(num1, num2, num3):
  print(num1 + num2 + num3)
 
sum(*my_num_list)
sum(**numbers)
#output is 18 for both cases
