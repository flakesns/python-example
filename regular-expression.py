import re

text= "UPDATE `my_table` SET `col1` = '' WHERE `col_id` = '123456'"
searchObj = re.search( r"`col_id` = '\d+'",text, re.M|re.I)
if searchObj:
    print "Result : ", searchObj.group()
else:
    print "Nothing found!!"
    
    
#Extract number from string
string = "test 123 test test"
mynumber = int(re.search(r'\d+', string).group())
print mynumber
