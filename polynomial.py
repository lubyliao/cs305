"""

Implement a data type named Polynomial such that 

 -- it is easy to specify the polynomial to be constructed, 
    for example it should be easy to create x^100 - 2.5 x^2 + 3 

 -- it provides a string representation of a polynomial that is similar to the way 
    the polynomial is normally written.  For example, 3 x^4 - 2.3 x^2 + 0.1 x + 7

 -- a method is provided to compute the derivative of a polynomial

 -- client code can write/compute the sum of two polynomials p and q
    with the expression p+q

In addition,

 -- given a plynomial p, the expression p(v) evaluates p at v.  For example, p(3)
    evaulates p at 3 and returns this value

"""

from numbers import Number

def nomial(coeff, exponent):
    """ 
    A helper function:
    Given coeff and exponent, this function produces 
    a text resentatioln of the nomial.
    For example, nomial(2,3) returns the string "2 x**3"
    """

    if coeff == 0:              # Zen of Python: flat is better than nested
        return "0"
    if exponent == 0:
        return str(coeff)
    if exponent == 1:
        if coeff == 1:
            return "x" 
        else:
            return "%s x" % coeff
    else:
        if coeff == 1:
            return "x**%s" % exponent
        else:
            return "%s x**%s" % (coeff, exponent)

class polynomial:
    def __init__(self, *args):
        d = self.coeff = {}
        exponents = self.exponent = set() # intrinstically, the set of exponents is part of the representation
                                          # of a polynomial
        if args:                          # if non-empty
            for coeff, exponent in args:  # Zen of Python: flat is better than nested
                if not isinstance(coeff, Number):
                    raise RuntimeError("Coefficient must be numbers!")
                if (type(exponent) != int) or (exponent < 0):
                    raise RuntimeError("Exponent must be non-negative integer!")
                if coeff == 0: continue
                if exponent not in exponents:
                    exponents.add(exponent)
                    d[exponent] = coeff
                else:
                    d[exponent] += coeff
        self.get_rid_of_zero_coeffs()


    def get_rid_of_zero_coeffs(self):
        d = self.coeff
        exponents = self.exponent
        non_zero_terms = [exponent for exponent in d if d[exponent] != 0]
        set_of_non_zero_terms = set(non_zero_terms)
        if set_of_non_zero_terms < exponents:
            zero_terms = exponents - set_of_non_zero_terms
            for exponent in zero_terms:
                del d[exponent]
            self.exponent = set_of_non_zero_terms
        if not self.exponent:
            self.exponent = set([0])
            self.coeff = {0:0}

    put_in_canonical_form = get_rid_of_zero_coeffs # useful alise
            
    def __str__(self):
        exponents = self.exponent
        coeff = self.coeff
        terms_list = list(exponents)
        terms_list.sort()
        terms_list.reverse()
        terms = [nomial(coeff[exponent], exponent) for exponent in terms_list]
        poly = " + ".join(terms)
        poly = poly.replace("+ -", "- ")
        return poly

    def derivative(self):
        exponent = self.exponent
        coeff = self.coeff
        if 0 in exponent:
            exponent = exponent - {0}
            
        new_coeff = {}
        for exp in exponent:
            new_coeff[exp - 1] = exp * coeff[exp]

        p = polynomial()
        p.exponent = set([n - 1 for n in exponent])
        p.coeff = new_coeff
        p.put_in_canonical_form()
        return p

    def __add__(self, other):
        exp1 = self.exponent
        exp2 = other.exponent
        coeff1 = self.coeff
        coeff2 = other.coeff
        coeff = {}
        for exp in (exp1 - exp2):
            coeff[exp] = coeff1[exp]
        for exp in (exp2 - exp1):
            coeff[exp] = coeff2[exp]
        for exp in (exp1 & exp2):
            coeff[exp] = coeff1[exp] + coeff2[exp]
        p = polynomial()
        p.exponent = exp1 | exp2
        p.coeff = coeff
        p.get_rid_of_zero_coeffs()
        return p

    def __call__(self, x):
        coeff = self.coeff
        total = 0
        for exponent in coeff:
            total += coeff[exponent] * x ** exponent
        return total

if __name__ == '__main__':
    p = polynomial()
    q = polynomial((1,2), (-3,2), (100.34, 100)) # etc
