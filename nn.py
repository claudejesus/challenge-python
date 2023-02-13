niyigabaclaujesus@gmail.com
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Here is a sample implementation of the code in Python:

scss
Copy code
def average_marks(dictionary, name):
    marks = dictionary[name]
    return round(sum(marks) / len(marks), 2)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{:.2f}".format(average_marks(student_marks, query_name)))
This code first defines the average_marks function which takes in a dictionary of student names and their marks, and a name of a student. It then calculates the average of the marks array for the student and returns the result rounded to 2 decimal places.

In the main section of the code, it first reads in the number of students from the user. It then loops over the number of students and reads in the name and marks for each student, storing the information in the student_marks dictionary.

Finally, it reads in the name of the student for which the average marks need to be calculated, and calls the average_marks function, passing in the student_marks dictionary and the query_name. The result is then printed with 2 decimal places.