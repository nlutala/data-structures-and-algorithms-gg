"""
A file to tackle the coding interview question as found on the website below:
https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/

Author: Nathan Lutala (nlutala)
"""


def min_num_of_platforms(
        arrival_times: list[str],
        departure_times: list[str]
) -> int:
    """
    We are given two arrays that represent the arrival and departure times of
    trains, the task is to find the minimum number of platforms required so
    that no train waits.\n

    :param - arrival_times (list of arrival times)\n
    :param - departure_times (list of depature times)\n

    returns the minimum number of platforms required.
    """
    # Find the most amount of trains present at one time
    max_trains_at_once = 0

    for dep_time in departure_times:
        current_trains_at_once = 0
        for arr_time in arrival_times:
            dep_hour_and_min = [int(part) for part in dep_time.split(":")]
            arr_hour_and_min = [int(part) for part in arr_time.split(":")]

            if arr_hour_and_min[0] < dep_hour_and_min[0]:
                current_trains_at_once += 1
            else:
                if arr_hour_and_min[0] == dep_hour_and_min[0]:
                    if arr_hour_and_min[1] < dep_hour_and_min[1]:
                        current_trains_at_once += 1

        max_trains_at_once = current_trains_at_once

    return max_trains_at_once
