"""
Factor generic code from subclasses such as Href, Table, etc into a superclass
to achieves code reuse and avoid code duplication.
"""

class HTMLElement:
    def __init__(self, **kw):
        for attr in kw:
            try:
                getattr(self, attr)
                setattr(self, attr, kw[attr])
            except:
                raise KeyError("Unsupported argument %s!" % attr)

class Table(HTMLElement):
    """ To be ported from Robin F's Table class
    """

class Href(HTMLElement):

    target = None
    onClick = None
    onMouseOver = None
    onMouseOut = None

    def __init__(self,
                 url='',
                 text='',
                 **kw):
        
        self.url = url
        self.text = text

        HTMLElement.__init__(self, **kw)

    def __str__(self):
        s = ['<A HREF="%s"' % self.url]
        if self.target: s.append(' TARGET="%s"' % self.target)
        if self.onClick: s.append(' onClick="%s"' % self.onClick)
        if self.onMouseOver: s.append(' onMouseOver="%s"' % self.onMouseOver)
        if self.onMouseOut: s.append(' onMouseOut="%s"' % self.onMouseOut)
        s.append('>%s</A>' % self.text)
        return ''.join(s)
        
usd = Href(text='USD', url='http://www.sandiego.edu', target='_blank')
print(usd)
