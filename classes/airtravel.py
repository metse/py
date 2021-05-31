
class Flight:

  def __init__(self, number):
    if not number[:2].isalpha():
      raise ValueError(f'No airline code in {number}')
    if not number[:2].isupper():
      raise ValueError(f'Invalid airline code {number}')

    self._number = number
  
  def number(self):
    return self._number