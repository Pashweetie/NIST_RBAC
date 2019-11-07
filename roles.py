import sys
def removeEmpty(r):
  while("" in r):
    r.remove("")
  return r

def getRules():
  f = open('permissionsToRoles.txt')
  rules = dict()

def inherit(matrix, keys, ascendant):
  descendant = keys[ascendant]
  
  if descendant == None:
    return
  inherit(keys[ascendant])

def getRoles(name):
  f = open(name)
  lines = f.readlines()
  roles = dict()
  reverse_roles = dict()
  for line in lines:
    vline = removeEmpty(line.strip("\n").split(" "))
    if len(vline) > 2:
      return (False, {},{})
    if roles.get(vline[0]):
      return (False, vline[0],{})
    else:
      roles[vline[0]] = vline[1]
    if reverse_roles.get(vline[1]):
      reverse_roles[vline[1]].append(vline[0])
    else:
      reverse_roles[vline[1]]=[vline[0]]
  return (True, roles, reverse_roles)

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
    (valid, roles,reverse_roles) = getRoles("roleHierarchy.txt")
    if valid:
      # print(r)
      head = findHead(roles)
      printTree(head, roles)
      resources(roles)
      break
    input(
      f"Invalid tree, duplicate decendant: {roles}, press ENTER to read it again")


def buildMatrix(roles, res):
  matrix = dict()
  for role in roles:
    inner = dict()
    for r in res:
      inner[r] = []
    matrix[role] = inner
  return matrix

def roleMatrix(roles, res):
  n = len(res)
  m = len(roles)
  print("-----"*6)
  for role in roles:
    sys.stdout.write("   ")
    for i in range(n+m):
      if i >= m:
        sys.stdout.write(f"   {res[i-m]}")
      else:
        sys.stdout.write(f"   {roles[i]}")
      if (i+1) % 5 == 0 or i+1 == n+m:
        sys.stdout.write(f"\n{role}:\n   ")
    print("-----"*5)

def checkDupes(r):
  c = []
  for resource in r:
    if resource not in c:
      c.append(resource)
    else:
      return (resource, True)
  return ("", False)

def getResources(name):
  f = open(name)
  line = f.readline()
  f.close()
  return line.split(" ")

def resources(rroles):
  roles = []
  for i in rroles:
    if i not in roles:
      roles.append(i)
    if rroles.get(i) not in roles:
      roles.append(rroles.get(i))

  print(roles)
  while True:
    r = getResources("resourceObjects.txt")
    r = removeEmpty(r)
    (dupe, found) = checkDupes(r)
    if not found:
      roleMatrix(roles,r)
      print(buildMatrix(roles,r))
      break
    input(f"Duplicate object is found {dupe}, press ENTER to read it again")



if __name__ == "__main__":
  main()