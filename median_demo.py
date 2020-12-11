import openpyxl
import openpyxl.utils
from us_state_abbrev import us_state_abbrev

def get_data_rows(file_name):
    excel_file = openpyxl.load_workbook(file_name)
    sheet = excel_file.active
    return sheet.rows

def process_data(all_data):
    state_data= []
    for row in all_data:
        state_name= row[0].value
        if state_name in us_state_abbrev:
            actual_data= row[1].value
            data_tuple= (state_name,actual_data)
            state_data.append(data_tuple)
    return state_data

def get_key(state_tuple):
    return state_tuple[1]

def main():
    all_data= get_data_rows("lanrderr-unemployment.xlsx")
    state_data= process_data(all_data)
    state_data.sort(key=get_key)
    middle = len(state_data)// 2
    median = state_data[middle]
    print(f"{median[0]} had the median unemployment rate of {median[1]}")

if __name__ == '__main__':
    main()