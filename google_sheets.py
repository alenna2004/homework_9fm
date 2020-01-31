# 1 и 2(уже сдано)
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gc = gspread.authorize(creds)
dir(gc)
sh = gc.openall()
worksheet = sh[0].worksheet('9')
lis = worksheet.get_all_values()
with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(lis)
df = read_csv("out.csv")
lis


# 3
def create_table_without_duplicate(sheet_name: str, row_number: int, col_number: int):
    sh = gc.openall()
    try:
        worksheet = sh[0].add_worksheet(title=sheet_name, rows=row_number, cols= col_number)
    except:
        sh[0].del_worksheet(sh[0].worksheet(sheet_name))
        return create_table_without_duplicate(sheet_name, row_number,col_number)
        
create_table_without_duplicate('Nikolaeva',30,20)


# 4
def copy_student_marks(surname: str, row_number: int):
    if row_number < 2 or row_number > 40:
        raise Exception("Вы ввели неадекватный номер строки")
    else:
        sh = gc.openall()
        from_worksheet = sh[0].worksheet('9')
        to_worksheet = sh[0].worksheet('Nikolaeva')
        r1 = from_worksheet.row_values(1)
        r2 = from_worksheet.row_values(2)
        for i in range(len(r1)):
            to_worksheet.update_cell(1, i+1, r1[i])
        for i in range(len(r2)):
            to_worksheet.update_cell(2, i+1, r2[i])
        lis = from_worksheet.get_all_values()
        i = 1
        while surname not in lis[i][0]:
            i = i + 1
            if i > len(lis):
                raise Exception("Этого человека не существует")
                break
        marks = lis[i]
        for i in range(len(marks)):
            if to_worksheet.row_values(row_number) != []:
                raise Exception('Эта строка уже занята')
        for i in range(len(marks)):
            to_worksheet.update_cell(row_number, i+1, marks[i])
copy_student_marks('Николаева', 3)


# 5
def titles_of_lists(table_name: str):
    sh = gc.open(table_name)
    worksheet_list = sh.worksheets()
    title_list = []
    for i in worksheet_list:
        title_list.append(i.title)
    return title_list
t_list = titles_of_lists('conduit9')
print(t_list)
