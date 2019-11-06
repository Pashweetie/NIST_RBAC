class Node:
  def __init__(self, role = None, descendant=[], ascendants=[]):
    self.role = role
    self.descendants = descendant
    self.ascendant = ascendants
def build_tree(a_descendant, a_ascendant):
    
    return a_descendant
def traverse_down(start,role):
    hi = 0
    #to be implemented
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
    needToCheck = []
    for line in fline:
        needToCheck.append(line.split())
    print_array(needToCheck)
    while needToCheck != []:
        for line in needToCheck:
            inTree = traverse_down(root,line)
            if inTree != None:
                root = inTree
            #traverse down to check if its in the tree
            #if it is then add it to the tree
            #otherwise keep in in needToCheck
    print_tree(root)
def print_array(array):
    for i in array:
        print()
        for b in i:
            print (b+" ",end='')
def print_tree(root):
    print(root.role)
    for nodes in root.ascendant:
        if nodes != None:
            print(nodes.role)
        elif nodes.ascendant != None:
            print_tree(nodes)

        print(nodes.role)
if __name__ == "__main__":
  main()