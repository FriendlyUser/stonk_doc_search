
from utils.get_docs import get_stonk_data_2
from datetime import datetime
stock_doc_names = ["ZIM:US", "UAN:US", "CM", "POW", "ERTH:CNX"]

for index, stock in enumerate(stock_doc_names):
    # start_date
    start_date = "2010-01-01"
    # end date today in YYYY-MM-DD format
    currentDate = datetime.now().strftime('%Y-%m:%d')
    get_stonk_data_2(stock, start_date, currentDate)
