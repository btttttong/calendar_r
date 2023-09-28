###GIVE UP!###

from datetime import datetime, timedelta

def get_cal_month(y, m, is_sunday):
    day = datetime(y, m, 1)  # get first day

    # friday = 4
    month = [[], [], [], [], [], [], []]

    month = add_desc(month, is_sunday)

    for i in range(day.weekday()):  # เติม '' ในช่องก่อนถึงวันที่ 1
        month[i].append('  ')

    while day.month == m:  # ถ้ายังอยู่ในเดือน
        this_weekday = month[
            day.weekday()]  # สร้างตัวแปรมาเก็บค่า ช่องที่ 0-6 ด้วยวันที่ในเดือนแต่ยังเป็น format แบบเต็มๆอยู่
        this_weekday.append(str(day.strftime('%d')))  # เติมค่าในช่องด้วยวันที่ที่ตัดแล้ว
        day = day + timedelta(days=1)  # ขยับวันไปเรื่อยๆ

    for j in range(len(month)):
        if len(month[j]) < 8:
            for x in range(len(month[j]), 8):
                month[j].append('  ')
    return month


def add_desc(month, is_sunday):
    rv = []
    if not is_sunday:
        for i in range(len(month)):
            desc = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            rv.append([desc[i]] + month[i])
    else:
        for i in range(len(month)):
            desc = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
            rv.append([desc[i]] + month[i])
    return rv



def get_cal_year(year, month_number, is_sunday):
    res = []
    for mon in range(1, 13):
        res.append(get_cal_month(year, mon, is_sunday))
    print(range(len(res)))

    for i in range(len(res)):
        day = datetime(year, i+1, 1)  # get first day
        print((datetime.strftime(day, '%B')).ljust(35))
        for j in range(len(res[0])):
            print('\t'.join(res[i][j]))
            # print(res[i][j])
        # print(res[0][i])


# get_cal_year(int(input('Please input year: ') or 2023))


year = int(input('Enter year: ') or 1993)
month_num_row = int(input('How many months to display in a single row (1, 2, or 3)?: ') or 3)
is_sunday = input('Is Sunday (y/n)?: ' or 'n')
is_sunday = True if is_sunday == 'y' else False
get_cal_year(year, month_num_row, is_sunday)
