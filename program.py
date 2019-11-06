class Node:
  def __init__(self, role = None, descendant=[], ascendants=[]):
    self.role = role
    self.descendants = descendant
    self.ascendant = ascendants
def build_tree(a_descendant, a_ascendant):
    #add here
    a_descendant.ascendant.append(Node(a_ascendant.role,a_descendant))
    return a_descendant
def traverse_down(start,role):
    hi=0
    #to be implemented
def main():
    while True:
        try:
            f = open('roleHierarchy.txt')
            break
        except:
            print('oops, please have a valid roleHierarchy.txt file in the directory')
            input('Press enter to try again')
    fline = f.readlines()
    root = Node()
    needToCheck = []
    for line in fline:
        needToCheck.append(line.split())
    print_array(needToCheck)
    count = 0
    while needToCheck != []:
        for line in needToCheck:
            if count != 0:
                if root.role == line[0]:
                    root = build_tree(Node(line[1]),root)
                    needToCheck.remove(line)
                else:
                    inTree = traverse_down(root,line[1])
                    if inTree != None:
                        build_tree(inTree,Node(line[0]))
                        needToCheck.remove(line)
            else:                    
                root = Node(line[1])
                root.ascendant.append(Node(line[0],root))
                count =1
                print_tree(root)
    print_tree(root)
def print_array(array):
    for i in array:
        print()
        for b in i:
            print (b+" ",end='')
def print_tree(root):
    print()
    for nodes in root.ascendant:
        print(root.role+" ->",end='')
        if nodes != None:
            print(nodes.role, end='')
        elif nodes.ascendant != None:
            print_tree(nodes)
        print()
if __name__ == "__main__":
  main()