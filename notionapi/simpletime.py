ISO8601_string = "2022-07-28T9:19:00.000Z"


def simple_time(string):
    """Simplifies ISO8601 datetime format into day/month/year and am-pm

    Args:
        string (string): This ISO8601 string is provided by created_time from Notion API

    Returns:
        tuple: date and time as a string respectively
    """
    # Remove unneccessary stuff
    remove_trail = string.replace(".000Z", "")
    separate = remove_trail.split("T")
    # Get date portion
    date = separate[0]
    date_separate = date.split("-")
    # Change year-month-date to date-month-year
    date_reverse = date_separate[::-1]
    date_join = "/".join(date_reverse)
    #  Get time portion
    time = separate[1]
    time_separate = time.split(":")
    # Offsetting UTC+8 to local time
    hour = int(time_separate[0])
    minute = time_separate[1]
    corrected_hour = hour + 8
    # If-else statement converting 24hours time to am - pm
    if corrected_hour > 24:
        str_corrected_hour = str(corrected_hour - 24)
        str_corrected_hour = str_corrected_hour + f":{minute}" + " am"
    elif corrected_hour == 24:
        str_corrected_hour = "12" + f":{minute}" + " am"
    elif corrected_hour <= 12:
        str_corrected_hour = str(corrected_hour)
        str_corrected_hour = str_corrected_hour + f":{minute}" + " am"
    else:
        str_corrected_hour = str(corrected_hour - 12)
        str_corrected_hour = str_corrected_hour + f":{minute}" + " pm"

    return date_join, str_corrected_hour


# date_time = simple_time(string)

# print(date_time[0],date_time[1])
