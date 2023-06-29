import re
import numpy as np
import pandas as pd
from tkinter import filedialog

class Log_analyser():
    def __init__(self, file):
        self.file = file
        self.data_list = []

    def extract_data(self):
        # fields = ['Direction', 'time', 'Rate']
        with open(self.file) as f:

            # self.data_list.append(fields)
            for line in f:
                try:
                    if re.split(" ", line)[5] == "Benchmark":
                        data_line = []
                        data_line.append(self.get_xfert_direction(line))
                        data_line.append(self.get_year(line) + "-" +
                                         self.get_month(line) + "-" +
                                         self.get_day(line) + "-" +
                                         self.get_time(line))
                        data_line.append(self.get_xfert_rate(line))
                        self.data_list.append(data_line)

                except:
                    continue

    def get_year(self, line):
        pattern = "[0-9]{4}"
        result = re.search(pattern, line).group()
        return str(result)

    def get_day(self, line):
        line_split = re.split(" ", line)
        return str(line_split[2])


    def get_month(self, line):
        month_number = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
                        "Jul": 7, "Aug": 8, "Sep":9, "Oct": 10, "Nov": 11, "Dec": 12}
        line_split = re.split(" ", line)
        return str(month_number[line_split[1]])

    def get_time(self, line):
        line_split = re.split(" ", line)
        return str(line_split[3])

    def get_xfert_rate(self, line):
        line_split = re.split(" ", line)
        return float(line_split[11])

    def get_xfert_direction(self, line):
        line_split = re.split(" ", line)
        return line_split[8]

    def create_csv_np(self):
        np.savetxt("csv_export_np.csv", self.data_list, delimiter=",", fmt ='% s')

    def create_dataframe(self):
        fields = ['Direction', 'time', 'Rate']
        df = pd.DataFrame(self.data_list, columns=fields)
        return df
        print(df)

def main():
    log_path = filedialog.askopenfilename()
    log = Log_analyser(log_path)
    log.extract_data()
    # log.create_csv()
    # log.create_csv_np()
    df = log.create_dataframe()
    df.to_csv("export.csv")
    # print(log.data_list)
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
