

class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props: dict=None):
        self.tag = tag
        self.val = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        
        text = ""
        for key,value in self.props.items():
            text += f' {key}="{value}"'

        return text
    
    def __repr__(self):
        return f'HTMLNode({self.tag},{self.val},{self.children},{self.props_to_html()})'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value,None, props)

    def to_html(self):
        prop_text = ""
        
        if not self.val:
            raise ValueError('Missing Leaf node Value')
        if not self.tag:
            return self.val
        
        if self.props:
            prop_text = self.props_to_html()
        
        return f"<{self.tag}{prop_text}>{self.val}</{self.tag}>"
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError ("tag class missing")
        if not self.children:
            raise ValueError ("children tag missing")

        htmltext = []
        for child in self.children:
            htmltext.append(child.to_html())
        
        return f"<{self.tag}{self.props_to_html()}>{"".join(htmltext)}</{self.tag}>"
        

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"