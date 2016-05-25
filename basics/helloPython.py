import sys

print("Hello world!");
# Comment
'''
multiline
comment
'''


def main():
    print('Hello there', sys.argv[1])


# if the python interpreter is running that module (the source file) as the main program,
# it sets the special __name__ variable to have a value "__main__". If this file is being
# imported from another module, __name__ will be set to the module's name.
if __name__ == '__main__':
    main()
