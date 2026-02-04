from datetime import datetime

class Date:
    # constructor
    def __init__(self, year: int,month: int, day: int ) -> None: 
        #here in the constructor we:
        # 1. try to set the date
        if not self.setDate(year, month, day):
            # 2. if the date is invalid, we set it to a default date
            self._year = 1982
            self._month = 6
            self._day = 17

    # __str__ prints if you try to print the object, is similar to toString() methon in Java
    # which is called when you try to print the object
    def __str__(self) -> str:
        # return datetime.timestamp(datetime(self._year, self._month, self._day)).strftime("%d-%m-%Y")
        dt = datetime(self._year, self._month, self._day)
        return dt.strftime("%x")# US format MM/DD/YYYY


    # Getters to access attributes day, month, year
    @property
    def day(self) -> int:
        return self._day
    @property
    def month(self) -> int:
        return self._month
    @property
    def year(self) -> int:
        return self._year
    
    # create setters to modify the attributes day, month, year WITH VALIDATION
    @day.setter
    def day(self, value: int) -> None:
        if value < 1 or value > 31:
            raise ValueError("Day must be between 1 and 31")
        self._day = value
    @month.setter
    def month(self, value: int) -> None:
        if value < 1 or value > 12:
            raise ValueError("Month must be between 1 and 12")
        self._month = value
    @year.setter
    def year(self, value: int) -> None:
        self._year = value

    def is_leap_year(self, year: int) -> bool:
        """Check if the year is a leap year."""
        # method 1 less readable:
        # return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        # method 2 more readable:
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False
        
    def setDate(self, year: int, month: int, day: int) -> bool:
        # days_in_month = [31, 28 + int(self.is_leap_year(year)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # Boolean to int give 0 or 1
        days_in_month: list[int] = [31, 29 if self.is_leap_year(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month < 1 or month > 12:
            return False
        if day < 1 or day > days_in_month[month - 1]:
            return False
        # if all checks passed, set the date
        self._year = year
        self._month = month
        self._day = day
        return True



if __name__ == "__main__":
    date = Date(2024, 6, 15)
    print(date)  # Output: 15-06-2024
    print(f"Day: {date.day}, Month: {date.month}, Year: {date.year}") # here we call the getters
    date.day = 17
    date.month = 6
    date.year = 1982
    print(f"Day: {date.day}, Month: {date.month}, Year: {date.year}") # here we call the getters
    try:
        date.day = 32  # This will raise a ValueError
    except ValueError as e:
        print(e)
    print(f"Day: {date.day}, Month: {date.month}, Year: {date.year}") # here we call the getters
    print(f"Is {date.year} a leap year? {date.is_leap_year(date.year)}")
    print(f"{2038} {'is a leap year' if date.is_leap_year(2038) else 'is not a leap year'}")

    if date.setDate(2020, 2, 29):
        print(f"Date set to: {date}")
    else:
        print("Failed to set date")