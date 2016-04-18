import sys

HELP_TEXT = 'Usage: python forest1.py <file> <nodeID_1> <nodeID_2>'
SUPER_ROOT_UID = 'super_root'


class Node:
    """Represents a tree  node with identifier, data and a list of children nodes
    Provides basic functionality for a general tree
    methods: add_child(), show_children(), find_child(), ancestors()
    static methods: load_from_file()
    """
    def __init__(self, uid, data=None):
        """
        :param uid: Unique identifier for this node
        :param data:
        """
        self.uid = uid
        self.data = data  # placeholder for useful data
        self.children = []

    def __str__(self):
        return self.uid

    def __repr__(self):
        return str(self)

    def add_child(self, child):
        """Append a child node to this node's list of children.
        :param child: Node to be added
        """
        self.children.append(child)

    def show_children(self, depth=0):
        """Print out a tree structure starting from this node as a root.
        :param depth: Keeps track of recursion level,
            should be omitted when calling this method from outside the class
        """
        print('|', depth * '--', self)
        for c in self.children:
            c.show_children(depth + 1)

    def find_child(self, uid):
        """Search for a successor node of a current node with specified uid.
        :param uid: identifier of a target node
        :return: Node object or None if a node with specified uid is not found
        """
        if self.uid == uid:
            return self
        else:
            for c in self.children:
                return c.find_child(uid)
        return None

    def ancestors(self, target_uid, parents=None):
        """Construct and return a list of ancestral nodes to the target node.
        :param target_uid: identifier of a target node
        :param parents: list for storing ancestral nodes
            should be omitted when calling this method from outside the class
        :return: list of ancestors in a bottom-up order up to the root node
            or [] if target node not found
        """
        if parents is None:  # Create a new empty list for every external call.
            parents = []

        if self.uid == target_uid:
            return True
        # If any of the children of a current node test True for being an ancestor to the target node,
        # current node should be added to the list of ancestors to the target node.
        if any(c.ancestors(target_uid, parents) for c in self.children):
            parents.append(self)
        return parents

    @staticmethod
    def load_from_file(path):
        """Construct a tree from a text file.
        A file may contain more than one tree (contain multiple lines with a single node), for that reason
        all root nodes from a file become children of a super_root node, which is returned.
        :param path: path to a text file containing the definition of a tree
        :return: super_root Node object, that is a root to a tree defined in a file
        """
        root_node = Node(SUPER_ROOT_UID)
        with open(path) as in_file:
            for line in in_file.readlines():
                words = line.split()
                if len(words) == 1:                         # Top level node with no parents
                    root_node.add_child(Node(words[0]))     # becomes a child to super_root.
                else:
                    parent = root_node.find_child(words[1])
                    parent.add_child(Node(words[0]))
        return root_node


def closest_common_ancestor(root_node, first_node, second_node):
    """Find the nearest common ancestor to nodes with specified ids.
    Uses Node.parents() method
    :param root_node: Node object, root of tree to be searched
    :param first_node: identifier of first node object
    :param second_node: identifier of second node object
    :return: Node object or None if either or both first_node and second_node are not found
    """
    first, second = root_node.ancestors(first_node), root_node.ancestors(second_node)
    x = None
    # Last matching node in ancestral lists is the closest common ancestor.
    while first and second and first[-1] == second[-1]:
        x, _ = first.pop(), second.pop()
    return x


if __name__ == '__main__':
    if '-h' in sys.argv or len(sys.argv) != 4:
        print(HELP_TEXT)
        exit()
    else:
        path, first_node, second_node = sys.argv[1:]
        try:
            root_node = Node.load_from_file(path)
            cca = closest_common_ancestor(root_node, first_node, second_node)
            if not cca:
                print('{} and/or {} not found in tree'.format(first_node, second_node))
            elif cca.uid == SUPER_ROOT_UID:
                print("{} and {} don't have common ancestors".format(first_node, second_node))
            else:
                print(cca)
        except IOError:
            print('file', path, 'not found or corrupt')
