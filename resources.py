import sys

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

def removeEmpty(r):
  while("" in r):
    r.remove("")
  return r

def main():
  roles = ["R1", "R2", "R3"] #temp
  while True:
    r = getResources("resourceObjects.txt")
    r = removeEmpty(r)
    (dupe, found) = checkDupes(r)
    if not found:
      roleMatrix(roles,r)
      break
    input(f"Duplicate object is found {dupe}, press ENTER to read it again")

  


if __name__ == "__main__":
  main()