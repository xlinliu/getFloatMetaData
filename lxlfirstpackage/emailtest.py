# -*- coding: UTF-8 -*-

def send_email_163(from_addr = 'xlinliu@163.com',
                   password = 'kexueTOU821666WW',
                   to_addrs = ['xiaolinliu@whu.edu.cn'],
                   subject = 'the itu things2',
                   content = None
                   ):
    """This function use 163 email to send simple message.If success,return Ture,else return False
    from_addr:should be 163 email adress
    password:password of your email account
    to_addrs:should be a tuple,like ('xxxxxx@163.com','xxxxxx@163.com')
    subject:subject of your email
    content:content of your email
    """

    if content is None:
        print 'content is None.'
        return False
    try:
        from smtplib import SMTP
        from email.mime.text import MIMEText

        email_client = SMTP(host = 'SMTP.163.com',port=25)
        email_client.login('xlinliu', password)

        #create msg
        msg = MIMEText(content,'plain', _charset = 'utf-8')
        msg['Subject'] = subject
        msg['From']='xlinliu@163.com'
        email_client.sendmail(from_addr,to_addrs, msg.as_string())
        return True

    except Exception,e:
        print e
        return False
    finally:
        email_client.quit()


if __name__ == '__main__':

    print send_email_163(content = 'did you get it?')