import sys
import csv
from tabulate import tabulate
def (main):
    table = []

    try:
        with open(sys.argv[1], "r") as csvfile:
             reader = csv.reader(csvfile)
             for row in reader:
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))
    def check_command_arg():
    if len(sys.argv)<2:
        sys.exit("too many command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
