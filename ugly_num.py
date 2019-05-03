class Sol:
    def ugly_num(self,num):
        while num%2==0:
            num//=2
        while num%3==0:
            num//=3
        while num%5==0:
            num//=5
        if num==1:
            return True
        return False
if __name__ == '__main__':
    p1=Sol()
    print(p1.ugly_num(21))
