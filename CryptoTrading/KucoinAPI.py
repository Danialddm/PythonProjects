import requests
import csv
import numpy as np
from datetime import datetime
# ////////////////////////////
_startAt = 2018-12-25 09:27:53
_startAt = datetime.timestamp(_startAt)
_endtAt = 2018-12-25 09:27:53
_endtAt = datetime.timestamp(_endtAt)
_params = {
            "type": "1hour",
            "symbol": "ETH-USDT",
            "startAt": _startAt,
            "endAt": _endtAt
          }
_url = requests.get("https://api.kucoin.com/api/v1/market/candles", params=_params)
_respjson = _url.json()
_time = []
_openingPice = []
_closingPrice = []
_highestPrice = []
_lowestPrice = []
_volume = []
_amount = []
_resp = _respjson['data']
for d in _resp:
    dt = datetime.fromtimestamp(d[0])
    date_time = dt.strftime("%Y-%m-%d, %H:%M:%S")
    _time.append(date_time)
    _openingPice.append(d[1])
    _closingPrice.append(d[2])
    _highestPrice.append(d[3])
    _lowestPrice.append(d[4])
    _volume.append(d[5])
    _amount.append(d[6])

arrtime = np.array(_time)
arrop = np.array(_openingPice)
arrcp = np.array(_closingPrice)
arrhp = np.array(_highestPrice)
arrlp = np.array(_lowestPrice)
arrvol = np.array(_volume)
arramo = np.array(_amount)

"""
with open('//Kucoindata.csv', 'w') as f:
        _writer = csv.writer(f) # create
        _writer.writerow(["DateTime", "OpeningPrice", "ClosingPrice", "HighestPrice", "LowestPrice", "Volume", "Amount"])
        for k in range(_params['limit']):
            _writer.writerow([arrtime[k], arrop[k], arrcp[k], arrhp[k], arrlp[k], arrvol[k], arramo[k]])
"""