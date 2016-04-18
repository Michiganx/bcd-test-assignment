The basic idea is to construct an ordered a list of ancestors for both nodes. The last matching ancestor will be the closest common one to both nodes.
Task implies that a single input file may contain description of several trees. (Lines with only one node)
For more elegant design, rather than searching multiple trees, let us make all of the trees from the input file subtrees of a single tree,
by making all the root nodes from the file children to a common parent node (super_root)
If the CCA for two Nodes comes back as super_root it means they are not in the same tree and don't have common ancestors

Assumption about the file:
- No node has more than one parent
- Lines may follow in arbitrary order, but
- ... a root is declared before its children

Who is and isn't a parent?
For the purposes  of this task lets assume that the node is NOT a parent or a child to itself
         A
        / \
       /   \
      /     \
     B       C
    / \     /
   D   E   F

for the tree above CCA(D,B) would be A, but B and A would have NO common ancestors
following the same logic CCA(B,B) would be A, but A and A have NO common ancestors
