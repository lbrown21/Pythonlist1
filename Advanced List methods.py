# task 1

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# task 2

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submitted_set = set(submitted)
attended_set = set(attended)

common_students = submitted_set.intersection(attended_set)
print(common_students)

# task 3

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

both = list(set(submitted) & set(attended))
print(both)

identical = set(submitted) == set(attended)
print(identical)

submitted_set = set(submitted)
attended = [student for student in attended if student in submitted_set]
print(attended)