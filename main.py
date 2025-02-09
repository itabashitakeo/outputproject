import json
import sys
import requests
from IPython.display import display
import pandas as pd

pd.set_option("display.max_columns", None)

API_URL = "https://api.jquants.com"
refreshtoken = "eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.QG04sGTvKERL9-TJ3LOY5CZZw-qqUtCcGhuq3HEh0IFRItcLk6YnIcgRyGa12Dvx12_7ZTwxboPgl6lQ6JKlxBvbT76XVukI_DLUV-31twEzU2fZ05oRrl6LzI8BeBfm501fvBKmi-A49G9wZjAfOW_wPd-aEgTkItUnaaP58ifdwFeU1sT0X1y5qF5M3ipSfpClHGtscMW1RXOSytY5ewx_6TbgSuGwQB6alJorj11yH-58kFWqE1YjqAAxCkbNQPT-a98o-dKJkkZWjNPZLmds0Lf0b9F0Gby3TClTpwpPqByoGn8FPvPdQlvGjpz1XkiQSKmQOj6iWfhoCrVqbA.x53mLadGx6ZvH9jS.lUnWWr89WukIgskTi-afoyz7Dhf4eIFPCDMZjbdd3Q1wX3cZojxZT1ggv1B-GI0XI7TQ5zcc8qE_ADI7RrEL5CdLLb2anxwroh3TCkDDt1D8VPloxbAOEmkfuw7WHE7PaJOzcVwc3tYkAiyupq8muyxKymNeSZ9czmvAtjE_gQhHfNExZdE9_KHP6ZW-9g1Z4G56jJUJxqa6PxRns9qfLFfU-jQosdXRC8pBfqIJ7WoB7jdDsBSH2A-u7SflHYB1yH7Uipx5sNQXsYHWZHdK09C142iy4ug1QhIj6kqE3Kc52IDWXS_lDH1vYoPhZcwWi1dlhQeVzgP4ta7AW081WnzOX7OQEv8IxmJmhg95vcnWZThf0WWZMBuIQOs3Iym0FCAb_tqqmOBUS8HB_hgnq9tp1qF-9rs0Ljyzms7RkXQyyzaeQ34Oitkya2afejlqU5MDIXz9cABFHRKVgJiR1cPq4g4k-bcyckYo1INRbeGWKe3m3S78EiOd_Hpx2neYrt83y4nZshTPb3Hwf4BVz6-5H5cQuj-ujq6rUjZtvdL58UtXgNt9l68jK-QWnaBLb2u7AQFHCQ0dUx-nCRuWA_GL6Y-eK53KLvyfVBhDYik2JAZhuakobphuHV2Ems8_JywnK9YYErBtf4XeW2X9zGzNg0i1WnKo8DI9r-W5PC2tk8sV-25TPRBxzriMaL76opIlMfF8CWlIVMe-hYHuD5Otl-pHtAyW2cJDNPHMGUg5lqvPcAsayl82NHRg0VX3GIwiq0eAGomBxkt8kTLj5FrdjilErMjJu7_2ViVeLvXr3O6oQ10I8kbvWUE55WseR4v5Ky8_s5qOgRWqc7Lfv-qm35uiiDlC_Tt4X42EV6e4HXYhE-H6fSReH5FKklLD9Difd3SQSSjPuA1bD6W5s1bf9uPekZyDvVMZNIeC772hkG18oFkik2pV3m_9XfJgKTsUDPgnAUHyIAas6zw5-2kVgTDpOqpaxEMwEsIId96EejrBGVXuxy8fmdKcpt9v79Qc25MRKactwDIEcbdPZ-CnMhyUHRH_K2hW-jopAeDXzNzQXIEAXw6SWfkPJH9CTBPxVOFVgKyjw9COychAjtsYJG42HYoifBub-C-EQYSL1nws7s3O3OWHfy-MDprCw2kVPBwF62cKjHiEdhm4sR3lNx6lPFGQONeIbuXgYEKhPdSrL7WT7XEWbi2keKwwEoPPnbHBmx0GOqP679-AMALCkmFd0-iJpPna7xnhw7QzmFMaWgvbxNCcg6WlMaofAjHcIVDsqijPzO6kVQ2KmOXqOmo5d8jx4A3uAbBaOuiUN5haOly8bmx5_JKKewAe4CmG0E_QZfRO3w.14ZUupI48faTQV51Hbsj-Q"#@param {type: "string"}

# idToken取得
res = requests.post(f"{API_URL}/v1/token/auth_refresh?refreshtoken={refreshtoken}")
if res.status_code == 200:
    id_token = res.json()['idToken']
    headers = {'Authorization': 'Bearer {}'.format(id_token)}
    display("idTokenの取得に成功しました。")
else:
    display(res.json()["message"])
#@title 株価四本値（/prices/daily_quotes）

#@markdown - 株価は分割・併合を考慮した調整済み株価（小数点第２位四捨五入）と調整前の株価を取得することができます。
#@markdown - データの取得では、銘柄コード（code）または日付（date）の指定が必須となります。

#@markdown （データ更新時刻）
#@markdown - 毎営業日の17:00頃

#@markdown - Premiumプランの方には、日通しに加え、前場(Morning)及び後場(Afternoon)の四本値及び取引高（調整前・後両方）・取引代金が取得可能です。


code = "1301"#@param {type:"string"}
date = "20240514"#@param {type:"string"}

res = requests.get(f"{API_URL}/v1/prices/daily_quotes", params=params, headers=headers)

if res.status_code == 200:
  d = res.json()
  data = d["daily_quotes"]
  while "pagination_key" in d:
    params["pagination_key"] = d["pagination_key"]
    res = requests.get(f"{API_URL}/v1/prices/daily_quotes", params=params, headers=headers)
    d = res.json()
    data += d["daily_quotes"]
  df = pd.DataFrame(data)
  display(df)
else:
  print(res.json())
