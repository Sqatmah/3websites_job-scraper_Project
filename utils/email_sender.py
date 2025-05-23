import yagmail

def send_email_with_attachment(recipient_email, subject, body, attachment_path):
    # Log in to your Gmail account
    yag = yagmail.SMTP("sqatmah@gmail.com", "Sdavid1997@")
    yag.send(
        to=recipient_email,
        subject=subject,
        contents=body,
        attachments=attachment_path,
    )
    print("📧 Email sent successfully!")
