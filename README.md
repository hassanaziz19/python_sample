# Task1
Multiples Calculator
This program takes 2 arguments through command line (input file name, output file name). Where Input file has multiple rows with 3 integers seperated by space. It will calculate all the multiples of first two integers which are less than the third integer and then sort them in the ascending order of how many multples does a certain row has. The output is printed and written to a file provided as the second command line argument.
As an exampe a sample file is used sample_file.txt which contain rows of integers in following way with an empty row in between:

2 7 26
5 8 31
3 5 10

3 5 15
2 2 10

and the output would for such file would be:

10: 3 5 6 9
10: 2 4 6 8
15: 3 5 6 9 10 12
31: 5 8 10 15 16 20 24 25 30
26: 2 4 6 7 8 10 12 14 16 18 20 21 22 24

The command used to run the main.py file with 2 arguments is:

python main.py --input_file=sample_file.txt --output_file=output1
