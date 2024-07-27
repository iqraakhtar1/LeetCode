class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        
        days_names = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        
        def isLeapYear(y):
            if y%4 == 0:
                if y%100 == 0:
                    if y%400 == 0:
                        return True
                    return False
                else:
                    return True
            else:
                return False
        
        def calculateDays(day, month, year):
            
            start = 1971
            
            total_days = 0
            for y in range(start, year):
                total_days += 365
                if isLeapYear(y):
                    total_days += 1
                else:
                    continue
            
            for m in range(month):
                if m in [1, 3, 5, 7, 8, 10,12]:
                    total_days += 31
                
                elif m in [4,6,9,11]:
                    total_days += 30
                
                elif m == 2:
                    total_days += 28
                    if isLeapYear(year):
                        total_days += 1
                        
            total_days += day
            
            name_ind = (total_days%7)-1
            
            return days_names[name_ind]
        
        return calculateDays(day, month, year)
                    