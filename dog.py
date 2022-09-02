dog={} #empty dog dictionary
dog={'name':'husky','color':"grey",'breed':"huskyy",'legs':4,'age':5}
print(dog) #prints dog dictionary

student={'first_name':"ganesh",'last_name':"setty",'gender': "male",'age':23,'martial status':"single",'skills':["coding"],
'country': "india",'city': "hyd",'address':"gacchibowli"}
print(student) #"student dictionary"

lenght= len(student) #"length of the student dictionary"  
print(lenght)

skills_value=student.get('skills') #getting skill values by get method
print(skills_value) 

print(type(skills_value)) # type of skill valuse as list

student['skills']=["coding","singing","dance"] #adding values to the skill list
print (student)

keyss_list=list(student.keys())
values_list=list(student.values())
print(keyss_list) #keys as list

print((values_list)) #values as list