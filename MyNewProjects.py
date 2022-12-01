'''
        Mini Project 1
      Bank Management System

1.mini statement
2.credit
3.debit
4.user details

Step 1:
users in dictionary

Step 2:
login

Step 3:
 :-mini statement
 :-credit
 :-debit
 :-user details

Step 4:
result print

'''


                      #Bank Management System

Account_Holders={ 'Immanuel':'imm123@','Olivia':'olv123@','Shailu':'shl123@'}
Amount=5000
username=input('Enter Username:')
password=input('Enter Password:')
if username in Account_Holders.keys():
      if password in Account_Holders.values():
            print('Login Successfull')
            s=input('Enter Your Choice : 1.Mini Statement 2.Credit 3.Debit 4.User Details: ')
            if(s=='1' or s.lower=='Mini Statement'):
                  print('Amount Available in Account:',Amount)
            elif(s=='2' or s.lower=='Credit Amount'):
                  cr=int(input('How Much Amount Do You Want to Credit:'))
                  print('Credit Amont:',cr)
                  Amount=Amount+cr
                  print('Total Amount',Amount)
            elif(s=='3' or s.lower=='Debit Amount'):
                  dr=int(input('How much Amount do you want to debit:'))
                  print('Debit Amount:',dr)
                  Amount=Amount-dr
                  print('Remaining Balance:',Amount)
            elif(s=='4' or s.lower=='User Details'):
                  print('Name:',username)
                  print('UserMail:',username+'@gmail.com')
                  print('Address : Kamareddy,Hyderabad,Telangana')
            else:
                  print('Invalid Choice Please Try Again')
      else:
            print('Entered Wrong Details')
else:
      print('Invalid Credentials')