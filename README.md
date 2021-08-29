# scut_class2calendar

将华工的课程表导入谷歌日历中.python实现
仅支持华工教务系统的课程表述方法:

`课程<>周次<>地点<>教师<>教学班<>教学班组成<>学分`

1. 在<https://developers.google.com/calendar/quickstart/python>申请api接口文件`credentials.json`

2. 复制接口文件到项目目录下

3. 安装库
    ```shell
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    ```

4. 更改`main.py`和`term_time.py`中的学期开始时间

5. 更改`main.py`中日历名称

6. 运行`main.py`并根据提示进行oauth登录,登陆成功后请终端终端

7. 按照`main.py`中的提示添加课程并运行
  注意: 暂时不支持连堂课,请将`(...-...节)`删除:
  `大学物理实验(二)/(5-8节)2-16周(双)/五山校区 未排地点//(2020-2021-2)-041101051-116/19轻化工程2班;19资源环境科学/1`
  改为
  `大学物理实验(二)/2-16周(双)/五山校区 未排地点//(2020-2021-2)-041101051-116/19轻化工程2班;19资源环境科学/1`
  效果:
  ![](https://github.com/ShevonKuan/scut_class2calendar/blob/master/final.png)
