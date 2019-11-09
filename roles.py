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



## --------------ROLES SECTION----------------------

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
  print("\nThe Tree:")
  while len(l) > 0:
    if roles.get(l[0]):
      sys.stdout.write(f"{l[0]} -> ")
      for a in roles[l[0]]:
        sys.stdout.write(f"{a}, ")
        l.append(a)
      print()
    l.remove(l[0])
  print()

def orderRoles(roles, head):
  ordered = dict()
  l = [head]
  while len(l) > 0:
    if roles.get(l[0]):
      ordered[l[0]] = roles[l[0]]
      for a in roles[l[0]]:
        l.append(a)
    l.remove(l[0])
  return ordered






# ---------------------- RANDOM ----------------------------------------------

def userMatrix(reverse_roles, users):
  roles = []
  for i in reverse_roles:
    if i not in roles:
      roles.append(i)
    if reverse_roles.get(i) not in roles:
      for a in reverse_roles[i]:
        if a not in roles:
          roles.append(a)

  empty = " "
  for user in users:
    print("   ",end="")
    for role in roles:
      print(f"{empty*(9-len(role))}{role[0:9]}", end="")
    print(f"\n{user}:", end="")
    for role in roles:
      if role in users[user]:
        print(f"       + ", end="")
      else:
        print(empty*9, end="")
    print()
  
def loop_until_constraints():
  while True:
    (line_no,isMoreValid, constraints) = read_constraints()
    if isMoreValid:
      print_constraints(constraints)
      return constraints
    input(f'Invalid constraints at line no#: {line_no+1}, press ENTER to read it again')

def matrixControls(roles, matrix):
  for descendant in roles:
    if "control" not in matrix[descendant][descendant]:
      matrix[descendant][descendant].append("control")
    for ascendant in roles[descendant]:
      if "control" not in matrix[ascendant][ascendant]:
        matrix[ascendant][ascendant].append("control")
  return matrix

def matrixOwn(roles, matrix):
  for role in roles:
    stack = []
    for a in roles[role]:
      stack.append(a)    
    while len(stack) > 0:
      if roles.get(stack[0]):
        for a in roles[stack[0]]:
          stack.append(a)
      if "owns" not in matrix[role][stack[0]]:
        matrix[role][stack[0]].append("owns")
      stack.remove(stack[0])
  return matrix


## --------------PERMISSIONS SECTION----------------------

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


## --------------CONSTRAINTS SECTION----------------------

def print_constraints(constraints):
  counter = 1
  for i in constraints:
    print('Constraint '+str(counter)+", n = "+i['n']+', set of roles = {',end='')
    for b in i['roles']:
      print(b+', ',end = '')
    print('}')
    counter += 1

def read_constraints():
  try:    
    constraints = []
    f = open('roleSetsSSD.txt')
    line = f.readlines()
    f.close()
    counter = 0
    for i in line:
      line2 = i.split()
      constraints.append(dict())
      if(int(line2[0])<2):
        return (counter,False, None)
      constraints[counter]['n']=line2[0]
      line2.remove(line2[0])
      constraints[counter]['roles'] = line2
      counter = counter + 1
    return (None,True, constraints)
  except:
    input('Please have a valid file before attempting again. Press enter once this is updated')


## --------------USER SECTION----------------------

def checkUsers(constraints):
  f = open('userRoles.txt')
  users = dict()
  lines = f.readlines()
  f.close()
  j = 0
  for line in lines:
    c = []
    for i in range(len(constraints)):
      c.append(dict())
      c[i]["n"] = constraints[i]["n"]
      c[i]["roles"] = []
      for r in range(len(constraints[i]["roles"])):
        c[i]["roles"].append(constraints[i]["roles"][r])

    line = line.split()
    if users.get(line[0]):
      return (False, j+1, None, f'duplicate user: {line[0]}')
    users[line[0]] = []

    for role in line[1:]:
      cnum = 1
      for n in c:
        if role in n["roles"]:
          n["n"] = int(n["n"]) - 1
          if n["n"] == 0:
            return (False, j+1, None, f'constraint #{cnum}')
        cnum += 1
      users[line[0]].append(role)
    j += 1

  return (True, None, users, None)



