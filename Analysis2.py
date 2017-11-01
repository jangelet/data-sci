from collections import Counter
import csv, matplotlib.pyplot as plt, matplotlib.ticker as ticker


def monthlyReportTotals():

    with open('complaint_data.csv', 'r') as f:
        reader = csv.DictReader(f)
        report_string = [row['CMPLNT_FR_DT'] for row in reader]               #collecting dates, populating list
        print(report_string)

    split_report_str = [i.split('/', 2)[0] for i in report_string]     #splits list, removing minutes from timestamps
    report_dict = Counter(split_report_str)
    print(report_dict)

    keys = []
    for keys in report_dict.keys():
        0

    #graph
    plt.bar(report_dict.keys(), report_dict.values(), width=1, color='#c2f0f0')
    plt.title("Total Reports Per Month in the Bronx" + '\n' + "in 2016")
    plt.xlabel("Month (January to December)")
    plt.ylabel("Number of Reports")
    plt.xticks(range(0,12))
    ax = plt.axes()
    ax.xaxis.set_major_formatter(ticker.NullFormatter())
    ax.xaxis.set_minor_locator(ticker.FixedLocator([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5,
                                                    12.5, 13.5]))
    ax.xaxis.set_minor_formatter(ticker.FixedFormatter(['Jan.', 'Feb.', 'March', 'April', 'May', 'June', 'July',
                                                        'August', 'Sept.', 'Oct.', 'Nov.', 'Dec.']))

    for label in ax.get_xminorticklabels():
        label.set_rotation(30)
    ax.yaxis.grid()
    plt.xlim(1,13)
    plt.show()


monthlyReportTotals()