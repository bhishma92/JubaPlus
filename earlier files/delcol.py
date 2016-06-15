from openpyxl import load_workbook
from openpyxl.cell import column_index_from_string as col_index
from openpyxl.cell import get_column_letter as col_letter

def del_col(s, col, cmax=None, rmax=None):
    col_num = col_index(col) - 1
    cols = s.columns
    if isinstance(cmax, str):
        cmax = col_index(cmax)
    cmax = cmax or s.get_highest_column()
    rmax = rmax or s.get_highest_row()
    for c in range(col_num, cmax - 1):
        # print("working on column %i" % c)
        for r in range(0, rmax):
            cols[c][r].value = cols[c+1][r].value
    for r in range(0, rmax):
        cols[c+1][r].value = ''

    return s

if __name__ == '__main__':
    wb = load_workbook('input_book.xlsx')
    ws = wb.active
    # or by name: ws = wb['SheetName']
    for i in range(7,:):
        del_col(ws, i)
        wb.save('output_book.xlsx')