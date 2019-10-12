from dataBaseHelper import DataBaseHelper
from datetime import time,datetime
class Controller:
    def __init__(self):
        self.obj=DataBaseHelper()
    def createReminder(self):
        descriptionForReminder = input('Enter the description for Reminder:')
        print('Enter the date and time details to set reminder')
        yearForReminder = int(input('Enter the year(YYYY):'))
        monthForReminder = int(input('Enter the month(MM):'))
        dateForReminder = int(input('Enter the date(DD):'))
        hourForReminder = int(input('Enter the hour in 24hr format(hh):'))
        minuteForReminder = int(input('Enter the minute(mm):'))
        try:
            dateTimeReminder = datetime(year=yearForReminder,month=monthForReminder,day=dateForReminder,hour=hourForReminder,minute=minuteForReminder)
            response = self.obj.createReminder(descriptionForReminder,dateTimeReminder)   
            if(response['status']=='success'):
                return {'status':'success'}
            else:
                return {'status':'failed','message':response['message']}
        except Exception as e:
            return {'status':'failed','message':e}


    def viewReminder(self):
        responses = self.obj.selectReminder()
        result=[]
        for response in responses:
            result.append({'id':response[0],'description':str(response[1]),'time':str(response[2])})
        return result
    def updateReminder(self):
        id = int(input('Enter the id of reminder to edit:'))
        yearForReminder = int(input('Enter the year(YYYY):'))
        monthForReminder = int(input('Enter the month(MM):'))
        dateForReminder = int(input('Enter the date(DD):'))
        hourForReminder = int(input('Enter the hour in 24hr format(hh):'))
        minuteForReminder = int(input('Enter the minute(mm):'))
        try:
            dateTimeReminder = datetime(year=yearForReminder,month=monthForReminder,day=dateForReminder,hour=hourForReminder,minute=minuteForReminder)
            response = self.obj.updateReminder(id,dateTimeReminder)
            if(response['status']=='success'):
                return {'status':'success'}
            else:
                return {'status':'failed','message':response['message']}
        except Exception as e:
            return {'status':'failed','message':e}
        
