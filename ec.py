#Eliza Nip
#CS325
#Extra credit
#0-1 knapsack algorithm

def knapsack(W, itemsList):
    length = len(itemsList)
    B = [[0 for _ in range(W +1)] for _ in range (length+1)]
    for i in range(1, length):
        for j in range(1, W + 1):
            if itemsList[i][0] <= j:
                B[i][j] = max(itemsList[i][0] + B[i-1][j-itemsList[i][0]],B[i-1][j])
            else:
                B[i][j] = B[i-1][j]
    return B[i][j]

def main():
    W = 5
    itemsList = [[2,3],[3,4],[4,5],[5,6]]
    print("Maximal value:",knapsack(W,itemsList))

if __name__ == '__main__':
    main() 
            
            

