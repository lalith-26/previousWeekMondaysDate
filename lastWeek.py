sun,mon,tue,wed,thur,fri,sat=0,1,2,3,4,5,6;

def findLeapYear(year):
    if (year % 4) == 0:
       if (year % 100) == 0:
           if (year % 400) == 0:
               return 1;
           else:
               return 0;
       else:
           return 1;
    else:
       return 0;

def getPreviousMonthDays(month,year):
        if month<1:
            month=12;
        if month == 9 or month == 4 or month == 6 or month == 11:
            return 30
        elif month == 1 or month == 3 or month == 5 or month== 7 or month == 8 or month == 10 or month== 12:
            return 31
        elif month == 2 and findLeapYear(year) == 1:
            return 29
        elif month == 2 and findLeapYear(year) == 0:
            return 28
        else:
            return None;

def getStartDate(date,day,month,year):
    daysLeft =date-(6+day);
    if (daysLeft)<1:
        
        monthDays = getPreviousMonthDays(month-1 ,year);
        if month!=1:
            return monthDays+(daysLeft),month-1,year;
        else:
            return monthDays+(daysLeft),12,year-1;
        
    return date-(6+day);
    
print getStartDate(1,mon,1,2018);
    
#getStartDate(date,day,month,year)  (day - sun,mon,tue,wed,thur,fri,sat=0,1,2,3,4,5,6);