"""

Problem:

Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

"""

print("Write down the number of months")

n = int(input())

print("Write down the lifespan")

m = int(input())



t=[1]*n



for x in range (2,n):
        if x < m :
                t[x]=t[x-1]+t[x-2]
        else:
                t[x]=t[x-1]+t[x-2]-t[x-m-1]


        
        
print( t[-1])




