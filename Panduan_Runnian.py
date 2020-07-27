#判断年份是不是润年
year = int(input("亲，请输入一个年份："))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print("{}是闰年".format(year))
else:
    print("{}不是闰年".format(year))
    
  
