from .Stack_structure import Stack

class divideBy2:
    def divide2(self,decNumber):
        remstack = Stack()

        while decNumber>0:
            rem = decNumber % 2
            remstack.push(rem)
            decNumber = decNumber//2

        binString=''
        while not remstack.isEmpty():
            binString = binString+str(remstack.pop())

        return binString

class BaseConverter:
    def baseConverter(self,decNumber, base):
        digits = "0123456789ABCDEF"

        remstack = Stack()
        while decNumber > 0:
            rem = decNumber % base
            remstack.push(rem)
            decNumber = decNumber // base

        newString = ""
        while not remstack.isEmpty():
            newString = newString + digits[remstack.pop()]

        return newString