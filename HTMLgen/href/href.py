"""In this third version, each instance has only attibutes that
it actually needs.

Note that <link>.<attribute> must resolve to an object, otherwise
__str__ would raise an exception.  Therefore, if <attribute> is not in
<link>'s namespace, it should be in Href's.

An eye sore of this version is that the number of the if statements
grows linearly as the number of the arguments.  So, in the case of
the Table class, we might have 40+ if statements.

"""

class Href:

    onClick = None
    onMouseOver = None
    onMouseOut = None
    target = None


    def __init__(self,
                 target=None,
                 onClick=None,
                 onMouseOver=None,
                 onMouseOut=None,
                 url='http://www.sandiego.edu',
                 text='USD'):
        if target: # if user passes in non-trivial values, then create
                   # an instance variable
                   self.target = target

        if onClick: # if user passes in non-trivial values, then create
                   # an instance variable
                   self.onClick = onClick
        if onMouseOver:
            self.onMouseOver = onMouseOver

        if onMouseOut:
            self.onMouseOut = onMouseOut 

        if url:
            self.url = url

        if text:
            self.text = text


    def __str__(self):
        s = ['<A HREF="%s"' % self.url]
        if self.target: s.append(' TARGET="%s"' % self.target)
        if self.onClick: s.append(' onClick="%s"' % self.onClick)
        if self.onMouseOver: s.append(' onMouseOver="%s"' % self.onMouseOver)
        if self.onMouseOut: s.append(' onMouseOut="%s"' % self.onMouseOut)
        s.append('>%s</A>' % self.text)
        return ''.join(s)

usd = Href(text='UCSD', url='http://ucsd.edu', target='_blank')
print(usd)
print(vars(usd))
