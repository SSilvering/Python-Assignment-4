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
            print('Illegal time. Default time has been set.')
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

        print('Todo list for {0}:'.format(str(self.date)))
        for i in range(len(hours) - 1):
            print('{0}.  {1}-{2} - {3}'.format(i + 1, str(hours[i][0]), str(hours[i][1]), self.tasks[hours[i]]))
        i += 1
        return '{0}.  {1}-{2} - {3}'.format(i + 1, str(hours[i][0]), str(hours[i][1]), self.tasks[hours[i]])
               
    def addTask(self, description, startTime, endTime):
        ''' This method adds new task to the specific date. '''
        
        # Creates a tuple from the times for a specific task.
        key = (str(startTime),str(endTime)) # Creates a tuple from the times for a specific task.
        
        if key not in self.tasks:           # Checks if the key exist in the dictionary.
            self.tasks[key] = description
        else:
            return "Another task which wrote for those hours in tasks list. New entry did not register."

#------------------------------------------------------------------------------ 
# Question -2-

def make_class(attrs, base=None):
    """Return a new class (a dispatch dictionary) with given class attributes"""

    # Getter: class attribute (looks in this class, then base)
    def get(name):
        if name in attrs: return attrs[name]
        elif base:        return base['get'](name)

    # Setter: class attribute (always sets in this class)
    def set(name, value): attrs[name] = value

    # Return a new initialized object instance (a dispatch dictionary)
    def new(*args):
        # instance attributes (hides encapsulating function's attrs)
        attrs = {}

        # Getter: instance attribute (looks in object, then class (binds self if callable))
        def get(name):
            if name in attrs:       return attrs[name]
            else:
                value = cls['get'](name)
                if callable(value): return lambda *args: value(obj, *args)
                else:               return value

        # Setter: instance attribute (always sets in object)
        def set(name, value):       attrs[name] = value

        # instance dictionary
        obj = { 'get': get, 'set': set }

        # calls constructor if present
        init = get('__init__')
        if init: init(*args)

        return obj
    
    # class dictionary
    cls = { 'get': get, 'set': set, 'new': new }
    return cls

def make_date_class():
    """
    Class Date:
     The Date class is created through a make_date_class function,
     which has structure similar to a class statement in Python,
     but concludes with a call to make_class.
    """
    
    ''' Constructor '''
    def __init__(self, year = 2000, month = 1, day = 1):
        if check_date(year, month, day):  # Checks if the date is correct.
            self['set']('year', year)
            self['set']('month', month)
            self['set']('day', day)
        else:
            print("    An incorrect date. \nDefault date has been set.")
            self['set']('year', 2000)
            self['set']('month', 1)
            self['set']('day', 1)
    
    def year(self):
        self['get']('year')
        
    def month(self):
        self['get']('month')
    
    def day(self):
        self['get']('day')
    
    # Creates a dictionary from local variables.
    cls = { '__init__': __init__, 'year': year, 'month': month, 'day': day }
    
    return make_class(cls)

def make_time_class():
    """
    Class Time:
     The Time class is created through a make_time_class function,
     which has structure similar to a class statement in Python,
     but concludes with a call to make_class.
    """
    
    ''' Constructor '''
    def __init__(self, hour = 8, minute = 0):
        if hour >= 0 and hour <= 23 and minute >= 0 and minute <= 59:
            self['set']('hour', hour)
            self['set']('minute', minute)
        else:
            print('Illegal time. Default time has been set.')
            self['set']('hour', 8)
            self['set']('minute', 0)
            
    def __str__(self):
        """ This function prints a string representation of this Time class. """
        return '{0:0=2d}:{1:0=2d}'.format(self['get']('hour'), self['get']('minute'))
    
    # Creates a dictionary from local variables.
    cls = {'__init__':__init__,'__str__':__str__}
    
    return make_class(cls)
            
def make_calentry_class():
    """
    Class CalendarEntry:
     The CalendarEntry class is created through a make_calentry_class function,
     which has structure similar to a class statement in Python,
     but concludes with a call to make_class.
    """

    ''' Constructor '''
    def __init__(self, year, month, day):
        dt = make_date_class()
        dt['get']('__init__')(self, year, month, day) # Composition of Date object to represent the date for tasks.
        self['set']('tasks', {})                      # Define empty dictionary that will contain the tasks for date.
    
    def addTask(self, description, startTime, endTime): 
        ''' This function adds new task to the specific date. ''' 
         
        # Creates a tuple from the times for a specific task.
        key = (startTime['get']('__str__')(), endTime['get']('__str__')())
        
        if key not in self['get']('tasks'):           # Checks if the key exist in the dictionary.
            self['get']('tasks')[key] = description

        else:
            return "Another task which wrote for those hours in tasks list. New entry did not register." 
    
    # Creates a dictionary from local variables.
    cls = {'__init__':__init__,'addTask':addTask}
    
    return make_class(cls)    

