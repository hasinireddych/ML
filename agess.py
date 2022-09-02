import statistics
print("Hello World")
ages=[19,22,19,24,20,25,26,24,25,24]
ages.sort() #'sorting the list ages'
print(ages)

print(min(ages))
print(max(ages))
ages.append(min(ages))
ages.append(max(ages))
print(ages) #"adding min and max to the list ages"

med=statistics.median(ages) #"median of the given list using statistics library"
print(med)
averag=statistics.mean(ages) #"finding avg using mean method from statistics"
print(averag)
print(max (ages)- min(ages))