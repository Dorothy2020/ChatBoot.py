import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail:

    def __init__(self):
        ...

    def send(self, emails):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)
        
        for email in emails:
            mail = MIMEMultipart('alternative')
            mail['Subject'] = 'Geekflare Celebrations'
            mail['From'] = self.sender_mail
            mail['To'] = email

            text_template = """
            Geekflare

            Hi {0},
            We are delighted announce that our website hits 10 Million views this month.
            """
            html_template = """
            <h1>Geekflare</h1>

            <p>Hi {0},</p>
            <p>We are delighted announce that our website hits <b>10 Million</b> views last month.</p>
            """

            html_content = MIMEText(html_template.format(email.split("@")[0]), 'html')
            text_content = MIMEText(text_template.format(email.split("@")[0]), 'plain')

            mail.attach(text_content)
            mail.attach(html_content)

            service.sendmail(self.sender_mail, email, mail.as_string())

        service.quit()


if __name__ == '__main__':
    mails = input("Enter emails: ").split()

    mail = Mail()
    mail.send(mails)