from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from lession import lession
import os.path
import pickle
import datetime
date_start = '2021-03-01'  # 该学期第一周的星期日日期 请同时修改term_time中的数值
term = '大二下学期教学周'  # 周次前缀
calendar = ''  # 谷歌日历中希望修改的日历名称


'''
####################################接口初始化#####################################
'''
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

"""Shows basic usage of the Google Calendar API.
Prints the start and name of the next 10 events on the user's calendar.
"""
creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)
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

'''
lession('植物纤维化学/7-8周/五山校区 320303/李兵云/(2020-2021-2)-038100011-2/19轻化工程2班/3',1,4,4).execute()
lession('植物纤维化学/9-12周/五山校区 320303/叶君/(2020-2021-2)-038100011-2/19轻化工程2班/3',1,4,4).execute()
lession('印刷色彩学/1-4周,9-16周/五山校区 340402/唐宝玲/(2020-2021-2)-038100171-1/19轻化工程1班;19轻化工程2班/1.5',2,2,5).execute()
lession('物理化学实验Ⅱ/1-16周/五山校区 未排地点/沈葵,刘仕文,袁高清,安小宁,王芙蓉/(2020-2021-2)-037102001-1/19材料类全英创新班;19轻化工程1班;19轻化工程2班;19资源环境科学/1',2,3,6).execute()
lession('物理化学实验Ⅱ/1-16周/五山校区 未排地点/沈葵,刘仕文,袁高清,安小宁,王芙蓉/(2020-2021-2)-037102001-1/19材料类全英创新班;19轻化工程1班;19轻化工程2班;19资源环境科学/1',2,4,6).execute()
lession('物理化学Ⅰ/5-8周/五山校区 340303/王芙蓉/(2020-2021-2)-037101531-11/19轻化工程1班;19轻化工程2班;19资源环境科学/3',2,5).execute()
lession('植物纤维化学/1-4周,13-14周/五山校区 320303/李兵云/(2020-2021-2)-038100011-2/19轻化工程2班/3',1,4,4).execute()
lession('植物纤维化学/9-12周/五山校区 320303/叶君/(2020-2021-2)-038100011-2/19轻化工程2班/3',3,3,4).execute()
lession('电工与电子技术Ⅱ/1-4周,7-15周/五山校区 340302/汪娟娟/(2020-2021-2)-024100213-6/19船舶工程2班;19海洋工程1班;19轻化工程1班;19轻化工程2班;19资源环境科学/4',3,5,7).execute()
lession('马克思主义基本原理概论/1周/五山校区 340201/昝玉林/(2020-2021-2)-031101621-18/19轻化工程1班;19轻化工程2班;19资源环境科学/2.5',4,3,3).execute()
lession('电工与电子技术Ⅱ/1-4周,7-15周/五山校区 340203/汪娟娟/(2020-2021-2)-024100213-6/19船舶工程2班;19海洋工程1班;19轻化工程1班;19轻化工程2班;19资源环境科学/4',5,1,7).execute()
lession('植物纤维化学/1-4周,7-8周,13-14周/五山校区 320308/李兵云/(2020-2021-2)-038100011-2/19轻化工程2班/3',5,2,4).execute()
lession('大学物理实验(二)/2-16周(双)/五山校区 未排地点/马佳洪/(2020-2021-2)-041101051-115/19轻化工程1班;19轻化工程2班/1',5,3,8).execute()
lession('大学物理实验(二)/2-16周(双)/五山校区 未排地点/马佳洪/(2020-2021-2)-041101051-115/19轻化工程1班;19轻化工程2班/1',5,4,8).execute()
'''
