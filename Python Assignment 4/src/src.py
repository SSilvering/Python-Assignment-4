#===============================================================================#
#---------------------------Python Assignment 4---------------------------------# 
#                                                                               #
# Student 1:             Shai Hod     - 304800402                               #
# Student 2:             Dudu Abutbul - 200913671                               #
#===============================================================================#

# Question -1-

def check_date(year, month, day):
    """ This boolean function checks if the date is correct. """
    if year < 2000:
        return False
    if month > 12:
        return False
    if day > 31:
        return False
    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # Checks if it leap year.
            if not day <= 29:
                return False
        elif not day <= 28:
            return False
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if not day <= 31:
            return False
    if month == 4 or month == 6 or month == 9 or month == 11:
        if not day <= 30:
            return False
            
    return True

class Date:
    """
    This class represents an object of type Date.
    """
    def __init__(self, year = 2000, month = 1, day = 1):
        if check_date(year, month, day):  # Checks if the date is correct.
            self.year, self.month, self.day = year, month, day

        else:
            print("    An incorrect date. \nDefault date has been set.")
            self.year, self.month, self.day = 2000, 1, 1
            
        self.monthName = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 
                          6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 
                          11:'November', 12:'December'}
    
    def year(self):
        """ This method returns the year of the date. """
        return self.year
    
    def month(self):
        """ This method returns the month of the date. """
        return self.month
    
    def day(self):
        """ This method returns the day of the date. """
        return self.day
    
    def __str__(self):
        """ This method prints a string representation of this Date class. """
        if self.day == 1: return '{0}st of {1}, {2}'.format(self.day, self.monthName[self.month], self.year)
        elif self.day == 2:return '{0}nd of {1}, {2}'.format(self.day, self.monthName[self.month], self.year)
        elif self.day == 3: return '{0}rd of {1}, {2}'.format(self.day, self.monthName[self.month], self.year)
        else: return '{0}th of {1}, {2}'.format(self.day, self.monthName[self.month], self.year)
    
    def __repr__(self):
        """ This method prints an evaluable string representation of this class. """
        return 'Date({0},{1},{2})'.format(self.year, self.month, self.day)

class Time:
    """
    This class represents an object of type Time.
    """
    def __init__(self, hour = 8, minute = 0):
        if hour >= 0 and hour <= 23 and minute >= 0 and minute <= 59:
            self.hour = hour
            self.minute = minute
        else:
            self.hour = 8
            self.minute = 0
    
    def __repr__(self):
        """ This method prints an evaluable string representation of this class. """
        return 'Time({0},{1})'.format(self.hour, self.minute)
    
    def __str__(self):
        """ This method prints a string representation of this Time class. """
        return '{0:0=2d}:{1:0=2d}'.format(self.hour, self.minute)

class CalendarEntry:
    """
    This class represents a calendar entry and TODO list by hours for specific date.
    """
    def __init__(self, year, month, day):
        self.date = Date(year, month, day)  
        self.tasks = {}
            
    def __repr__(self):
        """ This method prints an evaluable string representation of this class. """
        return 'CalendarEntry({0},{1},{2})'.format(str(self.date.year),str(self.date.month),str(self.date.day))
    
    def __str__(self):
        """ This method prints the list of tasks for the specific date. """
        hours = list(self.tasks.keys())     # Creates a list of hours for tasks.
        hours.sort()                        # Sorts list of hours in descending order.
        # TODO: To check if hours.sort() is allow.
        print('Todo list for {0}:'.format(str(self.date)))
        for i in range(len(hours) - 1):
            print('{0}.  {1}-{2} - {3}'.format(i + 1, str(hours[i][0]), str(hours[i][1]), self.tasks[hours[i]]))
        i += 1
        return '{0}.  {1}-{2} - {3}'.format(i + 1, str(hours[i][0]), str(hours[i][1]), self.tasks[hours[i]])
               
    def addTask(self, description, startTime, endTime):
        key = (str(startTime),str(endTime)) # Creates a tuple from the times for a specific task.
        
        if key not in self.tasks:           # Checks if the key exist in the dictionary.
            self.tasks[key] = description
        else:
            return "Another task which wrote for those hours in tasks list. New entry did not register."

# Question -2-
