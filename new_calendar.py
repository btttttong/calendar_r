from datetime import datetime, timedelta

def get_cal_month(year, mon, num, is_sunday):
    dt = datetime(year, mon, 1)
    month = [[], [], [], [], [], [], []]
    month_str = ''
    m_temp = mon
    padding_temp = 8

    wd_desc = ['Mon ', 'Tue ', 'Wed ', 'Thu ', 'Fri ', 'Sat ', 'Sun ']
    if is_sunday:
        wd_desc = ['Sun ', 'Mon ', 'Tue ', 'Wed ', 'Thu ', 'Fri ', 'Sat ']

    for i in range(len(wd_desc)):
        d = month[i]
        d.append(wd_desc[i])

    for x in range(num):
        start_wd = dt.weekday()
        if is_sunday:
            if start_wd == 6:
                start_wd = 0
            else:
                start_wd += 1

        if start_wd > 0:
            for i in range(start_wd):
                this_weekday = month[i]
                this_weekday.append(' ')


        month_str = month_str + (datetime.strftime(dt, '%B')).ljust(35)

        while dt.month == mon:
            start_wd = dt.weekday()
            if is_sunday:
                if start_wd == 6:
                    start_wd = 0
                else:
                    start_wd += 1

            this_weekday = month[start_wd]
            this_weekday.append(str(dt.day))
            dt = dt + timedelta(days=1)
        mon = dt.month

        # Add padding between month
        for i in range(len(month)):
            if len(month[i]) < padding_temp:
                for j in range(len(month[i]), padding_temp):
                    month[i].append(' ')
        padding_temp = padding_temp + 8

    print(month_str)
    return month


def get_cal_year(year, num_row, is_sunday):
    mon = 1
    while 1 <= mon <= 12:
        month = get_cal_month(year, mon, num_row, is_sunday)
        for m in range(len(month)):
            print('\t'.join(month[m]))
        mon += num_row


year = int(input('Enter year: ') or 1993)
month_num_row = int(input('How many months to display in a single row (1, 2, or 3)?: ') or 3)
is_sunday = input('Is Sunday (y/n)?: ' or 'n')
is_sunday = True if is_sunday == 'y' else False
get_cal_year(year, month_num_row, is_sunday)
