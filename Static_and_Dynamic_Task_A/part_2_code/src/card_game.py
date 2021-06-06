### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

class CardGame:


  def check_for_ace(self, card):
    if card.value == 1:
      return True
    else:
      return False
   

  def highest_card(self, card1, card2):
    card1.value = convert_to_ace(self, card1)
    card2.value = convert_to_ace(self, card2)
    if card1.value > card2.value:
      return card1
    else:
      return card2

  def cards_total(self, cards):
    total = 0
    for card in cards:
      card.value = convert_to_ace(self, card)
      total += card.value      
    return f"You have a total of {total}"

def convert_to_ace(self, card):
  if card.value == 1:
      card.value = 13
  return card.value
  


