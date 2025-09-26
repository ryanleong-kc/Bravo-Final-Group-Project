import random

def sum_date(date_string):
  cleaned_date = date_string.replace('/','')
  sum = 0

  for char in cleaned_date:
    sum += int(char)

  return sum

#FORTUNE TELLER FUNCTION
def fortune_teller():
  print("Welcome to Bravo's Fortune Teller!")
  print("Please enter your :-")
  name = input("Name :")

  birthday = input("Birthday (DD/MM/YYYY) : ")
  parts = birthday.split('/')

  if len(parts) == 3:
    birth_year = parts[2]

  current_year = 2025
  age = current_year - int(birth_year)

  print(f"\nHello {name}, press Enter to receive your fortune")
  rand_num = random.randint(0,12)

  list_fortunes = [
    "Expect good news in the near future.",
    "A journey of a thousand miles begins with a single step.",
    "You will soon have a chance to travel to a new place.",
    "Good things come to those who wait.",
    "The early bird gets the worm.",
    "Do not be afraid of the unknown, for it holds your future.",
    "Your hard work will soon pay off.",
    "Believe in yourself and your abilities.",
    "An exciting opportunity is just around the corner.",
    "A loyal friend is a great treasure.",
    "The best way to predict the future is to create it.",
    "Adventure is out there, find it.",
    "You will find happiness in unexpected places."
  ]
  
  print("Your fortune   : " + list_fortunes[rand_num])
  print(f"Your lucky age : {sum_date(birthday)}")

  if age >= sum_date(birthday):
    print("How's your lucky year? :)))")
  else:
    print("Can't wait for it to happen ;))")



#MAIN FUNCTION
print("""
 -------------------------------
|        FORTUNE TELLER         |
|            by Bravo           |
 -------------------------------
      """)
fortune_teller()