#------------------------------------------------------------------------------ 
# Question -3-    

class Shekel:
    """
    This class represents an instance of the NIS. 
    """
    def __init__(self, sum):
        self.sum = sum

    
    def amount(self):
        """ This method returns the amount of the instance in NIS. """
        return self.sum
    
    def __str__(self):
        """ This method prints a string representation of this currency. """
        return '{0}nis'.format(self.sum)
    
    def __repr__(self):
        """ This method prints an evaluable string representation of this class. """
        return 'Shekel({0})'.format(self.sum)
    
    def __add__(self, other): 
        return self.amount() + other.amount()
    
class Dollar:
    """
    This class represents an instance of dollar.
    """
    def __init__(self, sum):
        self.sum = sum
        
    def amount(self):
        """ This method returns the amount of the instance in NIS. """
        return self.sum * rates[('dollar','nis')]
        
    def __str__(self):
        """ This method prints a string representation of this currency. """
        return '{0}$'.format(self.sum)
    
    def __repr__(self):
        """ This method prints an evaluable string representation of this class. """
        return 'Dollar({0})'.format(self.sum)
    
    def __add__(self, other):
        return self.amount() + other.amount()
            
class Euro:
    """
    This class represents an instance of euros.
    """
    def __init__(self, sum):
        self.sum = sum
 
    
    def amount(self):
        """ This method returns the amount of the instance in NIS. """
        return self.sum * rates[('euro','nis')]
    
    def __str__(self):
        """ This method prints a string representation of this currency. """
        return '{0}euro'.format(self.sum)
    
    def __repr__(self):
        """ This method prints an evaluable string representation of this class. """
        return 'Euro({0})'.format(self.sum)
    
    def __add__(self, other):
        return self.amount() + other.amount()

def isShekel(obj):
    """ This function return True if object in type of Shekel. """
    return type(obj) == Shekel
def isDollar(obj):
    """ This function return True if object in type of Dollar. """
    return type(obj) == Dollar
def isEuro(obj):
    """ This function return True if object in type of Euro. """
    return type(obj) == Euro

def add(x, y):
    """ This dispatch function returns the correct function for calculate the sum of two types of coins. """
    if isShekel(x) and isShekel(y):
        return add_shekel_shekel(x, y)
    elif isShekel(x) and isDollar(y):
        return add_shekel_dollar(x, y)
    elif isShekel(x) and isEuro(y):
        return add_shekel_euro(x,y)
    
    elif isDollar(x) and isDollar(y):
        return add_dollar_dollar(x,y)
    elif isDollar(x) and isEuro(y):
        return add_dollar_euro(x,y)
    elif isDollar(x) and isShekel(y):
        return add_shekel_dollar(y,x)
    
    elif isEuro(x) and isEuro(y):
        return add_euro_euro(x,y)
    elif isEuro(x) and isDollar(y):
        return add_dollar_euro(y,x)
    elif isEuro(x) and isShekel(y):
        return add_shekel_euro(y,x)

def add_dollar_dollar(d1,d2):
    """ This function returns the sum of two objects from type of Dollar in NIS. """
    return round(d1.amount() + d2.amount(),2)
def add_euro_euro(e1,e2):
    """ This function returns the sum of two objects from type of Euro in NIS. """
    return round(e1.amount() + e2.amount(),2)
def add_shekel_shekel(s1,s2):
    """ This function returns the sum of two objects from type of Shekel. """
    return round(s1.amount() + s2.amount(),2)
def add_dollar_euro(d,e):
    """ This function returns the sum of two objects from type of Dollar and Euro in NIS. """
    return round(d.amount() + e.amount(),2)
def add_euro_dollar(e,d):
    """ This function returns the sum of two objects from type of Euro and Dollar in NIS. """
    return add_dollar_euro(e, d)
def add_dollar_shekel(d,s):
    """ This function returns the sum of two objects from type of Dollar and Shekel in NIS. """
    return round(d.amount() + s.amount(),2)
def add_shekel_dollar(s,d):
    """  This function returns the sum of two objects from type of Skekel and Dollar in NIS. """
    return add_dollar_shekel(d, s)
def add_euro_shekel(e,s):
    """ This function returns the sum of two objects from type of Euro and Shekel in NIS. """
    return round(e.amount() + s.amount(),2)
