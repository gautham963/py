def print_formatted(number):
    ln = len(bin(n)[2:])
    for i in range(1,n+1):
        oc = oct(i)[2:]
        
        hx = hex(i)[2:]
        hx = hx.upper()
        
        bn = bin(i)[2:]
        
        num = str(i)
        
        print(num.rjust(ln," "),oc.rjust(ln," "),hx.rjust(ln," "),bn.rjust(ln," "))
        #print(' {}  {}  {}  {}'.format(i,oc,hx,bn))
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
