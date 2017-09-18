
###with open("D:\Sagar\Python Related\Scripts\Test.txt","r") as f:
## #   for line in f:
##  #      print ("  "+line.rstrip())
##
### indent your Python code to put into an email
##import glob
### glob supports Unix style pathname extensions
##python_files = glob.glob('*.txt')
##for file_name in sorted(python_files):
##    print ('    ------' + file_name)
##
##    with open(file_name) as f:
##        for line in f:
##            print ('    ' + line.rstrip())

openFile = open("HarryBrown.txt", "r+")
writeFile = openFile.write("Test abc")
openFile.seek(0,0)
readFile = openFile.read()
print (readFile)

openFile.close()
