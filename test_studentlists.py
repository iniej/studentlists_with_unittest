'''
Practice using
 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn
'''

from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')

    ## TODO write a test that adds and removes a student, and asserts the student is removed
    # Use assertNotIn
    def test_add_and_remove_a_student(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student' , test_class.class_list)

    ## TODO write a test that removes a student not in the list, and asserts a StudentError is raised
    # def test_remove_a_student_not_in_the_list(self)
    def test_remove_a_student_not_in_the_list(self):
        test_class = ClassList(2)
        test_class.add_student('Christopher Columbus')
        test_class.add_student('Adam Smiths')
        with self.assertRaises(StudentError):
            test_class.remove_student('James Brown')

    ## TODO write a test that removes a student from an empty list, and asserts a StudentError is raised
    def test_remove_a_student_from_an_empty_list(self):
        test_class = ClassList(2)
        with self.assertRaises(StudentError):
            test_class.remove_student('James Taylor')


    def test_enrollment_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    ## TODO write a test that adds some example students to an example class, checks
    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Abraham Lincoln')
        test_class.add_student('Victor Ufor')
        self.assertTrue('Abraham Lincoln, Victor Ufor', test_class.class_list)

    def test_enrollment_empty_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


    ## TODO write a test that adds some example students to a test class, call check_enrolled
    # for a student not enrolled, assert check_enrolled returns false
    def test_enrollment_when_student_not_present(self):
        test_class = ClassList(2)
        test_class.add_student('Mary')
        test_class.add_student('John')
        self.assertFalse(test_class.is_enrolled('Kohl'))




    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', test_class.__str__())


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', test_class.__str__())


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))


    ## However, it would be useful to check that index_of_student returns None if a student isn't present.
    ## TODO write a test for index_of_student to assert it returns None if the student is not in the list
    # Cover the cases where the list is empty
    # And, when the list is not empty but does not contain the student name.
    def test_index_of_student_student_not_present(self):
        test_class = ClassList(2)
        self.assertIsNone(test_class.index_of_student('Jeff'))

        test_class.add_student('student_1')
        test_class.add_student('student_2')

        self.assertEqual(1, test_class.index_of_student('student_1'))
        self.assertEqual(2, test_class.index_of_student('student_2'))
        self.assertIsNone(test_class.index_of_student('student_3'))


    ## TODO write a test(s) for your new is_class_full method
    ## Test a case where the class is full, and when it isn't
    def test_class_is_full_when_class_is_full(self):
        test_class = ClassList(2)
        test_class.add_student('student1')
        test_class.add_student('student_2')
        self.assertTrue(test_class.is_class_full())

    def test_class_is_full_when_class_is_not_full(self):
        test_class = ClassList(3)
        test_class.add_student('student1')
        test_class.add_student('student_2')
        self.assertFalse(test_class.is_class_full())
