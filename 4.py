it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#finding the length of it_companies set
print(len(it_companies))

#adding a value to the it_companies set
it_companies.add('Twitter')
print(it_companies)

#adding multiple companies to it_companies set
it_companiesnew={'TCS','JPMC','EPAM'}
it_companies.update(it_companiesnew)
print(it_companies)

#removing one of the comapnies from it_comapnies set
it_companies.remove('EPAM')
print(it_companies)

'''
#The main difference between remove and discard methods in python is that
#if there is no particular item which i want to remove from the set
#then discard() method will never raise and error, whereas remove method will
#raise error if value specified is not present in the set

#For instance above i have removed company named EPAM by remove() method
#it did so successfully, but i use that method again it will raise an error
#again stating that item could not be found , but on the other hand discard
#mthod will never raise an error, it will print whole set as it is instead.
'''

#Joining A and B
print(A.union(B))

# finding A intersection B
print(A.intersection(B))

#verifying if A is subset of B
print(A.issubset(B))

#verifying if A and B are disjoint sets
print(A.isdisjoint(B))

#joining A with B and B with A
print(A.union(B))
print(B.union(A))

#finding symmetric difference between A and B
print(A.symmetric_difference(B))

#deleting both the sets A and B
A.clear()
print(A)

B.clear()
print(B)

#converting ages to a set
agesintoset=set(age)
print(agesintoset)

#comparing length of list to the set

lengthoflist=len(age)
print(lengthoflist)

lengthofset=len(agesintoset)
print(lengthofset)

'''
#after printing the length of set and list, it can be noticed that length of set
#is less than the list. Because in set duplicate elements will be removed.
'''