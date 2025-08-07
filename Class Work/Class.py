class Details:
  def __init__(self,name,email,pwd):
    self.name=name
    self._email=email
    self.__pwd=pwd
  def get(self):
    return self.__pwd
  def set(self,new_pwd):
    self.__pwd=new_pwd

vish=Details("vis","vish@gmail.com","vish@12")
print(vish.name)
vish.name="hema"
print(vish.name)
print(vish._email)
vish._email="hema@gmail.com"
print(vish._email)
print(vish.get())
vish.set("hema@12")
print(vish.get())

