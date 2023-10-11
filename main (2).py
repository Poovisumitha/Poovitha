Unit 3 
Challenge 1
def linear_search_product(product_list, target_product):
    indices = []
    for i in range(len(product_list)):
        if product_list[i] == target_product:
            indices.append(i)
    return indices

# Sample usage
if __name__ == "__main__":
    products = ["apple", "banana", "orange", "apple", "grape"]
    target = "apple"
    result = linear_search_product(products, target)
    print(result)￼Not
  Challenge 2
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the list of students based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function
if __name__ == "__main__":
    # Create a list of student objects
    students = [
        Student("Alice", "S001", 3.9),
        Student("Bob", "S002", 3.7),
        Student("Charlie", "S003", 4.0),
        Student("David", "S004", 3.5),
    ]

    # Sort the list of students by CGPA
    sorted_students = sort_students(students)

    # Print the sorted list
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
