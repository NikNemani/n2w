from flask import Flask
from flask_restful import Api, Resource
import json

"""
nonrecn2w
---------
    This is an implementation of a number to words program.The program is similar to num2words.py with a few minor differences. 
    One differnce is that it implements the two conversion functions nonrecursively (numtol3 and n2w).It also does not include 
    the factorial function. Other than that it works exactly same.

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
    numtol3 (num)
        Used to convert numbers that have a length less than or equal to 3
    n2w (num)
        Used to convert numbers that have a length greater than 3
    inscomma (nmbr,lngth)
        Inserts a comma into the number passed in.
    validrun (nmbr)
        Validates the input and invokes the n2w method with validated input.
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

    def numtol3(self, num):
        """ For numbers that are less than or equal to length 3. Takes in one int parameter num

        Args:
            num (int): the number passed in
        Returns:
            str: the number passed in is converted into words
        """
        number = str(num)
        nword = ""
        length = len(number)
        while length > 1 and num > 20:
            divn = 10 ** self.divisor_exponent.get(length)
            nplace = divmod(num,divn)
            if length == 3:
                nword += self.words[nplace[0]] + " " + self.w2[length] + " "
                num = nplace[1]
                length = len(str(num))
            else:
                nword += self.words[nplace[0]*10]
                num = nplace[1]
                length = len(str(num))
        return nword + " " + self.words[num]


    def n2w(self, num):
        """ For numbers that are greater than length 3. Takes in two int parameters
            nmbr, and lngth. Also calls numtol3 if lngth is less than 4

        Args:
            num (int): the number passed in
        Returns:
            str: the number passed in is converted into words
        """
        number = str(num)
        nword = ""
        length = len(number)
        while length > 1 and num > 20:
            divn = 10 ** self.divisor_exponent.get(length)
            nplace = divmod(num,divn)
            if length >=3:
                nword += self.numtol3(nplace[0]) + " " + self.w2[length] + " "
                num = nplace[1]
                length = len(str(num))
            else:
                nword += self.words[nplace[0]*10]
                num = nplace[1]
                length = len(str(num))

        return nword + " " + self.words[num]


    def inscomma(self, nmbr):
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
        nmbrstr = self.n2w(int(nmbr))

        return f"There are {lngth} digits in your number! {cnmbr} : {nmbrstr}"



if __name__ == '__main__':
    n2wfuncs = N2WClass()

    class RunN2W(Resource):
        def get(self, nmbr):
            return n2wfuncs.validrun(nmbr)

    app = Flask(__name__)
    api = Api(app)

    api.add_resource(RunN2W, '/n2w/<nmbr>')

    app.run()



