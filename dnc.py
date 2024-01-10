

def dnc(baseFunc, combineFunc):
    def newFunc(arr):
        n = len(arr)
        if n==1:
            return baseFunc(arr[0])
        return combineFunc(newFunc(arr[0:n//2]),newFunc(arr[n//2,n]))
    return newFunc


def maxAreaHist(hist):
    pass
