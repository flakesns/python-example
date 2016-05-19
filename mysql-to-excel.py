#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
I'm using XlsxWriter to generate excel file.
Install XlsxWriter from terminal (Ubuntu)
$ sudo pip install XlsxWriter
"""

import MySQLdb
import xlsxwriter

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet1 = workbook.add_worksheet('My 1')

worksheet1.write('A1','Col 1')
worksheet1.write('B1','Col 2')
worksheet1.write('C1','Col 3')

db = MySQLdb.connect("localhost","myusername","mypassword","mydb")
cursor = db.cursor()

sql = "SELECT col1,col2,col3 FROM my_table WHERE some_id = %d" % (13)

try:
  cursor.execute(sql)
  results = cursor.fetchall()
  
  i = 2;
  for row in results:
    worksheet1.write('A' + str(i), row[0])
    worksheet1.write('B' + str(i), row[1])
    worksheet1.write('C' + str(i), row[2])
    i += 1
      
except:
   print "Error: unable to fetch data"

bold = workbook.add_format({'bold': True})

#add new worksheet
worksheet2 = workbook.add_worksheet('My 2')

worksheet2.write('A1','Col 1')
worksheet2.write('B1','Col 2')
worksheet2.write('C1','Col 3')

worksheet2.write('A2','Data 1')
worksheet2.write('B2','Data 2', bold)
worksheet2.write('C2','Data 3')

db.close()

workbook.close()
