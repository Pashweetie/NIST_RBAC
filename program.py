class Node:
  def __init__(self, role = None, descendant=[], ascendants=[]):
    self.role = role
    self.descendants = descendant
    self.ascendant = ascendants
def build_tree(a_descendant, a_ascendant):
    a_descendant.ascendant.append(Node(a_ascendant.role,a_descendant))
    return a_descendant
def traverse_down(start,role):
    if start.ascendant == []:
        return (None,False)
    elif start.role == role:
        return (start,True)
    else:
        # print(start.role)
        # print(role)
        # print(len(start.ascendant))
        for i in start.ascendant:
            # print(start.role)
            # print(i.role)
            # print(i.ascendant[0].role)
            traverse_down(i,role)
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
    f.close()
    print_array(needToCheck)
    count = 0
    while needToCheck != []:
        for line in needToCheck:
            print('on line:')
            print(line)
            print('root is')
            print(root.role)
            print()
            print_array(needToCheck)
            if count != 0:
                if root.role == line[1]:                    
                    print(line[1])
                    print(line[0])
                    print('the thing we were looking for was the root')
                    root = build_tree(Node(line[1]),root)
                    needToCheck.remove(line)
                else:
                    print('its not the root')
                    print(line[1])
                    print(line[0])
                    print(root.role == line[1])
                    (node,inTree) = traverse_down(root,line[1])
                    print(inTree)
                    if inTree:
                        build_tree(node,Node(line[0]))
                        print('before need to check')
                        print_array(needToCheck)
                        needToCheck.remove(line)
                        print('after need to check')
                        print_array(needToCheck)
            else:                    
                root = Node(line[1])
                root.ascendant.append(Node(line[0],root))
                needToCheck.remove(line)
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