import smtplib
from email.mime.text import MIMEText

receiver = ['Alibaba-China@outlook.com', 'gyj37191@gmail.com'] # 设置邮件接收人，这里是我的公司邮箱

host = 'smtp.163.com'  # 设置发件服务器地址
port = 25  # 设置发件服务器端口号
sender = 'gyj282319036@163.com'  # 设置发件邮箱
pwd = 'Dishonored2'  # 设置发件邮箱的密码
body = '山东交通学院即将进入期末考试复习周,请各位同学做好准备-----sdjtu.edu.cn' # 设置邮件正文，这里是支持HTML的

msg = MIMEText(body, 'html') # 设置正文为符合邮件格式的HTML内容
msg['subject'] = '期末考试通知' # 设置邮件标题
msg['from'] = "sdjtu@edu.com"  # 设置发送人
msg['to'] = ';'.join(receiver)  # 设置接收人

s = smtplib.SMTP(host, port) 
s.login(sender, pwd)  # 登陆邮箱
s.sendmail(sender, receiver, msg.as_string())  # 发送邮件
