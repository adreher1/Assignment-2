'''
Name Ava Dreher
email adreher1@binghamton.edu
Lab Section and CA Name B57 Owen and Jennifer
Assignment #2
'''

## Do not write anything past column 78
## Go to next line instead (no wrapping!)
## USE MEANINGFUL NAMES!
## variables will use lower_snake_case
## constants will use UPPER_SNAKE_CASE

'''
ANALYSIS

RESTATE the problem clearly and without ambiguity
The goal of this program is to calculate the total price of items purchased given the price of one item, the number purchased of that item and both
state and county taxes applied. 

OUTPUT to monitor:
  The subtotal and total prices of the items purchased.
  . . .

INPUT from keyboard:
  Enter price of item
  Enter number of items purchased
  
  . . .

GIVENS (i.e., program constants):
  COUNTY_TAX = 0.025
  STATE_TAX = 0.05
  
  
PROCESSING:
  state_tax = 0.05 * item_price
  county_tax = 0.025 * item_price
  sub_total = item_price * item_count
  total_cost_tax = item_price * item_count * total_tax
  
'''

#IMPORTS

# CONSTANTS (NO LITERALS ALLOWED!  Except 1, -1, and 0)
COUNTY_TAX = 0.025
STATE_TAX = 0.05


## BRIEF description of overall program
def main():
  print("This program will compute the total price of a purchased item" "\n" "including sales and county tax.")
  ## START by giving the overall flow of your program in comments,
  ##   then interleave your code

  # Explain purpose of program to user

  # Usually you are going to ask the user for some input
  item_price_str = input('Enter the price of the item: $')
  item_count_str = input('Enter the number of items purchased:')
  

  # You may need to convert the input
  item_price = float(item_price_str)
  item_count = int(item_count_str)
  
  

  # Usually you will have to process the input in some way to get the outputs
  import math
  state_tax = 0.05 * item_price
  county_tax = 0.025 * item_price
  total_tax = state_tax + county_tax
  sub_total = item_price * item_count
  total_cost_tax = item_price * item_count + total_tax
  

  # Finally, you will have to display your labeled and formatted output
  print('The subtotal is ' + "$"+str(sub_total))
  print('The total is ' + "$"+str(total_cost_tax))

if __name__ == '__main__' :
  main()
