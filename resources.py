import sys

def roleObject(roles, res):
  n = len(res)
  print("-----"*5)
  for role in roles:
    for i in range(n):
      sys.stdout.write(f"   {res[i]}")
      if (i+1) % 5 == 0 or i+1 == n:
        print(f"\n{role}:")
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

def main():
  while True:
    r = getResources("resourceObjects.txt")
    (dupe, found) = checkDupes(r)
    if not found:
      roleObject(["R1", "R2", "R3"],r)
      break
    input(f"Duplicate object is found {dupe}, press ENTER to read it again")

  


if __name__ == "__main__":
  main()