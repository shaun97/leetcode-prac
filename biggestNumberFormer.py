# Given a number n, e.g. 23121; Given a set of numbers A e.g. (2, 4, 9). 
# Form the biggest number from the elements in A that is less than n.

# For this case, the return value is 22999
# n = 1 set = 8, 9

# We will form the digit of the same length with the max of the set
# 2999 set = {2, 9}, 9999
# We will iterate from the left of n, changing each digit to one that is <= the one in n
# 2999 9999, 2 -> 2999
# 2999 set = {1, 9}, 9999 -> 1999 return
# If we used a digit that is less than the ith digit in n, we return immediately
# If not, we add it in and continue.
# case 1: we could find any digit that is less than the one in. n = 1111, set = {9}, res = 9999 res >= n. if it is, we just return 999
# case 2: n = 111 set = {1, 9}
# 2299, [2, 9]

# res = 9999
# res = 2999
# res = 2299

# res = 2299 , n = 2299
# res = 2229
def biggestNumberFormer(n, setOfNo):
    # set -> sort it
    sortedA = list(setOfNo)
    sortedA.sort() # max 9
   # 

    # result
    res = 0

    lengthOfN = 0
    temp = n # -1 to handle the case where all the digits are the same
    while temp:
        res += sortedA[-1] * 10 ** lengthOfN 
        temp //= 10
        lengthOfN += 1

    temp = n

    # iterate from the left 
    while lengthOfN > 0:
        nDigit = temp % (10 ** (lengthOfN))
        nDigit = nDigit // (10 ** (lengthOfN - 1))
        for i in range(len(sortedA) - 1, -1, -1):
            if sortedA[i] > nDigit:
                continue

            res -= sortedA[-1] * (10 ** (lengthOfN - 1))
            res += sortedA[i] * (10 ** (lengthOfN - 1))

            if sortedA[i] < nDigit:
                return res
        lengthOfN -= 1

    res = 0
    lengthOfN = 0
    temp = n // 10 # -1 to handle the case where all the digits are the same
    while temp:
        res += sortedA[-1] * 10 ** lengthOfN
        temp //= 10
        lengthOfN += 1
    return res

print(biggestNumberFormer(11111, [1, 9]))
