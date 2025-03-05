# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   HMagnusson,2025MAR01, Modified Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
#student_first_name: str = ''  # Holds the first name of a student entered by the user.
#student_last_name: str = ''  # Holds the last name of a student entered by the user.
#course_name: str = ''  # Holds the name of a course entered by the user.
#student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
#csv_data: str = ''  # Holds combined string data separated by a comma.
#json_data: str = ''  #ference to an opened file. Holds combined string data in a json format.
#file = None  # Holds a re
menu_choice: str  # Hold the choice made by the user.

class FileProcessor:
    '''
    A collection of functions to process JSON files
    
    ChangeLog: (Who, When, What)
    HMagnusson, 2025MAR01, Created Class
    '''

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        '''
        This function reads the data from a JSON file to a list of dictionary rows

        ChangeLog: (Who, When, What)
        HMagnusson, 2025MAR01, Created Function

        :param file_name: A string indicating the file name
        :param student_data: A list of dictionary rows
        :return: list
        '''

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages(message="Text file must exist before running this script!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        '''
        This function writes the data to a JSON file from a list of dictionary rows

        ChangeLog: (Who, When, What)
        HMagnusson, 2025MAR01, Created Function

        :param file_name: A string indicating the file name
        :param student_data: A list of dictionary rows
        :return: None
        '''

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The following data was saved to file!")
            IO.output_student_courses(student_data=student_data)
        except TypeError as e:
            IO.output_error_messages(message= "Verify data is in a valid JSON format", error=e)
        except Exception as e:
            message=("Error: There was a problem with writing to the file.")
            message +=("Please check that the file is not open by another program.")
            IO.output_error_messages(message=message, error=e)
        finally:
            if file.closed == False:
                file.close()

class IO:
    '''
    A collection of functions for presenting input/output

    ChangeLog: (Who, When, What)
    HMagnusson, 2025MAR01, Created Class
    '''

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        '''
        This function displays a custom error message

        ChangeLog: (Who, When, What)
        HMagnusson, 2025MAR01, Created Function

        :param message: String with message data for display
        :param error: Exception object with technical message for display
        :return:
        '''
        print(message)
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error.__doc__)
            print(error.__str__())

    @staticmethod
    def output_menu(menu: str):
        '''
        This function displays the menu to the user.

        ChangeLog: (Who, When, What)
        HMagnusson, 2025MAR01, Created Function

        :param
        :return:
        '''

        print() #blank space for ease of reading
        print(menu)
        print() #blank space for ease of reading

    @staticmethod
    def input_menu_choice():
        '''
        This function displays the users menu choice

        ChangeLog: (Who, When, What)
        HMagnusson, 2025MAR01, Created Function

        :param None:
        :return: string with the users choice
        '''
        try:
            menu_choice = input("What would you like to do: ")
            if menu_choice not in ('1','2','3','4'):
                raise Exception('Invalid menu choice, please try again')
        except Exception as e:
            IO.output_error_messages(e)

        return menu_choice

    @staticmethod
    def output_student_courses(student_data: list):
        '''
        This function displays the students first and last name,
        and the course name to the user.

        ChangeLog: (Who, When, What)
        HMagnusson, 2025MAR01, Created Function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        '''

        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        '''
        This function prompts the user for the students
        first and last name, and the course name.

        ChangeLog: (Who, When, What)
        HMagnusson, 2025MAR01, Created Function

        :param student_data: list of dictionary rows from input data

        :return: list
        '''

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        except ValueError as e:
            IO.output_error_messages(message='Invalid Data Type', error= e)

        except Exception as e:
            IO.output_error_messages(message='Error: There was a problem with your entered data.', error= e)

        return student_data

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IO.input_student_data(student_data=students)


    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
