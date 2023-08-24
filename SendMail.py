import yagmail
from properties import properties

class SendMail():

    credential_path = './resources/credential.txt'

    prop = properties()

    property_values = prop.read_properties_file(credential_path)
    smtp_username = property_values['user']
    smtp_password = property_values['password']
    
    def send_birthday_email(self, email, subject, message, attachment):
        yag = yagmail.SMTP(self.smtp_username, self.smtp_password)
        yag.send(email,subject,message,attachment)


# credential_path = './resources/credential.txt'

# props = properties()

# property_values = props.read_properties_file(file_path=credential_path)
# smtp_username = property_values['user']
# smtp_password = property_values['password']
# print(smtp_username, smtp_password)      