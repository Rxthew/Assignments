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
with open ('Quicksort.txt', newline='') as quicklist:
    reader = csv.reader(quicklist, delimiter=' ')
    quick = []
    for row in reader:
        quick.append(int(row[0]))


def quickCompare(array, c):
    #Base case
    if len(array) == 1 or len(array) == 0:
        return array, c
    else:
    #Partition
        i = j = 1
        while j < len(array):
            if array[j] < array[0]:
                array[j], array[i] = array[i], array[j]
                j += 1
                i += 1
            else:
                j += 1
        array[i-1], array[0] = array[0], array[i-1]
    #Recursive Calls
    left, leftc = quickCompare(array[:i-1], len(array[:i-1]))  
    right, rightc = quickCompare(array[i:], len(array[i:]))
    left.append(array[i-1])
    c += leftc + rightc
    return  left + right,  c


#print(quickCompare(quick, 0)[1])
#Answer: 162085    

#Compute the number of comparisons (as in Problem 1), always using the final element of the given array as the pivot element.
#Again, be sure to implement the Partition subroutine exactly as it is described in the video lectures. Recall from the
#lectures that, just before the main Partition subroutine, you should exchange the pivot element (i.e., the last element) 
# with the first element.

def quickCompareSecond(array, c):
        #Base case
    if len(array) == 1 or len(array) == 0:
        return array, c
    else:
        #Swap Pivot
        array[-1], array[0] = array[0], array[-1]
        #Partition
        i = j = 1
        while j < len(array):
            if array[j] < array[0]:
                array[j], array[i] = array[i], array[j]
                j += 1
                i += 1
            else:
                j += 1
        array[i-1], array[0] = array[0], array[i-1]
    #Recursive Calls
        left, leftc = quickCompareSecond(array[:i-1], len(array[:i-1]))  
        right, rightc = quickCompareSecond(array[i:], len(array[i:]))
        left.append(array[i-1])
        c += leftc + rightc
    return  left + right,  c

#print(quickCompareSecond(quick,0)[1])
#Answer: 164123


#Compute the number of comparisons (as in Problem 1), using the "median-of-three" pivot rule.  [The primary motivation behind
#this rule is to do a little bit of extra work to get much better performance on input arrays that are nearly sorted or 
#reverse sorted.]  In more detail, you should choose the pivot as follows.  Consider the first, middle, and final elements of
#the given array.  (If the array has odd length it should be clear what the "middle" element is; for an array with even length
#2 k, use the k^th element as the "middle" element. So for the array 4 5 6 7,  the "middle" element is the second one 
# ---- 5 and not 6!)  Identify which of these three elements is the median (i.e., the one whose value is in between the other two),
#and use this as your pivot.  As discussed in the first and second parts of this programming assignment, be sure to implement 
#Partition exactly as described in the video lectures (including exchanging the pivot element with the first element just before 
# the main Partition subroutine).

#EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), middle (4), and last (1) elements; since 4 is 
#the median of the set {1,4,8}, you would use 4 as your pivot element.

#SUBTLE POINT: A careful analysis would keep track of the comparisons made in identifying the median of the three candidate elements.
#You should NOT do this.  That is, as in the previous two problems, you should simply add m − 1 to your running total of comparisons
#every time you recurse on a subarray with length m.



def choosePivot(array):
    mid = len(array)//2 + len(array)%2 - 1 
    pivots = [array[0], array[mid], array[-1]]
    for i in range(0,2):
        if pivots[i] > pivots[i+1]:
            pivots[i], pivots[i+1] = pivots[i+1], pivots[i]
        if i > 0 and pivots[i] < pivots[i-1]:
            pivots[i-1], pivots[i] = pivots[i], pivots[i-1]
    return pivots[1]


def quickerCompare(array, c):
        #Base case
    if len(array) < 3:
        return quickCompare(array, c)
    else:
        #Choose Pivot
        pivot = choosePivot(array)
        ind = array.index(pivot)
        array[0], array[ind] = array[ind], array[0]
        #Partition
        i = j = 1
        while j < len(array):
            if array[j] < array[0]:
                array[j], array[i] = array[i], array[j]
                j += 1
                i += 1
            else:
                j += 1
        array[i-1], array[0] = array[0], array[i-1]
    #Recursive Calls
        left, leftc = quickerCompare(array[:i-1], len(array[:i-1]))  
        right, rightc = quickerCompare(array[i:], len(array[i:]))
        left.append(array[i-1])
        c += leftc + rightc
    return  left + right,  c

#print(quickerCompare(quick,0)[1])
#Answer: 138382

#Question 4

#Download kargerMinCut.txt

#The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to 200. 
#The first column in the file represents the vertex label, and the particular row (other entries except the first column) 
#tells all the vertices that the vertex is adjacent to. So for example, the 6^th row looks like :
# "6	155	56	52	120	......".  This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with)
# the vertices with labels 155,56,52,120,......,etc

#Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph
#to compute the min cut. 
#(HINT: Note that you'll have to figure out an implementation of edge contractions.
# Initially, you might want to do this naively, creating a new graph from the old every time there's an edge contraction.
# But you should also think about more efficient implementations.)   (WARNING: As per the video lectures, please make sure 
# to run the algorithm many times with different random seeds, and remember the smallest cut that you ever find.)  


#Step 1:  have the interpreter read the data faithfully,

with open ('test.txt',  newline='') as thislist:
    reader = csv.reader(thislist, delimiter="\t" )
    graph = {}
    for row in reader:
        if len(row) > 1:
            graph[int(row[0])] = [int(i) for i in row[1:] if i != '']


#focus on one iteration only for now
#Step 2:  .....

#Let's see:
# 1 2 3 4
# 2 1
# 3 1 4
# 4 1 3

#So we want a function that compares the first column values of two rows
#then iterates through the row values and forms a union of the two sets with distinct elements. 
#(No such thing as self-loops if all elements distinct right?)
#Once this is done. The first column value can be assigned to 'A'. 
#I should think a dictionary is ideal for this sort of procedure.
#Stopping condition when there are only a pair of vertices left (one of which is A). 
# Count crossing edges == the length of the lesser array. 
# Contraction in my first iteration will proceed from the last-most edge in the new array
# Hm. What if there is a node unconnected to anything?   