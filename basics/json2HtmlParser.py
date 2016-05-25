import re

inputfile = open("jsonToHtmlParse.txt", "r")
lines = inputfile.readline()

codeRegex = re.compile(r'\[code=(java|sql|xml)].*?\[/code]',0)
