from flask import Flask
from flask_restful import Api, Resource
import json

"""nonrecn2w
---------
    This is an implementation of a number to words program. It converts a given number into the word form of 
    that number. For example, if the number is 1234, the program will output one thousand, two hundred thirty four.
    The program utilizes flask's built-in development server to display the result of number to words conversion on 
    a webpage. A similar implementation of this program can be found in nonrecn2w.py . The nonrecn2w.py implementation 
    doesn't have any recursive calls in it's conversion methods (n2w_lt3 and n2w).

classes
------- 
    N2WClass
        contains all the methods needed to convert a given number into it's word form.
"""

class N2WClass() :
    """ A class that contains all the methods needed to convert a number into words. Note this class only contains class attributes.
        It has no instance attributes.

    Attributes
    ---------- 
    words : dict(int : str)
        stores the integer form of a number between 0-20 and the tens places from 30 - 90; Maps these values to strings which
        is the number in word form
    w2 : dict(int : str)
        similar to words except stores the value of num places that have a length of 105 or less. 
    divisor_exponent : dict(int: int)
        provides the divisor for exponent. Needed for divby var in n2w functions.

    Methods
    ------- 
    n2w_lt3 (nmbr,lngth)
        Used to convert numbers that have a length less than or equal to 3
    n2w (nmbr,lngth)
        Used to convert numbers that have a length greater than 3
    inscomma (nmbr,lngth)
        Inserts a comma into the number passed in.
    validrun (nmbr)
        Validates the input and invokes the n2w method with validated input.
    fact (n)
        A method for finding the factorial of the number (n) that is passed in.
    """
    #Dictionary of numbers between 1-19 as well as tens places for numbers under 100
    words = {
        0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'
        , 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifeteen', 16: 'sixteen', 17: 'seventeen'
        , 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty'
        , 70: 'seventy', 80: 'eighty', 90: 'ninety'
    }

    #Dictionary of num places for numbers that have a length of 105 or less.
    w2 = {
        3: 'hundred'
        , 4: 'thousand', 5: 'thousand', 6: 'thousand'
        , 7: 'million', 8: 'million', 9: 'million'
        , 10: 'billion', 11: 'billion', 12: 'billion'
        , 13: 'trillion', 14: 'trillion', 15: 'trillion'
        , 16: 'Quadrillion', 17: 'Quadrillion', 18: 'Quadrillion'
        , 19: 'Quintillion', 20: 'Quintillion', 21: 'Quintillion'
        , 22: 'Sextillion', 23: 'Sextillion', 24: 'Sextillion'
        , 25: 'Septillion', 26: 'Septillion', 27: 'Septillion'
        , 28: 'Octillion', 29: 'Octillion', 30: 'Octillion'
        , 31: 'Nonillion', 32: 'Nonillion', 33: 'Nonillion'
        , 34: 'Decillion', 35: 'Decillion', 36: 'Decillion'
        , 37: 'Undecillion', 38: 'Undecillion', 39: 'Undecillion'
        , 40: 'Duodecillion', 41: 'Duodecillion', 42: 'Duodecillion'
        , 43: 'Tredecillion', 44: 'Tredecillion', 45: 'Tredecillion'
        , 46: 'Quattuordecillion', 47: 'Quattuordecillion', 48: 'Quattuordecillion'
        , 49: 'Quindecillion', 50: 'Quindecillion', 51: 'Quindecillion'
        , 52: 'Sexdecillion', 53: 'Sexdecillion', 54: 'Sexdecillion'
        , 55: 'Septendecillion', 56: 'Septendecillion', 57: 'Septendecillion'
        , 58: 'Octodecillion', 59: 'Octodecillion', 60: 'Octodecillion'
        , 61: 'Novemdecillion', 62: 'Novemdecillion', 63: 'Novemdecillion'
        , 64: 'Vigintillion', 65: 'Vigintillion', 66: 'Vigintillion'
        , 67: 'Unvigintillion', 68: 'Unvigintillion', 69: 'Unvigintillion'
        , 70: 'Duovigintillion', 71: 'Duovigintillion', 72: 'Duovigintillion'
        , 73: 'Trevigintillion', 74: 'Trevigintillion', 75: 'Trevigintillion'
        , 76: 'Quattuorvigintillion', 77: 'Quattuorvigintillion', 78: 'Quattuorvigintillion'
        , 79: 'Quinvigintillion', 80: 'Quinvigintillion', 81: 'Quinvigintillion'
        , 82: 'Sexvigintillion', 83: 'Sexvigintillion', 84: 'Sexvigintillion'
        , 85: 'Septenvigintillion', 86: 'Septenvigintillion', 87: 'Septenvigintillion'
        , 88: 'Octovigintillion', 89: 'Octovigintillion', 90: 'Octovigintillion'
        , 91: 'Nonvigintillion', 92: 'Nonvigintillion', 93: 'Nonvigintillion'
        , 94: 'Trigintillion', 95: 'Trigintillion', 96: 'Trigintillion'
        , 97: 'Untrigintillion', 98: 'Untrigintillion', 99: 'Untrigintillion'
        , 100: 'Duotrigintillion', 101: 'Duotrigintillion', 102: 'Duotrigintillion'
        , 103: 'Googol', 104: 'Googol', 105: 'Googol'
    }

    #divisor for exponent. Needed for divby var in n2w functions
    divisor_exponent = {
        1: 0, 2: 1, 3: 2
        , 4: 3, 5: 3, 6: 3
        , 7: 6, 8: 6, 9: 6
        , 10: 9, 11: 9, 12: 9
        , 13: 12, 14: 12, 15: 12
        , 16: 15, 17: 15, 18: 15
        , 19: 18, 20: 18, 21: 18
        , 22: 21, 23: 21, 24: 21
        , 25: 24, 26: 24, 27: 24
        , 28: 27, 29: 27, 30: 27
        , 31: 30, 32: 30, 33: 30
        , 34: 33, 35: 33, 36: 33
        , 37: 36, 38: 36, 39: 36
        , 40: 39, 41: 39, 42: 39
        , 43: 42, 44: 42, 45: 42
        , 46: 45, 47: 45, 48: 45
        , 49: 48, 50: 48, 51: 48
        , 52: 51, 53: 51, 54: 51
        , 55: 54, 56: 54, 57: 54
        , 58: 57, 59: 57, 60: 57
        , 61: 60, 62: 60, 63: 60
        , 64: 63, 65: 63, 66: 63
        , 67: 66, 68: 66, 69: 66
        , 70: 69, 71: 69, 72: 69
        , 73: 72, 74: 72, 75: 72
        , 76: 75, 77: 75, 78: 75
        , 79: 78, 80: 78, 81: 78
        , 82: 81, 83: 81, 84: 81
        , 85: 84, 86: 84, 87: 84
        , 88: 87, 89: 87, 90: 87
        , 91: 90, 92: 90, 93: 90
        , 94: 93, 95: 93, 96: 93
        , 97: 96, 98: 96, 99: 96
        , 100: 99, 101: 99, 102: 99
        , 103: 102, 104: 102, 105: 102
    }

    def n2w_lt3(self, nmbr, lngth):
        """ For numbers that are less than or equal to length 3. Takes in two int parameters
            nmbr, and lngth. This method makes a recursive call.

        Args:
            nmbr (int): the number passed in
            lngth (int): length of the number passed in

        Returns:
            str: the number passed in is converted into words
        """
        if nmbr < 20:
            return self.words.get(nmbr)
        else:
            #int that store num that nmbr will be divided by in divmod operation
            divby = 10 ** self.divisor_exponent.get(lngth)
            x = divmod(nmbr, divby)
            if lngth > 2:
                return (self.words.get(x[0]) + ' ' + self.w2.get(lngth) + ' ' + self.n2w_lt3(x[1], lngth - 1))
            else:
                return (self.words.get(x[0] * 10) + ' ' + self.words.get(x[1]))


    def n2w(self, nmbr, lngth):
        """ For numbers that are greater than length 3. Takes in two int parameters
            nmbr, and lngth. This method makes a recursive call. Also calls n2w_lt3 if 
            lngth is less than 4

        Args:
            nmbr (int): the number passed in
            lngth (int): length of the number passed in

        Returns:
            str: the number passed in is converted into words
        """
        if lngth < 4:
            return self.n2w_lt3(nmbr, lngth)

        #int that store num that nmbr will be divided by in divmod operation
        divby = 10 ** self.divisor_exponent.get(lngth)
        x = divmod(nmbr, divby)
        if x[0] < 10:
            word_str = self.words.get(x[0])
        elif x[0] < 100:
            word_str = self.n2w_lt3(x[0], 2)
        else:
            word_str = self.n2w_lt3(x[0], 3)

        return word_str + ' ' + self.w2.get(lngth) + ', ' + self.n2w(x[1], len(str(x[1])))

    def inscomma(self,nmbr):
        """ Inserts a comma into a number. For example if the number 12345 is passed in the mehtod will
            return 12,345

        Args:
            nmbr (str): the number passed in as a string.

        Returns:
            str: returns the number passed in with appropriate comma placement
        """
        lngth = len(nmbr)
        if lngth < 4:
            return nmbr
        qr = divmod(lngth, 3)

        if qr[1] == 0:
            firstpos = 3
        else:
            firstpos = qr[1]

        lastpos = lngth - 3

        ctr1 = 0
        ctr2 = 0
        cnmbr = ''
        for i in nmbr:
            cnmbr = cnmbr + i
            ctr1 += 1
            ctr2 += 1
            if ctr1 == firstpos:
                cnmbr = cnmbr + ','
                print(f'ctr1 : {ctr1} cnmbr: {cnmbr} firstpos: {firstpos}')
                ctr2 = 0
            else:
                print(f'ctr2 : {ctr2} cnmbr: {cnmbr} lastpos: {lastpos}')

                if ctr2 % 3 == 0 and ctr2 < lastpos:
                    cnmbr = cnmbr + ','
        return cnmbr

    def validrun(self,nmbr) :
        """ It validates the input and passes the validated input into n2w.

        Args:
            nmbr (str): The number that is passed in

        Returns:
            str: returns a string that shows the user that their inputed number has
            been converted into words. If the input is invalid it generates an appropiate
            error message.
        """
        try:
            nbr = int(nmbr)
        except:
            return 'Only numbers are allowed!'
        lngth = len(nmbr)
        if lngth > 105:
            return f'Length of the number is {lngth} digits! It is out of range!'
        if nbr < 0:
            return 'negative numbers not allowed!'
        if nbr == 0:
            return 'zero'
        cnmbr = self.inscomma(nmbr)
        nmbrstr = self.n2w(int(nmbr), len(nmbr))

        return f"There are {lngth} digits in your number! {cnmbr} : {nmbrstr}"

    def fact(self,n) :
        """ Takes the integer n that is passed in and return the result of n factorial(n!)

        Args:
            n (_int_): The integer passed in

        Returns:
            int: returns n factorial or n!
        """
        if n < 0:
            return 'Factorial not defined for negative numbers'
        elif n <= 1:
            return 1
        else :
            x = 1
            i = 1
            while i <= n:
                x = x * i
                i += 1
            return x

if __name__ == '__main__':

    n2wfuncs = N2WClass()

    class RunFact(Resource):
        def get(self, nmbr):
            return n2wfuncs.fact(int(nmbr))


    class RunN2W(Resource):
        def get(self, nmbr):
            return n2wfuncs.validrun(nmbr)

    app = Flask(__name__)
    api = Api(app)

    api.add_resource(RunN2W, '/n2w/<nmbr>')
    api.add_resource(RunFact, '/fact/<nmbr>')

    app.run()
