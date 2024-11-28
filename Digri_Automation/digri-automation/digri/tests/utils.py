# utils.py
import openpyxl


def read_excel(file_path, sheet_name):
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook[sheet_name]
        data = []
        headers = [cell.value for cell in sheet[1]]  # First row as headers
        for row in sheet.iter_rows(min_row=2, values_only=True):
            row_data = dict(zip(headers, row))  # Mapping headers to row data
            data.append(row_data)
        return data
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except KeyError:
        print(f"The sheet {sheet_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
