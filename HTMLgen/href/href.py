"""
Last version was incorrect because Href's initializer will allow
creation of meaningless attributes. 

This version corrects the error of the last version.

"""

class Href:

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

        for attr in kw:
            try:
                getattr(self, attr) # see if self  knows about attr
                setattr(self, attr, kw[attr])
            except:
                raise KeyError("You provide an argument %s that makes no sense" % attr)

    def __str__(self):
        s = ['<A HREF="%s"' % self.url]
        if self.target: s.append(' TARGET="%s"' % self.target)
        if self.onClick: s.append(' onClick="%s"' % self.onClick)
        if self.onMouseOver: s.append(' onMouseOver="%s"' % self.onMouseOver)
        if self.onMouseOut: s.append(' onMouseOut="%s"' % self.onMouseOut)
        s.append('>%s</A>' % self.text)
        return ''.join(s)

usd = Href('http://www.sandiego.edu', 'University of San diego', target='_blank')
print(usd)

ucsd = Href('http://ucsd.edu', 'UCSD', age =40) # Exception!

