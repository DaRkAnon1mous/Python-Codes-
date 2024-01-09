class LenVal():
    def __init__(self , a):
        self.LenV = len(a)
    def sho_val(self):
        print(self.LenV)

l = LenVal('Head')
l.sho_val()
l = LenVal([ 1, 9, 4, 2, 6])
l.sho_val()
l = LenVal((1, ))
l.sho_val()
