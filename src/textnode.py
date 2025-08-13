from enum import Enum

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    PLAIN = "plain"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        # if not url:
        #     self.url = None
        
    def __eq__(self, text_node):
        return (self.url == text_node.url and self.text_type == text_node.text_type and self.text == text_node.text)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
