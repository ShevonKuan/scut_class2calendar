from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from lession import lession
import os.path
import pickle
import datetime
date_start = '2021-08-30'  # 该学期第一周的星期一日期 请同时修改term_time中的数值
term = '大三上学期教学周'  # 周次前缀
calendar = 'drshevonkuan@gmail.com'  # 谷歌日历中希望修改的日历名称


'''
####################################接口初始化#####################################
'''
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

"""Shows basic usage of the Google Calendar API.
Prints the start and name of the next 10 events on the user's calendar.
"""
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())
service = build('calendar', 'v3', credentials=creds)


'''
####################################周数记录#####################################
'''
date_start = datetime.datetime.strptime(date_start, "%Y-%m-%d")

for i in range(1, 20):
    date_end = (date_start + datetime.timedelta(days=6))
    event = {
        'summary': term+str(i),
        'start': {
            'date': str(date_start.strftime("%Y-%m-%d")),
            'timeZone': 'Asia/Shanghai',
        },
        'end': {
            'date': str(date_end.strftime("%Y-%m-%d")),
            'timeZone': 'Asia/Shanghai',
        },
        'colorId': '8',
    }

    service.events().insert(calendarId=calendar, body=event).execute()
    date_start = (date_end + datetime.timedelta(days=1))

'''
####################################添加课程#####################################
'''
lession('流体力学与传热Ⅲ/1-13周,15周/五山校区 330601/易聪华/(2021-2022-1)-037100073-3/19轻化工程1班;19轻化工程2班/3.5',1,1,1,service=service).execute()
lession('机械设计基础/1-12周/五山校区 320306/朱本亮/(2021-2022-1)-030100145-12/19轻化工程2班/3.0',1,2,2,service=service).execute()
lession('纤维素功能化/1-8周/五山校区 330601/杨飞/(2021-2022-1)-038100631-1/19轻化工程1班;19轻化工程2班/1.0',1,3,3,service=service).execute()
lession('化工仪表与自动化/1-8周/五山校区 320406/李继庚 满奕/(2021-2022-1)-038100082-1/19轻化工程1班;19轻化工程2班/2.0',2,1,4,service=service).execute()
lession('印刷工艺学/1-8周/五山校区 330204/王钦雯/(2021-2022-1)-038100532-1/19轻化工程1班;19轻化工程2班/2.0',2,2,5,service=service).execute()
lession('制浆造纸原理与工程(一)/1-12周/五山校区 320306//(2021-2022-1)-038100691-2/19轻化工程2班/3.0',3,1,6,service=service).execute()
lession('机械设计基础/1-12周/五山校区 320306/朱本亮/(2021-2022-1)-030100145-12/19轻化工程2班/3.0',3,2,2,service=service).execute()
lession('电工与电子技术实验/1-5周,7周,10-13周,16周/五山校区 未排地点//(2021-2022-1)-024100141-7/19轻化工程1班;19轻化工程2班/1.0',3,3,7,service=service).execute()
lession('化工原理实验(一)/10-13周,16周/五山校区 未排地点//(2021-2022-1)-037100411-17/19轻化工程2班/0.5',3,3,8,service=service).execute()
lession('电工与电子技术实验/1-5周,7周,10-13周,16周/五山校区 未排地点//(2021-2022-1)-024100141-7/19轻化工程1班;19轻化工程2班/1.0',3,4,7,service=service).execute()
lession('化工原理实验(一)/10-13周,16周/五山校区 未排地点//(2021-2022-1)-037100411-17/19轻化工程2班/0.5',3,4,8,service=service).execute()
lession('流体力学与传热Ⅲ/1-13周,15周/五山校区 330601/易聪华/(2021-2022-1)-037100073-3/19轻化工程1班;19轻化工程2班/3.5',4,1,1,service=service).execute()
lession('化工原理实验(一)/16周/五山校区 未排地点//(2021-2022-1)-037100411-17/19轻化工程2班/0.5',4,1,8,service=service).execute()
lession('化工原理实验(一)/16周/五山校区 未排地点//(2021-2022-1)-037100411-17/19轻化工程2班/0.5',4,2,8,service=service).execute()
lession('化工仪表与自动化/1-8周/五山校区 320406/李继庚 满奕/(2021-2022-1)-038100082-1/19轻化工程1班;19轻化工程2班/2.0',4,2,4,service=service).execute()
lession('印刷工艺学/1-8周/五山校区 330204/王钦雯/(2021-2022-1)-038100532-1/19轻化工程1班;19轻化工程2班/2.0',4,3,5,service=service).execute()
lession('机械基础综合实验Ⅱ/12-13周,15-16周/五山校区 未排地点/赵可昕,冯梅,吴广峰,倪建龙,何军,刘新育/(2021-2022-1)-030103142-14/19轻化工程2班/0.5',4,3,9,service=service).execute()
lession('机械基础综合实验Ⅱ/12-13周,15-16周/五山校区 未排地点/赵可昕,冯梅,吴广峰,倪建龙,何军,刘新育/(2021-2022-1)-030103142-14/19轻化工程2班/0.5',4,4,9,service=service).execute()
lession('形势与政策/11周/五山校区 未排地点/陈吴翀/(2021-2022-1)-031101331-40/19轻化工程1班;19轻化工程2班;19资源环境科学/2.0',4,4,10,service=service).execute()
lession('植物纤维化学实验/4-13周/五山校区 未排地点/吴胜龙,何婉芬/(2021-2022-1)-038100181-7/19轻化工程2班/1.0',5,1,11,service=service).execute()
lession('植物纤维化学实验/4-13周/五山校区 未排地点/吴胜龙,何婉芬/(2021-2022-1)-038100181-7/19轻化工程2班/1.0',5,2,11,service=service).execute()
lession('植物纤维化学实验/4-13周/五山校区 未排地点/吴胜龙,何婉芬/(2021-2022-1)-038100181-7/19轻化工程2班/1.0',5,3,11,service=service).execute()
lession('植物纤维化学实验/4-13周/五山校区 未排地点/吴胜龙,何婉芬/(2021-2022-1)-038100181-7/19轻化工程2班/1.0',5,4,11,service=service).execute()
lession('制浆造纸原理与工程(一)/1-12周/五山校区 320306//(2021-2022-1)-038100691-2/19轻化工程2班/3.0',5,5,6,service=service).execute()
