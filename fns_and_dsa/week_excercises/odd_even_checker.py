def odd_or_even():
  number = float(input("Enter the number you'd like to check: "))
  if number % 2 == 0:
    return print(f"The number {number} is even")
  else:
       return print(f"The number {number} is odd")

odd_or_even()