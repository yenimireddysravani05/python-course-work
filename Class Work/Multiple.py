#Multiple multuple parents single child
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
class StatusV3(StatusV1,StatusV2):
  def addMusic(self,music):
    self.music=music
    print(f"{self.music} is added to your status")
sravani=Status()
sravani.uploadImage('selfie.png')
hema=StatusV1()
hema.uploadImage('GoodMnrg.png')
hema.addCaption("Morning frnds")
vish=StatusV2()
vish.uploadImage('Coffee.png')
vish.like()

rama=StatusV3()
rama.uploadImage("Mountains and Trees.png")
rama.addCaption("no wiif")
rama.like()
rama.addMusic("Maniratnam music.mp3")


