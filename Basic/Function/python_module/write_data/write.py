#create a txt file use a python program

fp=open('user.txt','w')
fp.write('hello')   #create only one line with write
print(fp)

fp=open('user.txt','w')
fp.writelines('''id,first_name,last_name,email,gender
1,Jeffry,Cases,jcases0@buzzfeed.com,Agender
2,Justino,Dayment,jdayment1@nba.com,Male
3,Colas,Dixon,cdixon2@shared.com,Male
4,Adiana,Colwell,acolwell3@symantec.com,Polygender
5,Gipsy,Alty,galty4@surveymonkey.com,Female''')   #create only one line with write
print(fp)

fp=open('user.txt','a')
fp.writelines('''id,first_name,last_name,email,gender
1,Jeffry,Cases,jcases0@buzzfeed.com,Agender
2,Justino,Dayment,jdayment1@nba.com,Male
3,Colas,Dixon,cdixon2@shared.com,Male
4,Adiana,Colwell,acolwell3@symantec.com,Polygender
5,Gipsy,Alty,galty4@surveymonkey.com,Female''')   #append used to rewrite 
print(fp)