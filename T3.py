###3. Remove Duplicates from Sorted Array II
class Solution:
def removeDuplicates2(A):  
        n = len(A)  
        if n <= 2 :  
            return n  
        index = 2  
        for i in xrange(2,n):  
            if A[i] != A[index-2]:  
                A[index] = A[i]  
                index += 1  
              
        A = A[:index]  
        return len(A)  