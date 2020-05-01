#!/usr/bin/env python3

class Student(object):
    def __init__(self, first_name, surname, student_id, email_address):
        self.__first_name = first_name
        self.__surname = surname
        self.__student_id = student_id
        self.__email_address = email_address
        self.__lab_marks = []

    def __str__ (self):
        return str(self.__surname).title() + ", " + str(self.__first_name).title() + ": id=" + str(self.__student_id) + " (" + str(self.__email_address) + ")"

    def set_test_mark(self, mark):
        try:
            if mark >= 0 :
                self.__test_mark = mark
            else:
                self.__test_mark = 0
        except:
            pass

    def get_test_mark(self):
        try:
            return float(self.__test_mark)
        except:
            return float(0)

    def set_exam_mark(self, mark):
        try:
            self.__exam_mark = mark
        except:
            pass

    def get_exam_mark(self):
        try:
            return float(self.__exam_mark)
        except:
            return float(0)

    def add_lab_mark(self, mark):
        try:
            if mark >= 0 and mark <= 100:
                self.__lab_marks.append(mark)
        except:
            pass

    def get_lab_marks(self):
        try:
            return str(self.__lab_marks)
        except:
            return []

    def get_average_lab_mark(self):
        try:
            tot = 0
            i = 0
            for num in self.__lab_marks:
                if num >= 0 and num <= 100:
                    tot += num
                    i += 1
            return round(tot / i, 1)
        except:
            return 0

    def get_final_mark(self):
        try:
            return sum(self.__lab_marks) * 0.1 + self.__test_mark * 0.2 + self.__exam_mark * 0.4
        except:
            return float(0)

    def get_grade(self):
        f_mark = self.get_final_mark()
        if f_mark <= 100.0 and f_mark >= 90.0:
            return "A"
        elif f_mark <= 89.9 and f_mark >= 75.0:
            return "B"
        elif f_mark <= 74.9 and f_mark >= 50.0:
            return "C"
        elif f_mark <= 49.9 and f_mark >= 40.0:
            return "D"
        elif f_mark <= 39.9 and f_mark >= 30.0:
            return "E"
        else:
            return "F"

def main():
    s1 = Student("John", "Smith", "N00000001", "john@amail.com")
    s1.add_lab_mark(96)
    s1.add_lab_mark(83)
    s1.add_lab_mark(91)
    s1.add_lab_mark(89)
    s1.set_test_mark(95)
    s1.set_exam_mark(92)
    print('Final={:.1f}, Grade={}'.format(s1.get_final_mark(), s1.get_grade()))

main()
