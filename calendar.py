from datetime import datetime, timedelta


def get_cal_month(y, m):
    day = datetime(y, m, 1)  # get first day
    # friday = 4
    month = [[], [], [], [], [], [], []]
    shift_flg = True
    i = 0

    for i in range(day.weekday()):
        month[i].append('  ')
    while day.month == m:
        this_weekday = month[day.weekday()]  # = ช่องที่ 0-6
        this_weekday.append(str(day.strftime('%d')))  # เติมค่าในช่องด้วยวันที่
        day = day + timedelta(days=1)  # ขยับช่อง

    for j in range(len(month)):
        if len(month[j]) < 8:
            for x in range(len(month[j]), 8):
                month[j].append('  ')
    return month


def add_desc(month):
    rv = []
    for i in range(len(month)):
        desc = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        rv.append([desc[i]] + month[i])
    return rv


def display(year, month):
    # print(month)
    rv = []
    tmpy = []
    for i in range(2, 13):
        # print(i)
        for j in range(len(month)):
            # print(j)
            nextm = add_desc(get_cal_month(year, i))
            rv.append(month[j] + nextm[j])
    return rv


def get_cal_year(year):
    month = get_cal_month(year, 1)
    for i in range(len(month)):
        # print(datetime.strftime(datetime(year, i, 1), '%B'))
        print('  '.join(display(year, add_desc(month))[i]))

    # for m in range(1, 13):
    #
    #     month = get_cal_month(year, m)
    #     print(datetime.strftime(datetime(year, m, 1), '%B'))
    #     # print(display(month))
    #
    #     for i in range(len(month)):
    #         # print(' '.join(add_desc(month)[i]))
    #         print(' '.join(display(month)[i]))

    print('---------------------------------------------')


get_cal_year(int(input('Please input year: ') or 2023))
