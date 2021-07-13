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

#Question 2

#Download the IntegerArray.txt. 
#This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
#Your task is to compute the number of inversions in the file given, where the i^th row of the file indicates the i^th entry of an array.
#Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.
#The numeric answer for the given input file should be typed in the space below.

import csv
with open ('IntegerArray.txt', newline='') as intlist:
    reader = csv.reader(intlist, delimiter=' ')
    arr = []
    for row in reader:
        arr.append(int(row[0]))

#Remember: This only works if there are no duplicate integers in the array.


#Base Case Handler.
def baseSortAndInversionCount(x, inversions): #inversions = 0    
    if len(x) == 1:
        return x, inversions
    elif len(x) == 2:
        if x[0] > x[1]:
            y = [x[1],x[0]]
            inversions += 1
            return y, inversions
        else:
            return x, inversions


    
def inversionCounter(somearray, inversions): #inversions = 0
    n = len(somearray)
    if n <= 2:
        return baseSortAndInversionCount(somearray, inversions)
    else:
        half = n//2
        first, firstInversions = inversionCounter(somearray[:half],inversions)
        second, secondInversions = inversionCounter(somearray[half:],inversions)
        final =  []
        i = j = 0
        inversions += firstInversions + secondInversions
        while len(final) < n:
            if i < len(first):
                if j < len(second):
                    if first[i] < second[j]:
                        final.append(first[i])  
                        i += 1
                    else:
                        final.append(second[j])
                        j += 1
                        inversions += len(first)-i
                else:
                    final += first[i:]
                    return final, inversions
            elif j < len(second):
                final += second[j:]
                return final, inversions    
        return final, inversions

#print(inversionCounter(arr,0)[1])
# Answer: 2407905288

#Question 3

# Download Quicksort.txt
#
#The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order.  The integer in the i^th
# row of the file gives you the i^th entry of an input array. Your task is to compute the total number of comparisons used to sort the
# given input file by QuickSort. As you know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask 
# you to explore three different pivoting rules. You should not count comparisons one-by-one.  Rather, when there is a recursive call 
# on a subarray of length m, you should simply add m−1 to your running total of comparisons. (This is because the pivot element is 
# compared to each of the other m−1 elements in the subarray in this recursive call.)
#
# WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can give you 
# differing numbers of comparisons.  For this problem, you should implement the Partition subroutine exactly as it is described 
# in the video lectures (otherwise you might get the wrong answer).

#DIRECTIONS FOR THIS PROBLEM:

#For the first part of the programming assignment, you should always use the first element of the array as the pivot element.

#import csv
with open ('New.txt', newline='') as quicklist:
    reader = csv.reader(quicklist, delimiter=' ')
    quick = []
    for row in reader:
        quick.append(int(row[0]))



def quickCompare(array, length, c):
    #Base case
    if length == 1:
        return c
    else:
    #Partition
        pivot = array[0]
        i = j = array[1]
        while j > length:
            if array[j] < pivot:
                x, y = array[i], array[j]
                array[i], array[j] = y, x
                j += 1
                i += 1
            else:
                j += 1
        x = array[i]
        array[i] = pivot
        array[0] = x
    #ignoring c for now
    left, leftLength = quickCompare(array[:pivot], len(array[:pivot]), #c  )
    right, rightLength = quickCompare(array[pivot + 1:], len(array[pivot + 1:]), #c)
    #return left + pivot + right?

    

