import csv
from datetime import datetime as dt
from wish import wish
from SendMail import SendMail

class greet():

    file_path = './resources/names.csv'

    def execute(self):

        with open(self.file_path, 'r') as csv_file:
            sheet = csv.reader(csv_file)

            today = dt.now().date()
            current_date = today.day
            current_month = today.month
            current_year = today.year

            for i in sheet:
                name, dob, doj, mail = i
                dob = dt.strptime(dob, '%d/%m/%Y')
                doj = dt.strptime(doj, '%d/%m/%Y')
                if current_date == dob.day and current_month == dob.month:
                    total_years = current_year-dob.year
                    print(f'Sending the Birthday mail to: {name}')
                    self.sending_mail(name, mail, 'Birthday', total_years)

                if current_date == doj.day and current_month == doj.month:
                    total_years = current_year-doj.year
                    print(f'Sending the Anniversary mail to: {name}')
                    self.sending_mail(name, mail, 'Anniversary', total_years)
    mails = SendMail()
    def sending_mail(self, name, mail, greeting, years):
        wishes = wish(name, greeting, years)
        subject = wishes.get_subject()
        message = wishes.get_message()
        attachment = wishes.get_attachment()
        self.mails.send_birthday_email(mail, subject, message, attachment)
        print('Mail sent')
