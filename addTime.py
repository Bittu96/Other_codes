import datetime

def add_time(start, duration, day=None):
    wdlist = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    h,m = map(int, duration.split(':'))
    trav = datetime.timedelta(hours=h, minutes=m)
    dt = datetime.datetime.strptime(start, '%I:%M %p')
    dt2= dt+trav

    dif = (int(dt2.strftime("%d"))-int(dt.strftime("%d")))
    if day==None: wd = ''
    else:
        day = day.title()
        # if dif > 1:
            # print(dif)
        wd = ', '+wdlist[(wdlist.index(day)+dif)%7]

    if dif == 1: dif = "(next day)"
    elif dif > 1: dif = f"({dif} days later)"
    else: dif = ''

    print(f'{int(dt2.strftime("%I"))}{dt2.strftime(":%M %p")}{wd} {dif}')


add_time("3:30 PM", "2:12")
add_time("11:55 AM", "3:12")
add_time("9:15 PM", "5:30")
add_time("11:40 AM", "0:25")
add_time("2:59 AM", "24:00")
add_time("11:59 PM", "24:05")
add_time("8:16 PM", "466:02")











# add_time("3:00 PM", "3:10")
# # Returns: 6:10 PM
 
# add_time("11:30 AM", "2:32", "mOndAy")
# # Returns: 2:02 PM, Monday
 
# add_time("11:43 AM", "00:20")
# # Returns: 12:03 PM
 
# add_time("10:10 PM", "3:30")
# # Returns: 1:40 AM (next day)
 
# add_time("11:43 PM", "24:20", "Tuesday")
# # Returns: 12:03 AM, Thursday (2 days later)
 
# add_time("6:30 PM", "205:12")
# # Returns: 7:42 AM (9 days later)