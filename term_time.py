import datetime

date_start = '2021-08-30'  # 该学期第一周的星期日日期
class t:
    '''
      a: 第a周
      b: 星期几
      c: 第几节课(两节45分钟算一节课)
      将会生成时间格式 '2021-06-04T12:25:00.000+08:00'
      方法:
      `.start` 输出上述格式开始时间
      `.end` 输出上述格式结束时间
    '''
    # 每一周的第一天星期一
    __firstday_list = [datetime.datetime.strptime(
        date_start, "%Y-%m-%d")+datetime.timedelta(days=ii*7) for ii in range(0, 20)]
    # 第几节课
    __starttime = ['08:00:00', '10:00:00', '14:30:00', '16:20:00', '19:00:00']
    __endtime = ['09:45:00', '11:40:00', '16:10:00', '18:00:00', '21:35:00']

    def __init__(self, a, b, c):
        self.week = a-1  # 周次
        self.wkst = b-1  # 星期
        self.order = c-1  # 课次
        self.date = (self.__firstday_list[self.week] +
                     datetime.timedelta(days=self.wkst)).strftime("%Y-%m-%d")

    def start(self):
        return self.date + 'T' + self.__starttime[self.order] + '.000+08:00'

    def end(self):
        return self.date + 'T' + self.__endtime[self.order] + '.000+08:00'
