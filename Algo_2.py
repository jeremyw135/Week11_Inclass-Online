import openpyxl
import openpyxl.utils

def get_data_rows(file_name):
    excel_file= openpyxl.load_workbook(file_name)
    main_worksheet= excel_file.active
    return main_worksheet.rows

def find_largest():
    game_data_rows= get_data_rows("games-features.xlsx")
    largest_row= None
    for game_row in game_data_rows:
        if largest_row is None:
            largest_row= game_row
        column_number= openpyxl.utils.column_index_from_string("R")-1
        largest_row_owners= largest_row[column_number].value
        if type(largest_row_owners) is str:
            largest_row=game_row
            continue
        game_row_owners= game_row[column_number].value
        if game_row_owners > largest_row_owners:
            largest_row= game_row
    game_name= largest_row[3].value
    print(f"The game with the most owners is {game_name} ")

find_largest()