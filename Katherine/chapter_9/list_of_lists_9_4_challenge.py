universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

students = []
tuition = []

def enrollment_stats():
    global students
    global tuition
    for key in universities:
        students.append(key[1])
        tuition.append(key[2])
    x = students, tuition
    return x

def mean(values):
    return sum(values)/len(values)

def median(values):
    values.sort()
    if len(values) % 2 == 0:        
        return (values[int(len(values)/2)]+values[int((len(values)-1)/2)])/2
    else:
        return values[int((len(values)-1)/2)]

enrollment_stats()
print("******************************")
print(f"Total students: {sum(students):,}")
print(f"Total tuition: ${sum(tuition):,} \n")

print(f"Studuent mean: {mean(students):,.2f}")
print(f"Student median: {median(students):,} \n")

print(f"Tuition mean: ${mean(tuition):,.2f}")
print(f"Tuition median: ${median(tuition):,} \n")
print("******************************")