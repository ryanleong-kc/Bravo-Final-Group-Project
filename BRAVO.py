import random

def sum_date(date_string):
  cleaned_date = date_string.replace('/','')
  sum = 0

  for char in cleaned_date:
    sum += int(char)

  return sum

def fortune_teller():
  print("Welcome to Bravo's Fortune Teller!")
  print("Please enter your :-")
  name = input("Name :")
  birthday = input("Birthday (DD/MM/YYYY) : ")
  print(f"Hello {name}, press Enter to receive your fortune")

  fortunes = ["Expect good news in the near future."]
  print("Your lucky age : " + sum_date(birthday))


print("""
 -------------------------------
|        FORTUNE TELLER         |
|            by Bravo           |
 -------------------------------
      """)
fortune_teller()