def readUsers(constraints):
  while True:
    (valid, line, users, failure) = checkUsers(constraints)
    if valid:
      return users
    input(f'Invalid line is found in usersRoles.txt: line {line} due to {failure}, press ENTER to read it again')



## --------------MATRIX SECTION----------------------
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

# Momento
# def printMatrix2(mat):
#   for role in mat:
#     print(" "*12)
#     for role2 in mat[role]:
#       print(role2+" "*9,end='')
#     print(str(role)+":", end ='')    
#     none_found = False
#     counter = 0
#     while not none_found:
#       for role3 in mat[role]:
#             if mat[role][role3][counter] == []:
#               print(' '*6)
#             else:
#               lengthOf = 9-len(permission)
#               print(' '*lengthOf+str(permission))

def printMatrix(mat):
  print("--------"*6)
  emptys = " "
  for role in mat:
    stack = []
    n = len(mat[role])
    i = 0
    sys.stdout.write("   ")
    for ob in mat[role]:
      stack.append(mat[role][ob][:])
      sys.stdout.write(f"{emptys*(9-len(ob))}{ob}")
      if (i+1) % 5 == 0 or i+1 == n:
        sys.stdout.write(f"\n{role}:")
        s = len(stack)
        while s is not 0:
          s = len(stack)
          for p in stack:
            if p == []:
              sys.stdout.write(emptys*9)
              s = s - 1
            else:
              sys.stdout.write(f"{emptys*(9-len(p[0]))}{p[0][0:9]}")
              p.remove(p[0])
          sys.stdout.write("\n   ")
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
  while True:
    r = getResources("resourceObjects.txt")
    r = removeEmpty(r)
    (dupe, found) = checkDupes(r)
    if not found:
      mat = buildEmptyMatrix(roles, r)
      print("Empty Object-Control Matrix:")
      printMatrix(mat) 
      cmat = matrixOwn(reverse_roles, matrixControls(reverse_roles, mat))
      print()
      return cmat
    input(f"Duplicate object is found {dupe}, press ENTER to read it again")
# -----------------------------QUERY-----------------------------------------

def query_valid(user_matrix,permission_matrix):  
  while True:
    user = input('Please enter the user in your query:')
    the_object = input('Please enter the object in your query (hit enter if it’s for any):')
    the_permission = input('Please enter the access right in your query (hit enter if it’s for any):')  
    if user in user_matrix:
      if query_logic(user,the_object,the_permission,user_matrix,permission_matrix):      
        continue_val = input('Would you like to continue for the next query?')
        if continue_val != 'yes':
          break
      else:
        print('invalid object, try again')
    else:
      print('invalid user, try again')

def query_logic(user, the_object, permission, user_matrix, permission_matrix):
  if the_object == '' and permission == '':
    for role in user_matrix[user]:
      for object1 in permission_matrix[role]:
        if permission_matrix[role][object1] != []:
          print(object1,end= ' ')
          for permission2 in permission_matrix[role][object1]:
            print(f'{permission2}, ',end ='')
          print()
    return True
  allowed = False
  for role in user_matrix[user]:
    if the_object not in permission_matrix[role]:
      return False  
    if permission == '':
      print(the_object,end=' ')
      for x in permission_matrix[role][the_object]:
        print(f'{x}, ', end='')
      print()
      return True
    if permission in permission_matrix[role][the_object]:
      allowed = True
  if allowed:
    print('authorized')
  else:
    print('rejected')
  return True


# ----------------------------MAIN-------------------------------------------

def main():
  while True:
    (valid, roles,reverse_roles) = getRoles("roleHierarchy.txt")
    (isValid,permissions) = readPermissions()
    constraints = loop_until_constraints()
    valid = valid and isValid
    if valid:
      head = findHead(roles)
      reverse_roles = orderRoles(reverse_roles, head)
      pTree(reverse_roles, head)
      matrix = resources(roles, reverse_roles)
      print(f"Matrix is: {matrix}")
      printMatrix(matrix)
      permissions_matrix = addPermissions(matrix,roles,permissions)
      print("\nFilled Object-Control Matrix:")
      printMatrix(matrix)
      print()
      users = readUsers(constraints)
      userMatrix(reverse_roles, users)
      query_valid(users,permissions_matrix)
      break
    input(
      f"Invalid tree, duplicate decendant: {roles}, press ENTER to read it again")

if __name__ == "__main__":
  main()