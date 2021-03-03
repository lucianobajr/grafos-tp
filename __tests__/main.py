import sys

if __name__ == "__main__":
    with open(str(sys.argv[2]), 'r') as file_input:  # arquivo de input
        while True:
            file_line = file_input.readline()
            if not file_line:
                break
            print(file_line)
                