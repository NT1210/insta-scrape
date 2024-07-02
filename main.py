import excel
import datetime
from time import sleep
from scrape import scrape
from openpyxl import load_workbook
from progressbar import ProgressBar

def main():
    
    date_today = datetime.date.today() # returns a datetime object
    date_today_formatted = date_today.strftime('%Y%m') #e.g.) 202407
    date_for_excel = str(date_today).split(" ")[0] #e.g.)2024-07-01

    wb, ws = excel.loadExcel(date_today_formatted)
    progress = ProgressBar(0, int((ws.max_row-2)/3))
    progress_end = excel.processExcel(date_for_excel, wb, ws, progress)
    sleep(2)
    progress_end.finish()



if __name__ == '__main__':
    main()
