import sys

def find_missing_number(number_list):
    number_list = [int(x) for x in number_list.split(',')]
    prev_number=0
    for number in number_list:
        if number == prev_number + 2:
            return number - 1
        else:
            prev_number = number

    return None

if __name__ == "__main__":

    print(find_missing_number(sys.argv[1]))
