

class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props: dict=None):
        self.tag = tag
        self.val = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        text = ""

        for key,value in self.props.items():
            text += f' {key}="{value}"'

        return text
    
    def __repr__(self):
        return f'HTMLNode({self.tag},{self.val},{self.children},{self.props_to_html()})'