

def is_twodigit_odd(number):
    valid_numbers = []
    for i in range(10, 100):
        if i % 2 != 0:
            valid_numbers.append(i)
    if number in valid_numbers:
        return True
    else:
        return False



def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others,
               sudo_mode):
    if sudo_mode:
        result = True
    elif user == file_owner:
        if writable_by_owner:
            return True
        elif writable_by_others:
            result = True
    elif writable_by_group:
        if file_group in users_groups:
            result = True
    else:
        result = False


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle,
                          strong_sunshine):
    other_factors = [red_sky, strong_flower_smell, spiders_down, lying_cattle]
    if wind_scale < 7:
        if rains:
            return True
        elif strong_sunshine:
            return True
        elif cloudy:
            if all(other_factors)
                return True
            else:
                return True
    else:
        return False


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    # This one was optional.
    pass

