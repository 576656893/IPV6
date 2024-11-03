from datetime import datetime
from time import sleep
import psutil
import smtplib
from email.mime.text import MIMEText
import socket

def get_ipv6_addresses():
    addresses = []
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET6:
                addresses.append(addr.address)  # 获取所有 IPv6 地址
    return addresses

def send_email(subject, body, to_email):
    smtp_server = 'smtp.qq.com'
    smtp_port = 587
    from_email = '396404216@qq.com'  # 替换为您的邮箱
    password = 'ifxnzywelithbjga'          # 替换为您的邮箱密码

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()  # 启动 TLS
            # smtplib.SMTP.debuglevel = 1
            server.ehlo()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
            print("邮件已发送")
    except smtplib.SMTPAuthenticationError:
        print("身份验证失败：请检查邮箱和密码")
    except smtplib.SMTPConnectError:
        print("无法连接到 SMTP 服务器，请检查服务器地址和端口")
    except Exception as e:
        pass

if __name__ == "__main__":
    control = 1
    ipv6_addresses = get_ipv6_addresses()
    while True:
        if control == True:
            if ipv6_addresses:
                subject = "当前 IPv6 地址"
                body = "\n".join(ipv6_addresses)

                now = datetime.now()
                formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
                print(formatted_time, end = "  ")

                send_email(subject, body, "576656893@qq.com")

                ipv6_addresses_new = get_ipv6_addresses()
                control = not(ipv6_addresses_new == ipv6_addresses)
                if control == True:
                    now = datetime.now()
                    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
                    print(formatted_time, end = "  ")
                    ipv6_addresses = ipv6_addresses_new
                    print("IPV6地址已改变!")
            else:
                print("未找到 IPv6 地址")
                break
        else:
            now = datetime.now()
            formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
            print(formatted_time, end = "  ")
            print("IPV6地址暂未改变")
            ipv6_addresses_new = get_ipv6_addresses()
            control = not(ipv6_addresses_new == ipv6_addresses)
            sleep(15)
            for i in range(1,10):
                print("Hahaha")