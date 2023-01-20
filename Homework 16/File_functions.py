
def create_file():
    file = input('Name the file')
    with open(file, 'w') as f:
        f.write(input('Write the content of the file'))

    print(f'The File {file} has been created')

    return f



def print_out_contents():
    with open(file, 'r') as f:

        print(f.read())


#changes


def read_file(file):
    with open(file, 'r') as f:
        content = f.read()
    print(content)