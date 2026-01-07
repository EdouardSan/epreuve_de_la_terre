import sys

for arguments in sys.argv:
    if arguments == sys.argv[0]:
        continue
    else:
        print(arguments)


