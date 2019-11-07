import sys
def removeEmpty(r):
  while("" in r):
    r.remove("")
  return r


def getRoles(name):
  f = open(name)
  lines = f.readlines()
  roles = dict()
  for line in lines:
    vline = removeEmpty(line.strip("\n").split(" "))
    if len(vline) > 2:
      return (False, {})
    if roles.get(vline[0]):
      return (False, vline[0])
    else:
      roles[vline[0]] = vline[1]
  return (True, roles)


def findHead(roles):
  for ascendant in roles:
    if not roles.get(roles[ascendant]):
      return roles.get(ascendant)

def printTree(key, roles):
  plist = []
  for role in roles:
    if roles.get(role) == key:
      plist.append(role)
  sys.stdout.write(f"{key} -> ")
  for item in plist:
    sys.stdout.write(f"{item}, ")
  print()
  for item in plist:
    printTree(item, roles)

def main():
  while True:
    (valid, roles) = getRoles("roleHierarchy.txt")
    if valid:
      # print(r)
      head = findHead(roles)
      printTree(head, roles)
      break
    input(
      f"Invalid tree, duplicate decendant: {roles}, press ENTER to read it again")


if __name__ == "__main__":
  main()