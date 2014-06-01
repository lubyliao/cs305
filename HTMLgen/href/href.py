class Href:

    """The first Href class.  Totally strightforward.  Totally boring.
    The only kind you can write in Java. """

    def __init__(self,
                 target,
                 onClick,
                 onMouseOver,
                 onMouseOut,
                 url,
                 text):
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

A = Href

link = Href(None,
            None,
            None,
            None,
            url = 'http://www.sandiego.edu',
            text = 'USD')


print link
