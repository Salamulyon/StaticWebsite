import unittest
from htmlnode import HTMLNode,LeafNode

class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode("p","html node","child",{"href": "https://www.google.com",
                                                "target": "_blank"
                                                })
        
        self.assertEqual(node1.props_to_html(),' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node1 = HTMLNode("p","html node","child",{"href": "https://www.google.com",
                                                "target": "_blank"
                                                })
        self.assertEqual(str(node1),'HTMLNode(p,html node,child, href="https://www.google.com" target="_blank")')

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        #node1 = LeafNode("p","leaf node")
        node2 = LeafNode("p", "This is a paragraph of text.")
        node3 = LeafNode("a", "Click me!",{"href": "https://www.google.com"})

        #self.assertEqual(node1.to_html,)
        self.assertEqual(node2.to_html(),"<p>This is a paragraph of text.</p>")
        self.assertEqual(node3.to_html(),"<a href='https://www.google.com'>Click me!</a>")

if __name__ == "__main__":
    unittest.main()