import msvcrt
import os

from HashTable import HashTable
from Student import Student
from Trie import Trie


def addStudent():
    """
    gets input from user and add a student to Trie and Hashtable
    :return: Nothing
    """
    name = input("Name: ")
    number = input("Number: ")
    gpa = input("GPA: ")
    field = input("Field: ")
    student = Student(name, number, gpa, field)
    if t.insert(number, student):
        ht.insert(student)
        print(name, "added successfully.")
    else:
        print("student number is not valid.")


def deleteStudent(s, number):
    """
    deletes a student with given hashcode and student's ID
    :param s: student's hash code
    :param number: student's ID
    :return: Nothing
    """
    t.remove(t.root, number)
    ht.remove(s, number)


def editStudent(s, number):
    """
    gets new information. deletes and insert again new student
    :param s: student's hash code
    :param number: student's ID
    :return: Nothing
    """
    nname = input("New Name: ")
    nnumber = input("New Number: ")
    ngpa = input("New GPA: ")
    nfield = input("New Field: ")

    deleteStudent(s, number)
    student = Student(nname, nnumber, ngpa, nfield)
    if t.insert(nnumber, student):
        ht.insert(student)
        print(nname, "edited successfully.")
    else:
        print("new student number is not valid.")


def searchStudent():
    """
    search for a student in Trie and show student's dialog
    :return: Nothing
    """
    os.system("cls")
    print("Input Number: ")
    print("Press q to abort\nPress enter if you done typing")
    keyin = msvcrt.getwch()
    if keyin == 'q':
        print("Searching Aborted.")
        return
    state, s, hashID = t.search(keyin)
    os.system("cls")
    for k in s:
        print(k)
    while 1:
        print("Input Number:", keyin)
        print("Press q to abort\nPress enter if you done typing")
        keyinnow = msvcrt.getwch()
        if keyinnow == 'q':
            print("Searching Aborted.")
            return
        elif keyinnow == '\x08':
            keyin = keyin[:-1]
        elif keyinnow == '\r':
            break
        else:
            keyin += keyinnow
        os.system("cls")
        state, s, hashID = t.search(keyin)
        for j in s:
            print(j)
    number = keyin
    state, s, hashID = t.search(number)
    if state == 1:
        student = ht.getIndex(hashID, number)
        inp1 = 0
        while inp1 != 4:
            inp1 = int(input("1. View Student\n2. Delete Student\n3. Edit Student\n4. Exit\n"))
            if inp1 == 1:
                print("Name:", student.data.name)
                print("Number:", student.data.number)
                print("GPA:", student.data.gpa)
                print("Field:", student.data.field)
            if inp1 == 2:
                deleteStudent(hashID, number)
                break
            if inp1 == 3:
                editStudent(hashID, number)
                break
    else:
        print("student doesn't exist.")


t = Trie()
ht = HashTable()
inp = 0
while inp != 3:
    inp = int(input("1. Add Student\n2. Search Student\n3. Exit\n"))
    if inp == 1:
        addStudent()
    if inp == 2:
        searchStudent()
