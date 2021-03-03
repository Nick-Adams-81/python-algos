                 #####      PYTHON ALGORITHIMS!     #####

# LIST EXAMPLES AND LIST FUNCTIONS #                         

courses = ['history', 'Math', 'Science', 'Physical Ed']
print('first list',courses)

# adding a value to our list
courses.insert(0, 'Art')
print('inserting item into our list', courses)

# extending our list with asnother list
courses_2 = ['Music', 'Detention']
courses.extend(courses_2)
print('extending a list with another list', courses)

# removing items from our list
courses.pop()
print('removing an item from our list', courses)

# reversing our list
courses.reverse()
print('reversing our list', courses)

# sorting our list
courses.sort()
print('sorting our list', courses)

#for loop for a list
data = ['hello', 'cruel', 'world']
# basic for loop
for item in data:
    print(item)
# getting the index of a list item in a for loop
for index, item in enumerate(data):
    print(index, item)

# toString method
course_str = ', '.join(courses)



# TUPLE EXAMPLES AND FUNCTIONS #





