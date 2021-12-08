import sys
from dataprep.cymean import mean


def main():
    result = 0.0

    try:
        nums = [float(num) for num in sys.argv[1:]]
    except ValueError:
        nums = []

    try:
        result = mean(nums)
    except ZeroDivisionError:
        pass

    print(result)
