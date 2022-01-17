import argparse
import csv
import datetime
import xml.etree.ElementTree as ET
import os

def get_points(test):
    with open(args.exercise+'.csv', mode='r') as exerciseFile:
        exerciseCSV = csv.reader(exerciseFile, delimiter=';')

        for lines in exerciseCSV:
            if lines[0] == test:
                print(test)
                return(int(lines[1]))

def get_success(test):
    with open(args.exercise+'.csv', mode='r') as exerciseFile:
        exerciseCSV = csv.reader(exerciseFile, delimiter=';')

        for lines in exerciseCSV:
            if lines[0] == test[-1] and lines[2] == '1':
                return(False)

        return(True)

def sum_points():
    with open(args.exercise+'.csv', mode='r') as exerciseFile:
        exerciseCSV = csv.reader(exerciseFile, delimiter=';')
        sum = 0

        for lines in exerciseCSV:
            if lines[1] != 'points':
                if lines[2] != '1':
                    print(lines[0])
                    sum = sum + int(lines[1])

        return sum

def find_failures(root):
    testname = []
    message = []
    minus_points = int(0)
    success = True
    for testcase in root.iter('testcase'):
        for failure in testcase.findall('failure'):
            testname.append(testcase.get('name'))
            message.append(failure.get('message'))
            minus_points = minus_points + get_points(testname[-1])
        if success and testname != []:
            success = get_success(testname)

    return (testname, message, minus_points, success)

# create the readers
#xml_parser = xml.sax.make_parser()
argument_parser = argparse.ArgumentParser(description='This script calculates the result of a student\'s exercise.')

# add file argument
argument_parser.add_argument("file_name", help="Provide the XML filename here. (with extension)")
argument_parser.add_argument("-e", "--exercise", help="Provide the exercise CSV here. You find the needed structure at [Insert link here]")
argument_parser.add_argument("-s", "--student", help="Provide the students ID (mail address/student's number/name/etc.) here. Could be a single ID or a CSV file.")
argument_parser.add_argument("-x", "--directory_XML", help="Provide the directory of the report XML file here.", default=".")
#argument_parser.add_argument("-ce", "--directory_exercise_CSV", help="Provide the directory of the exercise CSV file here.", default=".")
#argument_parser.add_argument("-cs", "--directory_student_CSV", help="Provide the directory of the student CSV file here.", default=".")
#argument_parser.add_argument("-t", "--directory_target", help="Provide the targeted directory for the assignment here.", default=".")

args = argument_parser.parse_args()
file = ET.parse(args.directory_XML+"/"+args.file_name)
root = file.getroot()

(testname, message, minus_points, success) = find_failures(root)
if success:
    achieved_points = sum_points() - minus_points
else:
    achieved_points = int(0)

if args.student != None:
    #write new csv
    with open(args.exercise+'_result.csv', 'a', newline='') as csvfile:
        fieldnames = ['Students', 'Achieved Points', 'Max Points', 'Timestamp']
        result_writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
        if os.stat(args.exercise+'_result.csv').st_size == 0:
            result_writer.writeheader()
        result_writer.writerow({'Students':args.student, 'Achieved Points': achieved_points, 'Max Points': sum_points(), 'Timestamp':datetime.datetime.now()})
else:
    i=0
    while i < len(testname):
        print(testname[i])
        print(message[i])
        print()
        i += 1
    print('######## Your Result #########')
    print(achieved_points, 'of', sum_points())

## TODO if count(XML-reports > 1) -> check directory instead of file
