
class Node:
  def __init__(self, role = None, descendant=[], ascendants=[]):
    self.role = role
    self.descendants = descendant
    self.ascendant = ascendants

def getRoles(name):
  f = open(name)
  lines = f.readlines()
  for line in lines:
    vline = 

def main():
  while True:
    r = getRoles("roleHierarchy.txt")
    (dupe, found) = checkDupes(r)
    if not found:
      roleObject(["R1", "R2", "R3"],r)
      break
    input(f"Duplicate object is found {dupe}, press ENTER to read it again")

if __name__ == "__main__":
  main()