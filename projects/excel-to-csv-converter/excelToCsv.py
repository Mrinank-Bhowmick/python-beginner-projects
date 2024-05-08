import os
import csv


import openpyxl


def excelToCsv(folder):
    """converts sheets in every excel file in a folder to csv
    Args:
        folder (str): folder containing excel files
    Returns:
        None
    """
    for excelFile in os.listdir(folder):
        # Skip non-xlsx files, load the workbook object.
        if not excelFile.endswith("xlsx"):
            continue
        wb = openpyxl.load_workbook(excelFile)

        for sheetName in wb.get_sheet_names():
            # Loop through every sheet in the workbook.
            sheet = wb.get_sheet_by_name(sheetName)

            # Create the CSV filename from the Excel filename and sheet title.
            csvFilename = excelFile.split(".")[0] + "_" + sheet.title + ".csv"
            csvFileObj = open(csvFilename, "w", newline="")

            # Create the csv.writer object for this CSV file.
            csvWriter = csv.writer(csvFileObj)

            # Loop through every row in the sheet.
            for rowObj in sheet.rows:
                rowData = []  # append each cell to this list
                # Loop through each cell in the row.
                for cellObj in rowObj:
                    # Append each cell's data to rowData.
                    rowData.append(cellObj.value)
                # Write the rowData list to the CSV file.
                csvWriter.writerow(rowData)

            csvFileObj.close()


if __name__ == "__main__":
    excelToCsv(".")
