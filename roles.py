import sys
def removeEmpty(r):
  while("" in r):
    r.remove("")
  return r

def getRules():
  f = open('permissionsToRoles.txt')
  rules = dict()

def inherit(matrix, keys, ascendant,permission,resource):
  descendant = keys.get(ascendant)
  print(descendant)
  if matrix[ascendant][resource] == None:
    matrix[ascendant][resource] = [permission]
  else:
    role_exist = False
    for i in matrix[ascendant][resource]:
      if i == permission:
        role_exist = True
    if not role_exist:
      matrix[ascendant][resource].append(permission)
  if descendant == None:
    return matrix
  return inherit(matrix,keys, descendant,permission,resource)

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
  if len(plist) > 0:
    sys.stdout.write(f"{key} -> ")
    for item in plist:
      sys.stdout.write(f"{item}, ")
    print()
    for item in plist:
      printTree(item, roles)

def pTree(roles, head):
  ordered = dict()
  l = [head]
  while len(l) > 0:
    if roles.get(l[0]):
      sys.stdout.write(f"{l[0]} -> ")
      for a in roles[l[0]]:
        sys.stdout.write(f"{a}, ")
        l.append(a)
      print()
    l.remove(l[0])

def orderRoles(roles, head):
  ordered = dict()
  l = [head]
  while len(l) > 0:
    if roles.get(l[0]):
      ordered[l[0]] = roles[l[0]]
      for a in roles[l[0]]:
        l.append(a)
    l.remove(l[0])
    print()
  return ordered


def main():
  while True:
    (valid, roles,reverse_roles) = getRoles("roleHierarchy.txt")
    (isValid,permissions) = readPermissions()
    valid = valid and isValid
    if valid:
      # print(r)
      head = findHead(roles)
      
      
      reverse_roles = orderRoles(reverse_roles, head)
      pTree(reverse_roles, head)
      print(reverse_roles)
      # matrix = resources(roles, reverse_roles)
      # matrix = addPermissions(matrix,roles,permissions)
      # printMatrix(matrix)
      break
    input(
      f"Invalid tree, duplicate decendant: {roles}, press ENTER to read it again")

def matrixControls(roles, matrix):
  for descendant in roles:
    if "control" not in matrix[descendant][descendant]:
      matrix[descendant][descendant].append("control")
    for ascendant in roles[descendant]:
      if "control" not in matrix[ascendant][ascendant]:
        matrix[ascendant][ascendant].append("control")
      # matrix[descendant][ascendant].append("own")
  return matrix

# def matrixOwn(roles, matrix, val):
def addPermissions(matrix, keys,permissions):
  new_matrix = dict()
  for i in permissions:
    ascendant = i[0]
    permission = i[1]
    resource = i[2]
    new_matrix = inherit(matrix,keys,ascendant,permission,resource)
  return new_matrix
def readPermissions():
  try:    
    f = open('permissionsToRoles.txt')
    line = f.readlines()
    f.close()
    return_array = []
    for i in line:
      return_array.append(i.split())

    return (True,return_array)
  except:
    return (False, None)

def buildEmptyMatrix(roles, res):
  matrix = dict()
  for role in roles:
    inner = dict()
    for r in roles:
      inner[r] = []
    for r in res:
      inner[r] = []
    matrix[role] = inner
  return matrix

# Old version of printing the role matrix
# def roleMatrix(roles, res):
#   n = len(res)
#   m = len(roles)
#   print("-----"*6)
#   for role in roles:
#     sys.stdout.write("   ")
#     for i in range(n+m):
#       if i >= m:
#         sys.stdout.write(f"   {res[i-m]}")
#       else:
#         sys.stdout.write(f"   {roles[i]}")
#       if (i+1) % 5 == 0 or i+1 == n+m:
#         sys.stdout.write(f"\n{role}:\n   ")
#     print("-----"*5)

def printMatrix(mat):
  print("--------"*6)
  emptys = " "
  for role in mat:
    stack = []
    n = len(mat[role])
    i = 0
    sys.stdout.write("   ")
    for ob in mat[role]:
      stack.append(ob)
      sys.stdout.write(f"{emptys*(9-len(ob))}{ob}")
      if (i+1) % 5 == 0 or i+1 == n:
        sys.stdout.write(f"\n{role}:")
        for p in stack:
          if mat[role][p] == []:
            sys.stdout.write(emptys*9)
          else:
            sys.stdout.write(f"{emptys*(9-len(mat[role][p][0]))}{mat[role][p][0]}")
        stack = []
        sys.stdout.write("\n\n   ")
      i = i+1
    print("--------"*6)

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

def resources(rroles, reverse_roles):
  roles = []
  for i in reverse_roles:
    if i not in roles:
      roles.append(i)
    if reverse_roles.get(i) not in roles:
      for a in reverse_roles[i]:
        if a not in roles:
          roles.append(a)
  print(roles)
  while True:
    r = getResources("resourceObjects.txt")
    r = removeEmpty(r)
    (dupe, found) = checkDupes(r)
    if not found:
      mat = buildEmptyMatrix(roles, r)
      # printMatrix(mat)
      cmat = matrixControls(reverse_roles, mat)
      # printMatrix(cmat)
      return cmat
    input(f"Duplicate object is found {dupe}, press ENTER to read it again")



if __name__ == "__main__":
  main()