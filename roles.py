
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


def printTree(roles):
  for role in roles:
    if roles.get(roles[role]):
      print(f"{roles.get(role)} -> {role} ")
    else:
      print(f"HEAD: {roles.get(role)} -> {role} ")


def main():
  while True:
    (valid, r) = getRoles("roleHierarchy.txt")
    if valid:
      print(r)
      printTree(r)
      break
    input(
      f"Invalid tree, duplicate decendant: {r}, press ENTER to read it again")


if __name__ == "__main__":
  main()