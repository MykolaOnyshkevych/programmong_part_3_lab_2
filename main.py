from utils import merge_ranges
from input import input_values


if __name__ == '__main__':
    merged_meetings = input_values()
    print(merge_ranges(merged_meetings))


