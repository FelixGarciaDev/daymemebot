import schedule
import time
import calendar

# datetime – Its a combination of date and time along with the attributes 
# year, month, day, hour, minute, second, microsecond, and tzinfo. 

# timedelta – A duration expressing the difference between two date, time, 
# or datetime instances to microsecond resolution.

from datetime import datetime

import telegramBot

from dotenv import dotenv_values
config = dotenv_values()


def postMeme(meme):
    telegramBot.sendMeme(meme)
    # discord.sendMemes(todayMemes)
    # twitter.sendMemes(todayMemes)
    print(schedule.get_jobs())
    return schedule.CancelJob


def scheduleTodayMemesByWeekDay(todayMemes):
    # schedule the meme posting...
    todayMemesByWeekScheduler = schedule.Scheduler()  
    for meme in todayMemes:
        print(meme['name'])
        print(meme['file'])
        print(meme['hour']) 
        todayMemesByWeekScheduler.every().day.at(meme['hour']).do(postMeme, meme)        
        
    
    while True:
        todayMemesByWeekScheduler.run_pending()                
        time.sleep(1)


def getTodayMemesByWeekDay(recurrent):
    today = datetime.now()

    todayDict = {
        'year': today.year,
        'month': today.month,
        'day': today.day,
        'weekday': calendar.day_name[today.weekday()],
        'hour': today.hour,
        'minute:': today.minute,
    }

    weekDay = todayDict['weekday']
    todayMemes = recurrent['weekly'][weekDay]

    scheduleTodayMemesByWeekDay(todayMemes)       


def memes(recurrent):
    # check every day what memes should be posted
    schedule.every().day.at(config["firts_schedule_hour"]).do(getTodayMemesByWeekDay, recurrent)

    while True:
        schedule.run_pending()                
        time.sleep(1)

    getTodayMemesByWeekDay(recurrent)