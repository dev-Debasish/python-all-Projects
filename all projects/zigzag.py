import time, sys
indent = 0   # no.of spaces to indent
indentIncresing = True   # indentation incresing or. decresing
try:
    while True:    # the main loop
# is a concise way to print spaces for indentation without moving to a new line.
        print(' ' * indent, end = '')
        print("*****")
        time.sleep(0.2)   #pause
        if indentIncresing:
            # increse the indentation
            indent = indent + 1
            if indent == 5:
                # change direction 
                indentIncresing = False
        
        else:
            # decrese the indentation
            indent = indent - 1
            if indent == 0:
                # change direction
                indentIncresing = True

except KeyboardInterrupt:
    sys.exit()


