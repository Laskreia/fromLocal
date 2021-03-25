"""
File: student.py
Resources to manage a student's name and test scores.
----------------------------------
Problem 1. 
Add three methods to the Student class that compare two Student objects. One method should test for equality. 
A second method should test for less than. The third method should test for greater than or equal to. 
In each case, the method returns the result of the comparison of the two students’ names. 
Include a main function that tests all of the comparison operators. 
-----------------------------
"""

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    def __eq__(self, student):
        return (self.name == student.getName())

    def __lt__(self, student):
        return (self.name < student.getName())
        
    def __ge__(self, student):
        return (self.name >= student.getName())

def main():
    student_1 = Student("Zhongli", 3)
    student_2 = Student("Ningguang", 3)
    student_3 = Student("Keqing", 3)

    print("\nTesting for equality")
    print("Result: ", student_1 == student_2) #Should be FALSE
    print("\nTesting for less than")
    print("Result: ", student_3 < student_2) #Should be TRUE

    print("\nTesting for greater than or equal to")
    print("Result: ", student_1 >= student_2) #Should be TRUE
    
if __name__ == "__main__":
    main()


