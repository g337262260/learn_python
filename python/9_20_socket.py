#!user/bin/env python3
# -*- coding:utf-8 -*-

"""socket-email"""
from email.mime.multipart import MIMEMultipart
from email.parser import Parser

__author__ = 'guowei'

import socket
from email.mime.text import MIMEText
import smtplib
import poplib
def receive_email():
    email = '337262260@qq.com'
    password = 'ewclcatvoixqcbdi'
    pop3_server = 'pop.qq.com'
    # 连接到POP3 服务器
    server = poplib.POP3_SSL(pop3_server,port=995)
    # 打开调试信息
    server.set_debuglevel(1)
    # 打印POP3的服务器欢迎文字
    print(server.getwelcome().decode('utf-8'))
    # 身份认证
    server.user(email)
    server.pass_(password)
    # 返回邮件的数量和占用空间
    print('Messages: %s. Size: %s' % server.stat())
    # list()返回所有邮件的编号:
    resp, mails, octets = server.list()
    # 可以查看返回的列表类似[b'1 82923', b'2 2184', ...]
    print(mails)

    # 获取最新一封邮件, 注意索引号从1开始:
    index = len(mails)
    resp, lines, octets = server.retr(index)

    # lines存储了邮件的原始文本的每一行,
    # 可以获得整个邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    # 稍后解析出邮件:
    msg = Parser().parsestr(msg_content)
    print(msg_content)
    # 可以根据邮件索引号直接从服务器删除邮件:
    # server.dele(index)
    # 关闭连接:
    server.quit()


def send_email():
    # msg = MIMEText('Hello ,send by Python..','plain','utf-8')
    # msg = MIMEText('<html><body><h1>Hello</h1>' +
    #                '<p>send by <a href="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1537444022575&di=2ce17eaa60d6745a119a9e60b03bdee3&imgtype=0&src=http%3A%2F%2Fimg1.gtimg.com%2Fzj%2Fpics%2Fhv1%2F125%2F164%2F2262%2F147128495.jpg">狗子</a>...</p>' +
    #                '</body></html>', 'html', 'utf-8')
    msg = MIMEMultipart()
    # 邮件正文是MIMEText:
    msg.attach( MIMEText('<html><body><h1>小宝，你在干哈呀，面试结束了嘛，我在学习python ,用它给你发邮件，想你啦。</h1>' +
                   '<p>send by <a href="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1537444022575&di=2ce17eaa60d6745a119a9e60b03bdee3&imgtype=0&src=http%3A%2F%2Fimg1.gtimg.com%2Fzj%2Fpics%2Fhv1%2F125%2F164%2F2262%2F147128495.jpg">狗子</a>...</p>' +
                   '</body></html>', 'html', 'utf-8'))
    msg['From'] = 'Guowei'
    msg['To'] = '376733924@qq.com'
    msg['Subject'] = 'Python 测试发邮件'
    from_addr = '337262260@qq.com'
    from_pwd = 'cztuukmmmpixbjfd'
    to_addr = '376733924@qq.com'
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.qq.com'
    server = smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    server.login(from_addr,from_pwd)
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()
    print('Complete')

def send_sina():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('www.sina.com.cn', 80))
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    buffer = []
    while True:
        d = s.recv(1024)
        if d:
            buffer.append(d)
        else:
            break
    data = b''.join(buffer)
    s.close()
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    with open(r'C:\Users\Administrator\Desktop\sina.html', 'wb') as f:
        f.write(html)

if __name__ == '__main__':
   receive_email()