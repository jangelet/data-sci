from collections import Counter
import csv, matplotlib.pyplot as plt, matplotlib.ticker as ticker

def dailyReportTotals():

    with open('complaint_data.csv', 'r') as f:
        reader = csv.DictReader(f)
        if(row['CMPLNT_FR_DT'] for row in reader):
            report_string = [row['CMPLNT_FR_TM'] for row in reader]               #collecting dates, populating list

    print(report_string)
    split_report_str = [i.split(':', 2)[0] for i in report_string]     #splits list, removing minutes from timestamps
    print(split_report_str)
    report_dict = Counter(split_report_str)
    print(report_dict)

    #graph
    plt.bar(report_dict.keys(), report_dict.values(), width = 1,color='#0099cc')
    plt.title("Total Reports Per Hour in the Bronx" + '\n' + "in 2016")
    plt.xlabel("Hour (0:00 - 23:00)")
    plt.ylabel("Number of Reports")
    plt.tick_params(axis='x', which='minor', labelsize=8)
    # plt.xticks(range(0,24), rotation=65)
    ax = plt.axes()
    ax.xaxis.set_major_formatter(ticker.NullFormatter())
    ax.xaxis.set_minor_locator(ticker.FixedLocator([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5,
                                                    11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5,
                                                    21.5, 22.5, 23.5]))
    ax.xaxis.set_minor_formatter(ticker.FixedFormatter(['0:00','01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
                                                        '07:00','08:00','09:00','10:00','11:00','12:00','13:00',
                                                        '14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00',
                                                        '22:00','23:00']))

    for label in ax.get_xminorticklabels():
        label.set_rotation(30)

    # plt.setp(ax.xaxis.get_majorticklabels(), rotation=70)
    # ax.set_xticklabels(ax.xaxis.get_xminorticklabels(), rotation=45)
    # plt.xticks(rotation=45)

    # ax.xaxis.grid()
    ax.yaxis.grid()
    plt.xlim(0, 24)

    plt.show()


dailyReportTotals()