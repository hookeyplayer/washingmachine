# -*- coding: utf-8 -*-

# -- Sheet 3 --

# **1. CSV文件**


import pandas as pd
# url = ''
# df = pd.read_csv(url)
df = pd.read_csv('11050350_Academic Request.csv')
df.head()

# **2. Excel文件**


import pandas as pd
url=''
df = pd.read_excel(url, sheetname=0, header=1)

# **3.JSON文件**


df = pd.read_json(url, orient='columns')

# **4.Querying SQL Database**


from sqlalchemy import create_engine
import pandas as pd
# 创建一个跟数据库的连接
database_connection = create_engine('sqlite:///sample.db') 
# Load data
df = pd.read_sql_query('SELECT * FROM data', database_connection) 
# View first two rows
df.head()

