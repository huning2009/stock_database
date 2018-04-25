# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 21:19:39 2018

@author: Administrator
"""
import pymysql    
import pandas as pd
import os,sys
from sqlalchemy import create_engine  
import numpy as np
from datetime import datetime
import datetime
from dateutil.parser import parse
class StockIndex:
    def __init__(self):
        self.__db=pymysql.connect("localhost","root","123123","stock_index",charset='utf8')
        self.__cursor=self.__db.cursor()
        self.__index_name={"上证50":"000016.SH",
                    "50etf":"510050.SH",
                    "上证综指":"000001.SH",
                    "深圳综指":"399106.SZ"}
    def InquiryName(self,name):
        try:
            return self.__index_name[name]
        except:
            print("名称不存在！")
            return False
    def readDatas(self,code,*args):
        if len(args)==0:
            sql="SELECT * FROM stock_index.`"+code+"`;"
        elif len(args)==1:
            sql="SELECT * FROM stock_index.`"+code+"` where date >= '"+args[0]+"';"
        elif len(args)==2:
            sql="SELECT * FROM stock_index.`"+code+"` where date >= '"+args[0]+"' and date<'"+args[1]+"';"
        else:
            print('wrong input in getdays()!')
            return None
        return self.__fetchall(sql)
    def readData(self,code,date):
        sql="SELECT * FROM stock.`"+code+"` where date = '"+date+"';"
        return self.__fetchall(sql)
    def __fetchall(self,sql):
        self.__cursor.execute(sql)
        self.__db.commit()
        return (self.__cursor.fetchall())  
    def __fetchone(self,sql):
        self.__cursor.execute(sql)
        self.__db.commit()
        return (self.__cursor.fetchone())  