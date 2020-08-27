def read_file():
    a_file = open("data.txt", "r")

    list_of_lists = []
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        int_list = []
        for el in line_list:
            int_list.append(int(el))
        list_of_lists.append(int_list)

    a_file.close()
    return list_of_lists


def knapsack(items, values, item_weight, weight):
    # items and weight are integers. values and item_weight are two arrays
    solution_set = [[0 for k in range(weight + 1)] for l in range(items + 1)]
    for i in range(1,items + 1):
        for j in range(1,weight + 1):
            if j - item_weight[i - 1] >= 0:
                solution_set[i][j] = max(solution_set[i-1][j], values[i - 1] + solution_set[i-1][j - item_weight[i - 1]])
            else:
                solution_set[i][j] = solution_set[i-1][j]

    sol_list = []
    size_of_list = 0
    weight_left = weight
    for num in range(items, 0, -1):
        if solution_set[num][weight_left] > solution_set[num - 1][weight_left]:
            sol_list.append(num)
            size_of_list += 1
            weight_left = weight_left - item_weight[num - 1]
    return solution_set[items][weight], sol_list


def main():
    user_input = int(input("Enter the capacity: "))
    source = read_file()
    item_values = []
    item_weights = []
    items = len(source)
    for list in source:
        item_values.append(list[1])
        item_weights.append(list[0])
    solution = knapsack(items, item_values, item_weights, user_input)
    print("The maximal value is: " + str(solution[0]))
    print("Optimal subset is: " + str(solution[1]))

if __name__ == '__main__':
    main()