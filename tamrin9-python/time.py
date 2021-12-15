
class time:

    def __init__(self,h,m,s):
        self.hour = h
        self.minute = m
        self.second = s

    def sum(self , secondt):
        result = time(None,None,None)
        result.second = self.second + secondt.second
        result.minute = self.minute + secondt.minute
        result.hour = self.hour + secondt.hour
        if result.second >= 60:
            result.second -= 60
            result.minute += 1
        if result.minute >= 60:
            result.minute -= 60
            result.hour += 1
        return result

    def sub(self,secondt):
        result = time(None,None,None)
        if self.hour > secondt.hour:
            result.second = self.second - secondt.second
            result.minute = self.minute - secondt.minute
            result.hour = self.hour - secondt.hour
            if result.second < 0:
                result.second += 60
                result.minute -=1
            if result.minute < 0:
                result.minute += 60
                result.hour -= 1
        elif self.hour < secondt.hour:
            result.second = secondt.second - self.second
            result.minute = secondt.minute - self.minute
            result.hour = secondt.hour - self.hour
            if result.second < 0:
                result.second += 60
                result.minute -=1
            if result.minute < 0:
                result.minute += 60
                result.hour -= 1
        return result

    def time_tosecond( self):
        result = time(0,0,None)
        result.second = self.hour * 3600 + self.minute * 60 + self.second
        return result.second

    def second_totime(self,second):
        result = time(None,None,second)
        result.hour = result.second//3600
        remain = result.second % 3600
        result.minute = remain // 60
        result.second = remain % 60
        return result

    def show(self):
        print(self.hour , ':' , self.minute , ':' , self.second)


hour = int(input('enter hour:'))
minute = int(input('enter minute:'))
second = int(input('enter second:'))
t1 = time(hour,minute,second)
t1.show()

hour = int(input('enter hour:'))
minute = int(input('enter minute:'))
second = int(input('enter second:'))
t2 = time(hour,minute,second)
t2.show()

t3 = t1.sum(t2)
t3.show()

t4 = t1.sub(t2)
t4.show()

t5 = t1.time_tosecond()
print(t5)

second = int(input('enter second:'))
t6 = time(0,0,0)
t7 = t6.second_totime(second)
t7.show()