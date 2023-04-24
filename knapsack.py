from ortools.algorithms import pywrapknapsack_solver

#read input file 
def read_data():
    values=[]
    weights=[]
    capacities=[]
    with open("kplib\\00Uncorrelated\\n00050\\R01000\\s001.kp") as rf:
        a=rf.readlines()
        capacities=int(a[2])
        for i in range(4,int(a[1])+4):
            x,y=a[i].split()
            values.append(int(x))
            weights.append(int(y))
    return [capacities],values,[weights]

#write solver to file output
def write_data():
    pass

def main():
    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')
    capacities,values,weights=read_data()
    # values = [
    #     845, 758, 421, 259, 512, 405, 784, 304, 477, 584, 909, 505, 282, 756, 
    #     619, 251, 910, 983, 811, 903, 311, 730, 899, 684, 473, 101, 435, 611, 
    #     914, 967, 478, 866, 261, 806, 549, 15, 720, 399, 825, 669, 2, 494, 868,
    #     244, 326, 871, 192, 568, 239, 968
    # ]
    # weights = [[
    #       804, 448, 81, 321, 508, 933, 110, 552, 707, 548, 815, 541, 964, 604,
    #       588, 445, 597, 385, 576, 291, 190, 187, 613, 657, 477, 90, 758, 877, 924, 
    #       843, 899, 924, 541, 392, 706, 276, 812, 850, 896, 590, 950, 580, 451, 661, 
    #       997, 917, 794, 83, 613, 487
    # ]]
    # capacities = [14778]

    solver.Init(values, weights, capacities)
    solver.set_time_limit(1)
    computed_value = solver.Solve()

    packed_items = []
    packed_weights = []
    total_weight = 0
    print('Total value =', computed_value)
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    print('Total weight:', total_weight)
    print('Packed items:', packed_items)
    print('Packed_weights:', packed_weights)


if __name__ == '__main__':
    main()