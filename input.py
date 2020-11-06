def input_values():
    merged_meetings = []
    print("Input your data:")
    while True:
        raw_numbers = input()
        if raw_numbers == "":
            print("Unmerged meetings")
            print(merged_meetings)
            print("Your merged meetings are:")
            break;
        meeting_start, meeting_end = raw_numbers.split(" ")
        if int(meeting_start) > int(meeting_end):
            print("Error, not correctly added values. Your first value should be smaller")
        else:
            merged_meetings.append((int(meeting_start), int(meeting_end)))

    return sorted(merged_meetings)