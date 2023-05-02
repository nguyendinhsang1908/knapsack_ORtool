from ortools.algorithms import pywrapknapsack_solver
import os
from wakepy import unset_keepawake,set_keepawake
import time 
set_keepawake(keep_screen_awake=True)

def knapsack(cap,value,weight):
    # Create the solver.
    start_time=time.time()
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')
    capacities=cap
    values=value
    weights=weight
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
    solver.set_time_limit(120)
    solver.Init(values, weights, capacities)

    computed_value = solver.Solve()

    packed_items = []
    packed_weights = []
    total_weight = 0
    # print('Total value =', computed_value)
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    # print('Total weight:', total_weight)
    # print('Packed items:', packed_items)
    # print('Packed_weights:', packed_weights)
    
    # print("time excution:",time.time() - start_time)
    time_excution=time.time()-start_time
    return computed_value,total_weight,packed_items,packed_weights,time_excution

def read_file(path):
    values=[]
    weights=[]
    capacities=[]
    with open(path) as rf:
        a=rf.readlines()
        capacities=int(a[2])
        for i in range(4,int(a[1])+4):
            x,y=a[i].split()
            values.append(int(x))
            weights.append(int(y))
    return  [capacities],values,[weights] 

def main():
    dir_path=os.getcwd()
    dir_path=dir_path+"\\kplib"
    list_kplib=os.listdir(dir_path) #00->012

    for i in list_kplib:
        dir_path_kplib=dir_path+"\\"+i
        list_case=os.listdir(dir_path_kplib)  #vào 00 rồi
        
        for i in list_case:    
            dir_path_0=dir_path_kplib+"\\"+i
            list_case=os.listdir(dir_path_0) # vào n rồi
            
            for i in list_case:
                dir_path_n=dir_path_0+"\\"+i # vào R rồi
                list_case=os.listdir(dir_path_n)
                
                for i in range(9,10):
                    dir_out=dir_path_n.replace("kplib","output") #path output 
                    dir_path_r=dir_path_n+"\\s00"+str(i)+".kp" #path readfile
                    path=dir_out+"\\output"+str(i)+".txt"
                    # print("doc file:",dir_path_r)
                    # print("doc file"+str(i),end="\n")
                    capacities,values,weights=read_file(dir_path_r)
                    print("ghi file:",path)
                    computed_value,total_weight,packed_items,packed_weights,time_excution=knapsack(capacities,values,weights)
                    # print(path)
                    f=open(path,"x")
                    # f.write(str(capacities))
                    # f.write(str(values))
                    # f.write(str(weights))
                    f.write('time knapsack caculate:'+str(time_excution)+'\n')
                    f.write('Total value ='+ str(computed_value)+'\n')
                    f.write('Total weight:'+ str(total_weight)+'\n')
                    f.write('Packed items:'+ str(packed_items)+'\n')
                    f.write('packed_weights:'+str (packed_weights))




if __name__ == '__main__':
    main()
    
unset_keepawake()