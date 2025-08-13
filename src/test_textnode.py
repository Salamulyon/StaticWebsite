import unittest
from textnode import TextNode,TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("Text node",TextType.BOLD)
        node2 = TextNode("Text node",TextType.BOLD)
        self.assertEqual(node1,node2)

    def test_url_not_eq(self):
        node1 = TextNode("Text node",TextType.BOLD,"https:google.com")
        node2 = TextNode("Text node",TextType.BOLD)
        self.assertNotEqual(node1,node2)




if __name__ == "__main__":
    unittest.main()