class Bank:
  def __init__(self):
    self._balance=0
  @property
  def noresbalance(self):
    return self._balance
  @noresbalance.setter
  def noresbalance(self,amount):
    self._balance+=amount
b=Bank()
print(b.noresbalance)
b.noresbalance=2000
print(b.noresbalance)