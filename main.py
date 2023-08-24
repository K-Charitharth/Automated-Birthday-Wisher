import schedule
import time
from greet import greet

greetings = greet()
print('Starting the thread!!!')
schedule.every().day.at('14:32').do(greetings.execute)

while True:
    schedule.run_pending()
    print('going to sleep')
    time.sleep(1)
    print('Press ctr+c to exit')

    
