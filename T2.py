###2. Remove Duplicates from Sorted Arra
def removeDuplicates(nums):  
        l = len(nums)  
        if l == 0:  
            return 0  
        index = 0  
        i = 1  
        nums[index] = nums[0]  
        while i<l:  
            if nums[index] != nums[i]:  
                index += 1  
                nums[index] = nums[i]  
            i += 1  
        return index+1  