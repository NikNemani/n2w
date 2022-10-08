
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
# ctr = 0
# ctr2 = 3
# for i in range(1,106):
#     if i<=3:
#         divisor_exponent[i] = i-1
#     else:
#         divisor_exponent[i] = ctr2
#         ctr += 1
#         if ctr % 3 == 0:
#             ctr2 += 3

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

#For numbers that are less than or equal length 3. Takes in one int parameter
# num
def numtol3(num):
    number = str(num)
    nword = ""
    length = len(number)
    while length > 1 and num > 20:
        divn = 10 ** divisor_exponent.get(length)
        nplace = divmod(num,divn)
        if length == 3:
            nword += words[nplace[0]] + " " + w2[length] + " "
            num = nplace[1]
            length = len(str(num))
        else:
            nword += words[nplace[0]*10]
            num = nplace[1]
            length = len(str(num))
    return nword + " " +words[num]


#For numbers that are greater than 3. Takes in one int parameter
# num
def n2w(num):
    number = str(num)
    nword = ""
    length = len(number)
    while length > 1 and num > 20:
        divn = 10 ** divisor_exponent.get(length)
        nplace = divmod(num,divn)
        if length >=3:
            nword += numtol3(nplace[0]) + " " + w2[length] + " "
            num = nplace[1]
            length = len(str(num))
        else:
            nword += words[nplace[0]*10]
            num = nplace[1]
            length = len(str(num))

    return nword + " " + words[num]


def main():
    while True:
        user_num = input("Enter a number: ").lower()
        if user_num == 'q':
            break
        try:
            num = int(user_num)
        except:
            print('Only numbers are alowed!')
            continue
        length = len(user_num)
        if length > 105:
            print('number out of range!')
            continue
        if num < 0:
            print('negative numbers not allowed!')
            continue
        if num == 0:
            print('zero')

        print(n2w(num))
        print("Your number is " + " " + str(len(user_num)) + " digits long")
main()