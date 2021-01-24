import Class_ecxel_write_data
import random
import time
import os
from log import init_logging
logger = init_logging(level='DEBUG')
time_now = time.strftime("%Y%m%d_%H_%M", time.localtime())
file_path="D:\python script\excel\data\ "+time_now
sheet_name='test_case1'
my_excel = Class_ecxel_write_data.Excel_write(file_path,sheet_name)
my_excel.write_data(1,1,'测试次数')
my_excel.write_data(1,2,'测试数据')
i=1
for i in range(1,10):
    i +=1
    data = random.randint(0,9)
    my_excel.write_data(i,1,i-1)
    my_excel.write_data(i,2,data)
my_excel.close_excel()
logger.info('测试结束')