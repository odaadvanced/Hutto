universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849,],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(university):
    student_enrollment = []
    tuition_enrollment = []
    for num in university:
        student_enrollment.append(num[1])
        tuition_enrollment.append(num[2])
    return_lists = [student_enrollment, tuition_enrollment]
    return return_lists

total_students = enrollment_stats(universities)[0]
total_tuition = enrollment_stats(universities)[1]
print(f"{'*' * 30}")
print(f"Total students:   {sum(total_students):,}")
print(f"Total tuition:  $ {sum(total_tuition):,}\n")

def mean(set):
    average_number = sum(set) / len(set)
    return average_number

def median(set):
    set.sort()
    if len(set) % 2 != 0:
        position = round(len(set)/2)
        if position % 2 == 0:
            median_number = set[position-1]
        else:
            median_number = set[position]
    else:
        position = int(len(set)/2)
        sum_of_middle_two = set[position-1] + set[position]
        median_number = sum_of_middle_two/2
    return median_number


print(f"Student mean:     {mean(total_students):,.2f}")
print(f"Student median:   {int(median(total_students)):,}\n")

print(f"Tuition mean:   $ {mean(total_tuition):,.2f}")
print(f"Tuition median: $ {int(median(total_tuition)):,}")
print(f"{'*' * 30}")