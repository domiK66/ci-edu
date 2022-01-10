import xml.sax
import argparse

class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.error = ""
        self.failed_test = ""
        self.failures = 0
        self.amount_tests = 0

    # Call when element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if(tag == "testsuite"):
            self.amount_tests = int(attributes["tests"])
            print("*****Result*****")
            if(attributes["errors"] != "0" or attributes["failures"] != "0" or attributes["skipped"] != "0"):
                self.failures = self.failures + int(attributes["errors"])
                self.failures = self.failures + int(attributes["failures"])
                self.failures = self.failures + int(attributes["skipped"])
            print(self.amount_tests-self.failures," of ",self.amount_tests)


# create the readers
xml_parser = xml.sax.make_parser()
argument_parser = argparse.ArgumentParser(description='This script calculates the result of a student\'s exercise.')

# turn off namespaces
xml_parser.setFeature(xml.sax.handler.feature_namespaces, 0)

# add file argument
argument_parser.add_argument("file_name", help="Provide the XML filename here. (with extension)")
argument_parser.add_argument("-e", "--exercise", help="Provide the exercise CSV here. You find the needed structure at [Insert link here]")
argument_parser.add_argument("-s", "--student", help="Provide the students ID (mail address/student's number/name/etc.) here. Could be a single ID or a CSV file.")
argument_parser.add_argument("-x", "--directory-XML", help="Provide the directory of the report XML file here.", default="./")
argument_parser.add_argument("-ce", "--directory-exercise-CSV", help="Provide the directory of the exercise CSV file here.", default="./")
argument_parser.add_argument("-cs", "--directory-student-CSV", help="Provide the directory of the student CSV file here.", default="./")
argument_parser.add_argument("-t", "--directory-target", help="Provide the targeted directory for the assignment here.", default="./")

# override the default ContextHandler
args = argument_parser.parse_args()
Handler = XMLHandler()
xml_parser.setContentHandler( Handler )
xml_parser.parse(args.directory+"/"+args.file_name)
