class Status:
  def uploadImage(self,imageurl):
    self.image=imageurl
    print(f"{self.image} is uplaoaded to your Status")
class StatusV1(Status):
  def addCaption(self,text=None):
    self.caption=text
    print(f'"{self.caption}" is added to your status')
class StatusV2(Status):
  def like(self):
    print(f"You can like status")
sravani=Status()
sravani.uploadImage('selfie.png')
hema=StatusV1()
hema.uploadImage('GoodMnrg.png')
hema.addCaption("Morning frnds")
vish=StatusV2()
vish.uploadImage('Coffee.png')
vish.like()


    