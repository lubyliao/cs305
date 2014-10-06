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
    """ Ported from Robin F's Table class in HTMLgen.py.  Keep all his
    Table attributes.  Minimally rewrite __str__ to make it work with
    Python 3.  How does the __init__ code differ from Robin's code?
    """
    caption_align = 'top'
    border = 2
    cell_padding = 4
    cell_spacing = 1
    width = '100%'
    heading = None
    heading_align = 'center'
    heading_valign = 'middle'
    body = [['&nbsp;']*3]
    column1_align = 'left'
    cell_align = 'left'
    cell_line_breaks = 1
    colspan = None
    body_color= None
    heading_color=None

    def __init__(self, tabletitle='', **kw):
        self.tabletitle = tabletitle
        HTMLElement.__init__(self, **kw)

    def __str__(self):
        """Generates the html for the entire table.
        """
        if self.tabletitle:
           s = ["<a name='%s'>%s</a><P>" % (self.tabletitle, self.tabletitle)]
        else:
           s = []

        s.append('<TABLE border=%s cellpadding=%s cellspacing=%s width="%s">\n' % \
                (self.border, self.cell_padding, self.cell_spacing, self.width))
        if self.tabletitle:
            s.append('<CAPTION align=%s><STRONG>%s</STRONG></CAPTION>\n' % \
                    (self.caption_align, self.tabletitle))

        for i in range(len(self.body)):
            for j in range(len(self.body[i])):
                if type(self.body[i][j]) == type(''):
                    #process cell contents to insert breaks for \n char.
                    if self.cell_line_breaks:
                        self.body[i][j] = self.body[i][j].replace('\n','<br>')
                    else:
                        self.body[i][j] = Text(self.body[i][j])

        # Initialize colspan property to 1 for each
        # heading column if user doesn't provide it.
        if self.heading:
            if not self.colspan:
                if type(self.heading[0]) == list:
                    self.colspan = [1]*len(self.heading[0])
                else:
                    self.colspan = [1]*len(self.heading)
        # Construct heading spec
        #  can handle multi-row headings. colspan is a list specifying how many
        #  columns the i-th element should span. Spanning only applies to the first
        #  or only heading line.
        if self.heading:
            prefix = '<TR Align=' + self.heading_align + '> '
            postfix = '</TR>\n'
            middle = ''
            if type(self.heading[0]) == type([]):
                for i in range(len(self.heading[0])):
                    middle = middle + '<TH ColSpan=%s%s>' % \
                             (self.colspan[i], \
                              self.get_body_color(self.heading_color,i)) \
                              + str(self.heading[0][i]) +'</TH>'
                s.append(prefix + middle + postfix)
                for i in range(len(self.heading[1])):
                    middle = middle + '<TH>' + str(self.heading[i]) +'</TH>'
                for heading_row in self.heading[1:]:
                    for i in range(len(self.heading[1])):
                        middle = middle + '<TH>' + heading_row[i] +'</TH>'
                    s.append(prefix + middle + postfix)
            else:
                for i in range(len(self.heading)):
                    middle = middle + '<TH ColSpan=%s%s>' % \
                             (self.colspan[i], \
                              self.get_body_color(self.heading_color,i)) \
                              + str(self.heading[i]) +'</TH>'
                s.append(prefix + middle + postfix)
        # construct the rows themselves
        stmp = '<TD Align=%s %s>'
        for row in self.body:
            s.append('<TR>')
            for i in range(len(row)):
                if i == 0 :
                    ss1 = self.column1_align
                else:
                    ss1 = self.cell_align
                s.append(stmp % (ss1, self.get_body_color(self.body_color,i)))
                s.append(str(row[i]))
                s.append('</TD>\n')
            s.append('</TR>\n')
        #close table
        s.append('</TABLE><P>\n')
        return ''.join(s)
    
    def get_body_color(self, colors, i):
        """Return bgcolor argument for column number i
        """
        if colors is not None: 
            try: 
                index = i % len(colors) 
                return ' bgcolor="%s"' % colors[index] 
            except: 
                pass 
        return ''



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

t = Table('Table')
t.heading = ['One', 'Two', 'Three']
t.body = [[1,2,3], [4,5,6]]
print ( t )
print(vars(t))
