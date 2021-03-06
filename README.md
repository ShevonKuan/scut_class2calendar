# scut_class2calendar

将华工的课程表导入谷歌日历中.python实现
仅支持华工教务系统的课程表述方法:

`课程<>周次<>地点<>教师<>教学班<>教学班组成<>学分`

1. 在<https://developers.google.com/calendar/quickstart/python>申请api接口文件
2. 安装库
    ```shell
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    ```
3. 更改`main.py`和`term_time.py`中的学期开始时间
4. 运行`main.py`并根据提示进行oauth登录,登陆成功后请终端终端
5. 按照`main.py`中的提示添加课程并运行

