def input_values():
    unmerged_meetings = []
    print("Input your data:")
    while True:
        meeting_time = input()
        if meeting_time == "":
            print("Unmerged meetings")
            print(unmerged_meetings)
            print("Your merged meetings are:")
            break
        meeting_start, meeting_end = meeting_time.split(" ")
        if int(meeting_start) > int(meeting_end):
            print("Error, not correctly added values. Your first value should be smaller")
        else:
            unmerged_meetings.append((int(meeting_start), int(meeting_end)))

    return unmerged_meetings
