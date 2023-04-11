universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
    ]

def enrollment_stats(universities):
    index = 0
    list1 = []
    list2 = []
    for list in universities:
        list1.append(universities[index][1])
        list2.append(universities[index][2])
        index = index + 1
    return ([list1, list2])

def mean(list):
    total = sum(list)
    return (total / (len(list)))

def median(list):
    list.sort()
    if len(list) % 2 == 0:
        index1 = int(len(list)/2)
        index2 = index1 + 1
        median = (list[index1] + list[index2]) / 2
    else:
        index = int((len(list) - 1) / 2)
        median = list[index]
    return median
      
total_students = f'{sum(enrollment_stats(universities)[0]):,}'
total_tuition = f'{sum(enrollment_stats(universities)[1]):,}'
student_mean = f'{mean(enrollment_stats(universities)[0]):,.2f}'
student_median = f'{median(enrollment_stats(universities)[0]):,}'
tuition_mean = f'{mean(enrollment_stats(universities)[1]):,.2f}'
tuition_median = f'{median(enrollment_stats(universities)[1]):,}'

print (f"""Total students: {total_students}
Total tuition: ${total_tuition}

Student mean: {student_mean}
Student median: {student_median}

Tuition mean: ${tuition_mean}
Tuition median: ${tuition_median}""")
