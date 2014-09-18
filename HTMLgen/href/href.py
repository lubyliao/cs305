class Href:

    """The only difference between this and the previous version is that it
    uses default arguments.

    The definition of the initilizer remains hard to write and ugly,
    but it becomes so much easier to call, because client code can omit
    any arguments that it does not use.

    The structure of the Href objects created using both versions remain unchanged.

    Note that similar to Java, all Href instances have the same set
    and same number of attributes, even when some are not being used.

    Can this be avoided?  That is, is it possible for an instance to not have an
    attribute that it does not really need, such as target?

    """

    def __init__(self,
                 target=None,
                 onClick=None,
                 onMouseOver=None,
                 onMouseOut=None,
                 url='http://www.sandiego.edu',
                 text='USD'):
        self.target = target
        self.onClick = onClick 
        self.onMouseOver = onMouseOver
        self.onMouseOut = onMouseOut 
        self.url = url
        self.text = text

    def __str__(self):
        s = ['<A HREF="%s"' % self.url]
        if self.target: s.append(' TARGET="%s"' % self.target)
        if self.onClick: s.append(' onClick="%s"' % self.onClick)
        if self.onMouseOver: s.append(' onMouseOver="%s"' % self.onMouseOver)
        if self.onMouseOut: s.append(' onMouseOut="%s"' % self.onMouseOut)
        s.append('>%s</A>' % self.text)
        return ''.join(s)

usd = Href(text='UCSD',
            url='http://ucsd.edu',
            target='_blank')

print(usd)
