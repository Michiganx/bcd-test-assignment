import unittest
import os
from forest.forest1 import Node, closest_common_ancestor, SUPER_ROOT_UID

TEXT_FOR_INPUT = """NodeA
NodeB NodeA
NodeC NodeB
NodeF
NodeK NodeB
NodeT NodeB
NodeD NodeA"""

TMP_FILE_NAME = 'tmp.txt'

class ForestCase(unittest.TestCase):
    input_file = os.path.join(
                os.path.dirname(os.path.abspath(__file__)), TMP_FILE_NAME
            )

    @classmethod
    def setUpClass(cls):
        with open(cls.input_file, 'w') as in_f:
            in_f.write(TEXT_FOR_INPUT)

        cls.root = Node.load_from_file(cls.input_file)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.input_file)

    def test_normal(self):
        self.assertEqual(closest_common_ancestor(ForestCase.root, 'NodeK', 'NodeB').uid,
                         'NodeA')

    def test_no_common_ancs(self):
        self.assertEqual(closest_common_ancestor(ForestCase.root, 'NodeF', 'NodeA').uid,
                         SUPER_ROOT_UID)

    def test_direct_child(self):
        self.assertEqual(closest_common_ancestor(ForestCase.root, 'NodeT', 'NodeB').uid,
                         'NodeA')

    def test_direct_child_top_level(self):
        self.assertEqual(closest_common_ancestor(ForestCase.root, 'NodeB', 'NodeA').uid,
                         SUPER_ROOT_UID)

    def test_same_node(self):
        self.assertEqual(closest_common_ancestor(ForestCase.root, 'NodeA', 'NodeA').uid,
                         SUPER_ROOT_UID)

    def test_same_node_top_level(self):
        self.assertEqual(closest_common_ancestor(ForestCase.root, 'NodeK', 'NodeT').uid,
                         'NodeB')

    def test_node_not_found(self):
        self.assertEqual(closest_common_ancestor(ForestCase.root, 'NodeB', 'NodeX'),
                 None)

if __name__ == '__main__':
    unittest.main()
