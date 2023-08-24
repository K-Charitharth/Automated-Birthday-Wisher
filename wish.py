class wish():
    
    def __init__(self, receiver_name, greeting, years):
        self.receiver_name = receiver_name
        self.greeting = greeting
        self.years = years
    
    def super_script(self):
        if self.years not in range(11,20):
            check = self.years % 10
            match check:
                case 1:
                    return 'st'
                case 2:
                    return 'nd'
                case 3:
                    return 'rd'
                case _:
                    return 'th'
        else:
            return 'th'
    
    def get_subject(self):
        return f"Happy {self.years}{self.super_script()} {self.greeting}!!"
    
    def get_message(self):
        if self.greeting == 'Birthday':
            return f'''Dear {self.receiver_name},\n\nWish you a very happy {self.years}{self.super_script()} {self.greeting}. Hope your special day is full of happiness, fun, and laughter!''' 
        else:
            return f'''Dear {self.receiver_name},\n\nWish you a very happy {self.years}{self.super_script()} {self.greeting}. You are contributor to our team and hope we cross many more milestones'''
    
    def get_attachment(self):
        if self.greeting == 'Birthday':
            return './resources/birthday.jpeg'
        else:
            return './resources/anniverary.jpeg'