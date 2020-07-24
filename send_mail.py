import smtplib 
from email.mime.text import MIMEText

def send_mail(user, reason, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '79ad108f4c93d8'
    password = 'a835da5163e985'
    message = f"<h3>New Feedback submited</h3><ul><li>User: {user}</li></ul><ul><li>Reason: {reason}</li></ul><ul><li>Rating: {rating}</li></ul><ul><li>Comments: {comments}</li></ul>"

    sender_email = 'email1@example.com'
    reciver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Python Feedback'
    msg['From'] = sender_email
    msg['To'] = reciver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, reciver_email, msg.as_string())
