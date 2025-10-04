import time, sys
from colorama import Fore, Style, init
# initialize colorama for cross-platform compatability
init()

indent = 0    # no. of spaces to indent
indentIncresing = True    # wheather the indentation is incresing or. not

try:
    while True:     # the main program loop
        # select color for the asterisks
        color = Fore.CYAN if indentIncresing else Fore.MAGENTA
        # print the indented colored asterisks
        print(' ' * indent, end = '')
        # Style.RESET_ALL:
        # This is a special style code from colorama that resets the terminal's text formatting to its default (e.g., no color, boldness, or other styles).
        print(color + "******" + Style.RESET_ALL)
        time.sleep(0.2)    # pause

        if indentIncresing:
            # increse the number of spaces
            indent = indent + 1
            if indent == 9:
                # change the direction
                indentIncresing = False
        else:
            # decrese the no of spaces
            indent = indent - 1
            if indent == 0:
                # change the direction
                indentIncresing = True
                
except KeyboardInterrupt:
    sys.exit()




