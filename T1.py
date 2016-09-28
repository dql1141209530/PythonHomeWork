###1. Remove Element
def removeElement(A, elem):  
        index = 0  
        for num in A:  
            if num != elem:  
                A[index] = num  
                index += 1  
                return index