# scrap tables from market beat using pandas
# and print the tables to a jupyter notebook
# url https://www.marketbeat.com/stocks/NYSE/ZIM/competitors-and-alternatives/

import pandas as pd
import requests
from bs4 import BeautifulSoup
import yfinance as yf

def get_marketbeat_comp(url = "https://www.marketbeat.com/stocks/NYSE/ZIM/competitors-and-alternatives/"):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    tables = soup.find_all("table")
    # find tables with id of competitors-table or competitors-table-alt
    table_ids = ["competitors-table"]
    table_classes = ["vsCompetitors"]

    tables_to_analyze = []
    for table in tables:
        if table.get("id") in table_ids:
            tables_to_analyze.append(table)
        
        tableClasses = table.get("class")
        if tableClasses is not None:
            for tableClass in tableClasses:
                if tableClass in table_classes:
                    tables_to_analyze.append(table)
        # get if tableClass is in table_classes
        # if table.get("class") in table_classes:
        #     tables_to_analyze.append(table)
        # if table.get("id") in table_ids:
    # className vsCompetitors
    dfs = []
    for table in tables_to_analyze:
        df = pd.read_html(str(table))[0]
        dfs.append(df)
    return dfs


def analyze_info(ticker: str = "ZIM"):
  msft = yf.Ticker(ticker)
  info = msft.info
  messages = []
  pluck = lambda dict, *args: (dict[arg] for arg in args)
  # analyzes yfinance info
  currentRatio, ebitda, earningsGrowth, forwardEps, forwardPE, returnOnAssets, returnOnEquity, totalCashPerShare, totalDebt = pluck(info, 'currentRatio', 'ebitda', "earningsGrowth", "forwardEps", "forwardPE", "returnOnAssets", "returnOnEquity", "totalCashPerShare", "totalDebt")
  if currentRatio != None and currentRatio < 1:
    messages.append({
        "currentRatio": f"The currentRatio of {currentRatio} is below 1 and this stock has a high chance of needing to raise revenue."
    })

  if ebitda != None and ebitda < 0:
    messages.append({
        "ebitda": f"This company has a negative ebitda of f{ebitda}"
    })

  if forwardEps != None and forwardEps < 0:
    messages.append({
        "forwardEps": f"Negative fowardEps of: {forwardEps}"
    })

  
  if forwardPE != None and forwardPE < 0:
    messages.append({
        "forwardPE": f"ForwardPE is negative: {forwardPE}"
    })

    messages.append({
        "earningsGrowth": f"EarningsGrowth: {earningsGrowth}"
    })

    messages.append({
        "totalCashPerShare": f"totalCashPerShare: {totalCashPerShare}"
    })

    messages.append({
        "totalDebt": f"totalDebt: {totalDebt}"
    })
    return messages
