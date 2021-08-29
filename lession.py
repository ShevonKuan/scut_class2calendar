from term_time import t


class lession:
    ''' 
      ls: 课程/周次/地点/教师/教学班/教学班组成/学分组成的字符串
      b: 星期几
      c: 第几节课(两节45分钟算一节课)
      color: 颜色代码
      service: 谷歌初始化日历接口
      这是一个完整的封装类,通过初始化该类来实现添加一个课程,如下:
      ```python
      english = lession('课程/周次/地点/教师/教学班/教学班组成/学分',b,c)
      ```
      请确认周次的描述采用`1-4周,13-14周`一类的格式,支持`-`和`,`辨识.
    '''

    def __init__(self, ls, b, c, color='2',service=None):
        self.ls = ls.split('/')
        self.summary = self.ls[0]
        self.location = self.ls[2]
        self.description = '课程名称: '+self.ls[0]+'\n'\
            '周次: '+self.ls[1]+'\n'\
            '授课老师: '+self.ls[3]+'\n'\
            '教学班组成: '+self.ls[5]+'\n'\
            '学分: '+self.ls[6]
        wk = []
        if ('单' in self.ls[1]):
            for i in self.ls[1].replace('周', '').replace('(单)', '').split(','):
                if '-' in i:
                    for j in range(eval(i.split('-')[0]), eval(i.split('-')[1])+1):
                        if j % 2 == 1:
                            wk.append(j)
        elif ('双' in self.ls[1]):
            for i in self.ls[1].replace('周', '').replace('(双)', '').split(','):
                if '-' in i:
                    for j in range(eval(i.split('-')[0]), eval(i.split('-')[1])+1):
                        if j % 2 == 0:
                            wk.append(j)
                else:
                    wk.append(eval(i))
        else:
            for i in self.ls[1].replace('周', '').split(','):
                if '-' in i:
                    for j in range(eval(i.split('-')[0]), eval(i.split('-')[1])+1):
                        wk.append(j)
                else:
                    wk.append(eval(i))
        self.wk = wk
        self.b = b
        self.c = c
        self.color = color
        self.service = service
    def execute(self):
        '''上传到谷歌日历,不可逆操作'''
        for i in self.wk:
            event = {
                'summary': self.summary,
                'location': self.location,
                'description': self.description,
                'start': {
                    'dateTime': t(i, self.b, self.c).start(),
                    'timeZone': 'Asia/Shanghai',
                },
                'end': {
                    'dateTime': t(i, self.b, self.c).end(),
                    'timeZone': 'Asia/Shanghai',
                },
                'colorId': self.color,
            }
            print(event)
            self.service.events().insert(calendarId='drshevonkuan@gmail.com', body=event).execute()
        return 'done'
