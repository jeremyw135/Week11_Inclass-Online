import openpyxl

def get_data_rows(file_name):
    excel_file= openpyxl.load_workbook(file_name)
    main_worksheet= excel_file.active
    return main_worksheet.rows

def count_data():
    row_count=0
    rows_to_count = get_data_rows("games-features.xlsx")
    for row_being_counted in rows_to_count:
        row_count +=1

    print(f"there are {row_count} rows in the file")
count_data()

