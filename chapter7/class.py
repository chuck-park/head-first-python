# class Athlete:
#     def __init__(self, name, dob=None, times=[]):
#         self.name = name
#         self.dob = dob
#         self.times = times
#
#     def top3(self):
#         return sorted(set([sanitize(t) for t in self.times]))[0:3]
#
#     def add_time(self, time_value):
#         self.times.append(time_value)
#
#     def add_times(self, list_of_times=[]):
#         self.times.extend(list_of_times)


class AthleteList(list):
    def __init__(self, name, dob=None, times=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(times)

    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            templ = data.strip().split(',')

            return AthleteList(templ.pop(0), templ.pop(0), templ)

    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return None


# james = get_coach_data('james2.txt')
# james.add_time('1.59')
# james.add_times(['2.04', '1:59'])
#
# print(james.name + "'s fastest times are: " + str(james.top3()))


# for test AthleteList
# james = get_coach_data('james2.txt')
# james.append('1.59')
# james.extend(['2.04', '1:59'])
#
# print(james.name + "'s fastest times are: " + str(james.top3()))

james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')
print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))
