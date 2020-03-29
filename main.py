import os
import sys
import argparse


def get_args(args):
    """
    Getting parameters from command line
    :param args: arguments from commandline
    :return: input file name and output file name
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True)
    parser.add_argument('--output_file', required=True)
    params = parser.parse_args(args)
    input_name = params.input_file
    output_name = params.output_file
    return input_name, output_name


def main(input_file, output_file):
    input_file_path = get_absolute_path_to(input_file)
    output_file_path = get_absolute_path_to(output_file)
    rows = read_file(input_file_path)
    all_multiples = get_multiples(rows)
    print_and_write_file(output_file_path, all_multiples)


def get_multiples_of_row(x, y, z):
    """
    This functions takes three integers as input and returns the list of multiples of first two integers which are less
    than third integer
    :param x:
    :param y:
    :param z:
    :return: sorted list of multiples of x and y
    """
    multiples = set([])
    for j in range(1, z):
        for number in [x, y]:
            result = number * j
            multiples.add(result) if result < z else None
    sorted_multiples = sorted(multiples)
    return sorted_multiples


def get_multiples(rows):
    """
    This function takes list of rows, split them,convert each str to int, calculate multiples and returns
    final sorted list of all multiples
    :param rows: list of strings
    :return: list of all multiples
    """
    list_of_all_multiples = []
    for row in rows:
        a = row.split(" ")
        if len(a) < 3:  # Checks if the row does not have 3 values
            continue
        x, y, z = int(a[0]), int(a[1]), int(a[2])
        multiples = get_multiples_of_row(x, y, z)
        string_multiples = " ".join(map(str, multiples))
        list_of_all_multiples.append("{}: {}".format(z, string_multiples))
    list_of_all_multiples.sort(key=len)
    return list_of_all_multiples


def get_absolute_path_to(file_name):
    """
    This function takes file name as an argument and returns the complete path of the file

    :param file_name: Name of file
    :type file_name str
    :return: path of file
    """
    my_directory_path = os.path.dirname(os.path.abspath(__file__))
    path_of_file = os.path.join(my_directory_path, file_name)
    return path_of_file


def read_file(new_file):
    """
    This function takes file path as an argument and returns list of all all rows in file

    :param new_file: complete path of file including file name
    :return: list of all rows in file
    """
    temp = open(new_file, 'r')
    list_of_rows = temp.read().split('\n')
    temp.close()
    return list_of_rows


def print_and_write_file(output_file_path, result_list):
    """
    This function takes file path and end result of all multiples list as arguments and prints and writes that to file

    :param output_file_path: complete path of file including file name
    :param result_list: final list of multiples of all values
    :type result_list list
    """
    new_file = open(output_file_path, "w")
    for item in result_list:
        print(item)
        new_file.write("{}\n".format(item))
    new_file.truncate(new_file.tell() - 2)
    new_file.close()


if __name__ == "__main__":
    input_file_arg, output_file_arg = get_args(sys.argv[1:])
    main(input_file_arg, output_file_arg)
