

def is_twodigit_odd(number):
    if len(str(number)) == 2 and number % 2 != 0:
        result = True
    else:
        result = False
    return result


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others,
               sudo_mode):
    if sudo_mode:
        result = True
    elif user == file_owner and writable_by_owner or writable_by_others:
        result = True
    elif writable_by_group and file_group in users_groups:
        result = True
    else:
        result = False


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or (year % 100 == 0 and year % 400 == 0):
        result = True
    else:
        result = False
    return result


def is_sunday(day, weekday_of_first):
    if weekday_of_first == "M" or weekday_of_first == "m":
        sundays = [7, 13, 19, 25, 31]
    elif weekday_of_first == "Tu" or weekday_of_first == "tu":
        sundays = [6, 13, 20, 27]
    elif weekday_of_first == "W" or weekday_of_first == "w":
        sundays = [5, 12, 19, 26]
    elif weekday_of_first == "Th" or weekday_of_first == "th":
        sundays = [4, 11, 18, 25]
    elif weekday_of_first == "F" or weekday_of_first == "f":
        sundays = [3, 10, 17, 24, 31]
    elif weekday_of_first == "Sa" or weekday_of_first == "sa":
        sundays = [2, 9, 16, 23, 30]
    elif weekday_of_first == "Su" or weekday_of_first == "su":
        sundays = [1, 8, 15, 22, 29]
    if day in sundays:
        result = True
    else:
        result = False
    return result


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle,
                          strong_sunshine):
    if (rains == True and wind_scale < 7) or (rains == False and cloudy == True and wind_scale < 7 and (spiders_down == True and strong_flower_smell == True and red_sky == True and lying_cattle == True) or (rains == False and wind_scale < 7 and strong_sunshine == True)):
        result = True
    else:
        result = False
    return result


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    pass