def add_shekel_euro(s,e):
    """ This function returns the sum of two objects from type of Shekel and Euro in NIS. """
    return add_euro_shekel(e, s)

#import add from operator

rates ={('dollar', 'nis'): 3.82,('euro','nis'): 4.07}

#------------------------------------------------------------------------------ 
# Question -4- 

def type_tag(x):
    return type_tag.tags[type(x)]

type_tag.tags = {Shekel: 'nis', Dollar: 'dollar', Euro: 'euro'}

def add_coins(x, y):
    """ This function makes a key tuple to retrieve the appropriate function. """
    types = (type_tag(x), type_tag(y))
    return add_coins.implementations[types](x, y)

# A Dictionary contains all the functions that use to make add operation between two different types of coins.
add_coins.implementations = {
                                ('dollar','euro'): add_dollar_euro, 
                                ('euro','dollar'): add_euro_dollar,
                                ('dollar', 'dollar'): add_dollar_dollar,
                                ('dollar','nis'): add_dollar_shekel, 
                                ('nis','dollar'): add_shekel_dollar,
                                ('nis', 'nis'): add_shekel_shekel,
                                ('euro','nis'): add_euro_shekel, 
                                ('nis','euro'): add_shekel_euro,
                                ('euro', 'euro'): add_euro_euro
                            }

def sub_coins(x, y):
    """ This function makes a key tuple to retrieve the appropriate function. """
    types = (type_tag(x), type_tag(y))
    return sub_coins.implementations[types](x, y)

def sub_dollar_dollar(d1,d2):
    """ This function returns the subtract of two objects from type of Dollar in NIS. """
    return round(d1.amount() - d2.amount(),2)
def sub_euro_euro(e1,e2):
    """ This function returns the subtract of two objects from type of Euro in NIS. """
    return round(e1.amount() - e2.amount(),2)
def sub_shekel_shekel(s1,s2):
    """ This function returns the subtract of two objects from type of Shekel. """
    return round(s1.amount() - s2.amount(),2)
def sub_dollar_euro(d,e):
    """ This function returns the subtract of two objects from type of Dollar and Euro in NIS. """
    return round(d.amount() - e.amount(),2)
def sub_euro_dollar(e,d):
    """ This function returns the subtract of two objects from type of Euro and Dollar in NIS. """
    return (-1)*sub_dollar_euro(d, e)
def sub_dollar_shekel(d,s):
    """ This function returns the subtract of two objects from type of Dollar and Shekel in NIS. """
    return (-1)*round(d.amount() - s.amount(),2)
def sub_shekel_dollar(s,d):
    """  This function returns the subtract of two objects from type of Skekel and Dollar in NIS. """
    return sub_dollar_shekel(d, s)
def sub_euro_shekel(e,s):
    """ This function returns the subtract of two objects from type of Euro and Shekel in NIS. """
    return (-1)*round(e.amount() - s.amount(),2)
def sub_shekel_euro(s,e):
    """ This function returns the subtract of two objects from type of Shekel and Euro in NIS. """
    return round(sub_euro_shekel(e, s),2)

# A Dictionary contains all the functions that use to make subtract operation between two different types of coins.
sub_coins.implementations = {
                                ('dollar','euro'): sub_dollar_euro, 
                                ('euro','dollar'): sub_euro_dollar,
                                ('dollar', 'dollar'): sub_dollar_dollar,
                                ('dollar','nis'): sub_dollar_shekel, 
                                ('nis','dollar'): sub_shekel_dollar,
                                ('nis', 'nis'): sub_shekel_shekel,
                                ('euro','nis'): sub_euro_shekel, 
                                ('nis','euro'): sub_shekel_euro,
                                ('euro', 'euro'): sub_euro_euro
                            }

def apply(operator, x, y):
    """Apply an operation ('add' or 'sub') to x and y. """
    tags = (type_tag(x), type_tag(y))
    key = (operator, tags)
    result = apply.implementations[key](x, y) # Returns the result of the operation between the two instances.
        
    # Create a new instance depending on the instance that  received from left operand.
    if isShekel(x):
        return Shekel(round(result,2))
    if isDollar(x):
        return Dollar(round(result/rates[('dollar','nis')],2))
    if isEuro(x):
        return Euro(round(result/rates[('euro','nis')],2)) 

# Put all the addition and subtraction on the arguments to dictionary.
apply.implementations = {}
adders = add_coins.implementations.items()
apply.implementations.update({('add', tags):fn for (tags, fn) in adders})
adders = sub_coins.implementations.items()
apply.implementations.update({('sub', tags):fn for (tags, fn) in adders})

#------------------------------------------------------------------------------ 
# Question -5- 
