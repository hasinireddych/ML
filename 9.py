from tkinter import N, W


students=input("enter the weights in lbs") # input weights in lbs
N=students.split() #splitting them to get a list from the input data
N= [int(item) for item in N] # converting the list items into intergers
print(N) # list woth intergers

weight_list=[] # new list for converting into kgs
for i in N: # for looping
    n=i* 0.45 # formula for converting ponds into kgs
    weight_list.append(n)
print(weight_list)  # new list after converiosn