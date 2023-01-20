with open('filetext', mode='r') as f:
    lines = f.readlines()
    longest_line = max(lines, key=len)
    print('The longest line is:', longest_line)