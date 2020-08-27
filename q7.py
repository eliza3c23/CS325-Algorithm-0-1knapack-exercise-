#Eliza Nip
#CS325
#Extra credit
#0-1 knapsack algorithm

# W:capacity
def knapsack (W, weight, value, n ):
    # table B: [[cols]rows]
    #Build table solution[cols][rows]
    B = [[0 for x in range(W +1)] for x in range (n + 1)]
    
    # Loop from n1 -> n+1
    for i in range(1,n + 1):
        # Loop from 
        for j in range(1,W + 1):
            if i == 0 or j == 0:
                B[i][j] = 0
            # If item is smaller than j, then item can be part of the solution
            elif weight[i-1] <= j:
                # user max() to return the largest item
                B[i][j] =  max(value[i-1] + B[i-1][j - weight [i-1]], B[i-1][j])
            # It item is too big, can not be part of the solution
            else:
                B[i][j] = B[i-1][j]
    return B[i][j]

def main():
    W = 5
    weight = [2,3,4,5]
    value = [3,4,5,6]
    n = len(value)
    print ("Maximal value:",knapsack(W, weight, value, n))  

if __name__ == '__main__':
    main()