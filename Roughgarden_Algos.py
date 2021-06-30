#Question 1

#In this programming assignment you will implement one or more of the integer multiplication
#algorithms described in lecture. To get the most out of this assignment, your program should
#restrict itself to multiplying only pairs of single-digit numbers.  
#You can implement the grade-school algorithm if you want, 
#but to get the most out of the assignment you'll
#want to implement recursive integer multiplication and/or Karatsuba's
#algorithm.
#So: what's the product of the following two 64-digit numbers?

#3141592653589793238462643383279502884197169399375105820974944592

#2718281828459045235360287471352662497757247093699959574966967627



#Implementing Karatsuba's algorithm

#Helper 1: Check if lengths are equal. If not, equalise.
def Standardise(x,y):
    lx, ly = len(str(x)), len(str(y))
    if lx == ly:
        return x, y, 1
    else:
        if lx - ly > 0:
            diff = 10**(lx - ly)
            z =  diff * y
            return x, z, diff
        else:
            diff = 10**(ly - lx)
            z =  diff * x
            return z, y, diff

#Helper 2: Check if lengths are power of 2. If not, convert accordingly. 
def Evenlength(x,y):
    x, y, diff = Standardise(x,y)
    if len(str(x))%2 != 0:
        x *= 10
        y *= 10
        diff *= 100
        return str(x),str(y),diff
    else:
        return str(x),str(y),diff 

#Note: Since algo doesn't work if no. of digits are not power of 2,
# we are keeping track of 'diff' so that we can use it to
#divide the output by, so that we get the actual result.
 
def Multiply(x,y):
    #Single-digit base cases
    if len(str(x)) == 1 or len(str(y)) == 1: 
        return x * y
    else:
        fx, fy, count = Evenlength(x,y)
        n  = len(fx) 
        a,b,c,d = '','','',''
        length = 0
        while length < n:
            if length < n//2:
                a += fx[length] 
                c += fy[length]
            else:
                b += fx[length]
                d += fy[length]
            length += 1
        a,b,c,d = int(a),int(b),int(c),int(d)
        ac, bd = Multiply(a,c), Multiply(b,d)
        e,f = a + b, c + d
        ef = Multiply(e,f)
        adbcsum = ef - ac - bd

        return ((10**n * ac) + (10**(n//2) * adbcsum) + bd)//count

#Answer: 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184









