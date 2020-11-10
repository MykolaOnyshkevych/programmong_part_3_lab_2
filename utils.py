from tim_sort import tim_sort


def merge_ranges(meetings):
    merged_meetings = []
    sorted_meetings = tim_sort(meetings)
    previous_meeting_start, previous_meeting_end = sorted_meetings[0]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:

        if current_meeting_start <= previous_meeting_end:

            previous_meeting_end = max(current_meeting_end, previous_meeting_end)

        else:

            merged_meetings.append((previous_meeting_start, previous_meeting_end))

            previous_meeting_start, previous_meeting_end = current_meeting_start, current_meeting_end

    merged_meetings.append((previous_meeting_start, previous_meeting_end))

    return merged_meetings
