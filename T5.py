###5. Pascal's Triangle
def generate1(numRows):
        def g(ls):
            res = [1]
            left = 1
            for i in range(1,len(ls)):
                res.append(left+ls[i])
                left = ls[i]
            res.append(1)
            return res
        
        res = []
        if numRows < 3:
            if numRows == 0:
                return res
            for i in range(1,numRows+1):
                res.append([1]*i)
        else:
            res.append([1])
            res.append([1,1])
            
            for i in range(2,numRows):
                res.append(g(res[i-1]))
        return res