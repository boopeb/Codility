# First code will be updated with more details. 
def solution(N):
    # write your code in Python 2.7
    aa = []
    aa = bin(N)[2:]
    max_gap = 0
    current_gap = 0
    for x in aa:
        #print x
        #print type(x)
        if x == "0":
            current_gap = current_gap + 1 
           # print current_gap
        else:
            if x == "1":
                max_gap = max(current_gap, max_gap)
                current_gap = 0
                
    return max_gap
