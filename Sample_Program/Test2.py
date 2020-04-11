import sys, getopt, os

print ("Hello World")

def print_help():
    print('Print Help')

print_help()

args = sys.argv
print('Program Name is :-', str(sys.argv[0]))

No_of_arg = len(sys.argv) - 1
for i in range(No_of_arg + 1):
    if i==0:
        pass
    else:
        print('Argument ', i, ' is :- ', str(sys.argv[i]))

try:
    f = open("Input2.csv")
    print("Input File present")
except IOError:
    print("File not accessible")
finally:
    print('File check complete')

inp = 'Input.csv'
oup = 'Output.csv'
call_func = 'Python File_Validation.py -i ' + inp + ' -o ' + oup
print(call_func)

os.system('Python File_Validation.py -i ' + inp + ' -o ' + oup)