class Node:
  def __init__(self, role, descendants, ascendant):
    self.role = role
    self.descendants = descendants
    self.ascendant = ascendant
def build_tree():
    ayy = 0
def build_tree_test(root, role):
    root.ascendant = Node(role,root,None)
    return root
def main():
    while True:
        try:
            f = open('roleHierarchy.txt')
            break
        except:
            print('oops, please have a valid roleHierarchy.txt file in the directory, then press enter')
            input()
    fline = f.readlines()
    for line in fline:
        a_d_array = line.split()
        print("ascendant"+str(a_d_array[0]))
        print("descendant"+str(a_d_array[1]))

if __name__ == "__main__":
  main()