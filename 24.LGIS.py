""" 
Problem:

A subsequence of a permutation is a collection of elements of the permutation in the order that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease. For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.

Given: A positive integer n≤10000 followed by a permutation ππ of length nn.

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

"""


def lis(o, a, b, c):
        M = [None] * l   
        P = [None] * l


        
        L = 1
        M[0] = 0

        for i in range(a, b, c):
                lower = 0
                upper = L
                if int(o[M[upper-1]]) < int(o[i]):
                    j = upper

                else:
                    while upper - lower > 1:
                        mid = (upper + lower) // 2
                        if int(o[M[mid-1]]) < int(o[i]):
                            lower = mid
                        else:
                            upper = mid

                    j = lower    

                P[i] = M[j-1]

                if j == L or int(o[i]) < int(o[M[j]]):
                    M[j] = i
                    L = max(L, j+1)

        result = []
        pos = M[L-1]
        for _ in range(L):
                result.append(o[pos])
                pos = P[pos]

        return(" ".join(result))

        

a = open("in_24.txt","r").read().split('\n')

o= a[1].split(" ")
l= int(a[0])

print(lis(o, 1, l, 1)[::-1])  

print(lis(o, l-1, 1, -1)) 
