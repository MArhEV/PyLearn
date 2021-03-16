import os
import xlsxwriter

def write_excel(data):

    data = tuple(data)

    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('pomiary.xlsx')
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': 1})

    # Write some data headers.
    worksheet.write('A1', 'Distance', bold)
    worksheet.write('B1', 'Throughput', bold)

    # Start from the first cell below the headers.
    row = 1
    col = 0

    for  distance, throughput in (data):

        worksheet.write_number(row, col, (distance))
        worksheet.write_number(row, col + 1, (throughput))
        row += 1

    workbook.close()

os.system('./waf --run scratch/ms-lab3a.cc > tmp.txt')
os.system('grep "Distance:" tmp.txt > tmp2.txt')

words = []

with open('tmp2.txt', 'r') as f:
    tmp =[]
    for lines in f:
        word = lines.split()
        tmp.append([float(word[1]), float(word[4])])
        print(word[1], word[4])
    f.close()
    write_excel(tmp)