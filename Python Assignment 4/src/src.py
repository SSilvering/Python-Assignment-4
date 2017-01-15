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
        if check_date(year, month, day): # Checks if the date is correct.
            self.year, self.month, self.day = year, month, day

        else:
            print("    An incorrect date. \nDefault date has been set.")
            self.year, self.month, self.day = 2000, 1, 1
    
    def month_name(self):
        """ Returns the name of the month of specific date. """
        if self.month == 1:
            return 'January'
        elif self.month == 2:
            return 'February'
        elif self.month == 3:
            return 'March'
        elif self.month == 4:
            return 'April'
        elif self.month == 5:
            return 'May'
        elif self.month == 6:
            return 'June'
        elif self.month == 7:
            return 'July'
        elif self.month == 8:
            return 'August'
        elif self.month == 9:
            return 'September'
        elif self.month == 10:
            return 'October'
        elif self.month == 11:
            return 'November'
        elif self.month == 12:
            return 'December'
    
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
        """ This method prints a string representation of this date class. """
        if self.day == 1: return '{0}st of {1}, {2}'.format(self.day, self.month_name(), self.year)
        elif self.day == 2:return '{0}nd of {1}, {2}'.format(self.day, self.month_name(), self.year)
        elif self.day == 3: return '{0}rd of {1}, {2}'.format(self.day, self.month_name(), self.year)
        else: return '{0}th of {1}, {2}'.format(self.day, self.month_name(), self.year)
    
    def __repr__(self):
        """ This method prints an evaluable string representation of this class. """
        return 'Date({0},{1},{2})'.format(self.year, self.month, self.day)

class Time:
    