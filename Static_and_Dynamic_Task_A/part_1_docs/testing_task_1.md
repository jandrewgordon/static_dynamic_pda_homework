### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
  # Conditional is missing the second '='. It should be "is card.value == 1;"
    if card.value = 1:
      return True
  # ":" is missing after "else"
    else
      return False
   

  dif highest_card(self, card1 card2):
  # Function should be defined with "def" and the logic should be indented.
  # "," is missing after card1 in the function's arguements.
  if card1.value > card2.value:
  # Aces are passed through with a value of "1" so this function will return a wrong answer unless aces are converted to a higher number.
    return card
    # Above should be "return card1"
  else:
    return card2
  

# The function is not correctly indented inside the CardGame class
def cards_total(self, cards):
# The variable "total" is not properly declared. It should be given an initial value, i.e. "total = 0"
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
