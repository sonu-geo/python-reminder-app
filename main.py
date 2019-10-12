from controller import Controller
import mysql.connector
flag = 1
while(flag):
    obj =Controller()
    print('\n\n-----------------------');
    inputAction = int(input('Enter the command \n 1-> Create reminder \n 2-> Show reminder \n 3-> Edit reminder \n 4-> Exit\n'))
    print('-----------------------\n\n');
    if(inputAction==4):
        flag=0
    elif(inputAction == 1):
        response = obj.createReminder()
        if(response['status']== 'success'):
            print('\n\n\n********************')
            print('| Reminder Created |')
            print('********************')
    elif(inputAction == 2):
        responses = obj.viewReminder()
        print('\n\n******************************')
        print('ID\tDescription\tTime')
        for response in responses:
            print(response['id'],'\t',response['description'],'\t',response['time'])
        print('******************************\n\n')
    elif(inputAction == 3):
        response = obj.updateReminder()
        if(response['status']== 'success'):
            print('\n\n\n********************')
            print('| Reminder Updated |')
            print('********************')
            
    
