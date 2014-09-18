"""

This is a quantum leap from the previous version.  Note that the long
list of arguments in the definition of the initializer disappears, and
so does the equally long block of the if statements.

It is amazing that no matter how many attributes the class uses, the size of its initializer remains a constant.

"""

class Href:

    target=None
    onClick=None
    onMouseOver=None
    onMouseOut=None

    def __init__(self,
                 url,
                 text,
                 **kw):

        self.url = url
        self.text = text

        for key in kw:
            setattr(self, key, kw[key])

    def __str__(self):
        s = ['<A HREF="%s"' % self.url]
        if self.target: s.append(' TARGET="%s"' % self.target)
        if self.onClick: s.append(' onClick="%s"' % self.onClick)
        if self.onMouseOver: s.append(' onMouseOver="%s"' % self.onMouseOver)
        if self.onMouseOut: s.append(' onMouseOut="%s"' % self.onMouseOut)
        s.append('>%s</A>' % self.text)
        return ''.join(s)

ucsd = Href(text='UCSD', url='http://ucsd.edu', target='_blank')
print(ucsd)
