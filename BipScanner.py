class baby:
  kuttests = {"bib", "bips", "bop", "lob", "beep"}
  def __init__(self, name, kuttnessLevel):
    self.name=name
    self.kuttnessLevel=kuttnessLevel

  def isBest(self):
    if self.name in self.kuttests:
      print("YES!", self.name, "is kuttest.")
    else:
      print("not kutt")

  def needKos(self):
    print("this baby surely needs kos.")
  def deserveKos(self):
    if self.name in self.kuttests:
      print("of course she deserve kos!")
    else:
      print("this baby does not deserve kos.")



print("type in baby name")
name=input()
bib=baby(name, 100)
bib.isBest()
bib.needKos()
bib.deserveKos()