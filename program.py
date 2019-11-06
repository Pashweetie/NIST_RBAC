class Node:
  def __init__(self, role = None, descendants=[], ascendant=[]):
    self.role = role
    self.descendants = descendants
    self.ascendant = ascendant
def build_tree():
    ayy = 0
def build_tree_test(root, role):
    print("before"+root.role)
    root.ascendant.append(Node(role,root,None))
    print("after"+root.role)
    
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
    root = Node()
    for line in fline:
        a_d_array = line.split()
        root.role = a_d_array[0]
        root = build_tree_test(root,a_d_array[1])
    print_tree(root)
def print_tree(root):
    for nodes in root.ascendant:
        print(nodes.role)
if __name__ == "__main__":
  main()