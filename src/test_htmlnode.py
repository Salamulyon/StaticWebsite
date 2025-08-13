import unittest
from htmlnode import HTMLNode

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


if __name__ == "__main__":
    unittest.main()