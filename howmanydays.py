monthsInYear = ["January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"]

def daysInMonth(year, month):
    #returns how many days are in the given month of a certain years
    #these first two establish the unchanging months
    if month == monthsInYear[3] or month == monthsInYear[5] or month == monthsInYear[8] or month == monthsInYear[10]:
        return 30
    elif month == monthsInYear[0] or month == monthsInYear[2] or month == monthsInYear[4] or month == monthsInYear[6] or month == monthsInYear[7] or month == monthsInYear[9] or month == monthsInYear[11]:
        return 31
    #this on checks if February is on a leap year, then returns the days
    else:
        if isLeapYear(year):
            return 29
        else:
            return 28

def isLeapYear(year):
    #determines whether the input year is a leap year
    if year % 4 != 0:
        #print "notleap"
        return False
    elif year % 100 != 0:
        #print "leap"
        return True
    elif year % 400 != 0:
        #print "notleap"
        return False
    else:
        #print "leap"
        return True

def daysRemainder(year, month, day, whichDate):
    #returns how many days remain in the month
    #this one checks the first date
    if whichDate == "First":
        #have to include the day we start, so add 1
        return daysInMonth(year, month) - day + 1
    #this one checks the second date
    else:
        return day

def checkValidDates(yearOld, monthOld, dayOld, yearNew, monthNew, dayNew):
    # an error catching functions, to make sure the dates are valid
    if yearNew < yearOld:
        return False
    #checks that the months and days form a continuous time period
    if yearNew == yearOld:
        if monthNew == monthOld:
            if dayNew < dayOld:
                return False
        if monthsInYear.index(monthNew) < monthsInYear.index(monthOld):
            return False
    else:
        return True

def daysBetweenDates(yearOld, monthOld, dayOld, yearNew, monthNew, dayNew):
    #the bulk of the program
    dayTotal = 0 #the value we need
    years = yearOld + 1
    if checkValidDates(yearOld, monthOld, dayOld, yearNew, monthNew, dayNew) == False:
        #checks to make sure dates are valid, or ends program
        return "Error"
    if yearOld == yearNew: #checks dates in the same year
        dayTotal += daysRemainder(yearOld, monthOld, dayOld, "First")
        #print dayTotal
        dayTotal += daysRemainder(yearNew, monthNew, dayNew, "Second")
        #print dayTotal
        #the following can be turned into a function, which can be done alongside
        #making both dates objects
        for month in monthsInYear[ monthsInYear.index(monthOld) + 1:monthsInYear.index(monthNew) ]:
            dayTotal += daysInMonth( yearOld, month)
            #print dayTotal
        return dayTotal
    else: #for dates with years seperating them
        dayTotal += daysRemainder(yearOld, monthOld, dayOld, "First")
        dayTotal += daysRemainder(yearNew, monthNew, dayNew, "Second")
        #checks the remaineder of months in the beginning year
        for month in monthsInYear[ monthsInYear.index(monthOld) + 1: ]:
            #print month
            dayTotal += daysInMonth( yearOld, month )
        #checks remainder of months in ending year
        for month in monthsInYear[ : monthsInYear.index(monthNew) ]:
            #print month
            dayTotal += daysInMonth( yearNew, month )
        while years != yearNew: #total days in each year
            for month in monthsInYear:
                dayTotal += daysInMonth( years, month )
            years += 1
        return dayTotal

print daysBetweenDates( 2015, "March", 10, 2018, "April", 10)
