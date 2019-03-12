class Rotation:
    def chkRotation(self, A, lena, B, lenb):
        if lena!=lenb:
            return False
        tmp= A+A
        print(tmp)
        if B in tmp:
            return True
        else:
            return False

a= Rotation()
b=a.chkRotation("123",3,'2311',3)
print(b)

#