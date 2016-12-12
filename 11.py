import smtplib
from email.mime.text import MIMEText

receiver = ['xxxxxxxa@outlook.com', 'xxx@xxx'] # 设置邮件接收人，这里是我的公司邮箱

host = 'smtp.163.com'  # 设置发件服务器地址
port = 25  # 设置发件服务器端口号
sender = 'xxx@xxx.com'  # 设置发件邮箱
pwd = 'xxxxxxx'  # 设置发件邮箱的密码
body = 'xxxxxxxxxxxxxxxxxxx' # 设置邮件正文，这里是支持HTML的

msg = MIMEText(body, 'html') # 设置正文为符合邮件格式的HTML内容
msg['subject'] = 'content' # 设置邮件标题
msg['from'] = "xxxxxx"  # 设置发送人
msg['to'] = ';'.join(receiver)  # 设置接收人

s = smtplib.SMTP(host, port) 
s.login(sender, pwd)  # 登陆邮箱
s.sendmail(sender, receiver, msg.as_string())  # 发送邮件
