
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("                        CRIME DATABASE MANAGEMENT                     \n")
CI=pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\CRIME INCIDENCE 2018-2020.csv')
df=pd.DataFrame(CI)
cr=pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\CRIME RATE 2018-2020.csv')
df1=pd.DataFrame(cr)
dc=pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\CRIME-2020.csv')
df2=pd.DataFrame(dc)
mc=pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\MAJOR CRIMES IN METRO CITIES 2018-2020.csv')
df3=pd.DataFrame(mc)
cj=pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\CRIME JUVE 2018-2020.csv')
df4=pd.DataFrame(cj)
cw=pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\CRIME WOMEN .csv')
df5=pd.DataFrame(cw)
cc=pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\CYBER CRIME.csv')
df6=pd.DataFrame(cc)



print('LETS LOOK THE CRIME IN INDIA OVER THE PAST COUPLE OF YEARS \n')
print('IN THE END OF THIS, I HOPE IT HAS MOTIVATED YOU ENOUGH TO HELP STOP CRIME IN INDIA \n')
print('Here are the options from which you can choose from \n')
print('1. crime incidence from 2018-2020 \n')
print('2. crime rate 2018-2020 \n')
print('3. different crimes in 2019-2020 \n')
print('4. crimes in metropolitian cities 2018-2020, the cities include CHENNAI, BENGULURU, MUMBAI, KOLKATA, DELHI \n')
print('5. get various visualisations for the above options, including line chart and barchart \n')
print('6. juvenile crimes in the year 2018-2020 in the metro cities \n')
print('7. crime against women in year 2018-2020 in metro cities \n')
print('8. cyber crime in the year 2018-2020 in metro cities \n')
data=int(input("which would you like to choose: "))
if data==1:
         print('here are some more options')
         print('1. dataframe')
         print('2. bar graph')
         print('3. line chart')
         data1=int(input('which one: '))
         if data1==1:
                   print(df)
         elif data1==2:
            
             df.plot(x='YEAR',y='CRIME INCIDENCE',kind='bar',color=['blue','orange','green'])
             plt.xlabel('YEAR')
             plt.ylabel('CRIME INCIDENCE')
             plt.title('crime incidence in year 2018-2020')
             plt.show()
         elif data1==3:
             xdata=[2018,2019,2020]
             ydata=[31.3,32.2,42.5]
             plt.plot(xdata,ydata,marker='*',markersize=10,linewidth=3,linestyle="--")
             plt.xlabel('year')
             plt.ylabel('crime incedence approx. in lakhs')
             plt.title('crime incidence in year 2018-2020')
             
             plt.show()
elif data==2:
    print('1. the data')
    print('2. line plot')
    print('3. barplot')
    data5=int(input('which one would you like to choose: '))
    if data5==1:
        print('here are the crime rates')
        print(df1)
    elif data5==2:
        df1.plot(x='YEAR',y='CRIME RATE', marker='p',markersize=10,linewidth=3,linestyle="-.")
        plt.ylabel('crime rate(crime per 1 lakh population)')
        plt.title('crime rate in year 2018-2020')
        plt.show()
    elif data5==3:
        df1.plot(x='YEAR',y='CRIME RATE',kind='bar',edgecolor='black',linewidth=2,linestyle='-',color=['blue','orange','green'])
        plt.ylabel('crime rate(crime per 1 lakh population)')
        plt.title('crime rate in year 2018-2020')
        plt.show()
    else:
         print('LOOK FOR OTHER OPTIONS')
         
    
    

elif data==3:
    data2=int(input('which year would you like to choose: '))
    if data2==2019:
        print(df2['2019'])
    elif data2==2020:
        print(df2['CASES-2020'])
    else:
        print('not available, choose another option')

elif data==4:
    print('here are some more options')
    print('1.crime in all cities from 2018-2020')
    print('2. crime in benguluru')
    print('3. crime in chennai')
    print('4. crime in delhi')
    print('5. crime in mumbai')
    print('6. crime in kolkata')
    data3=int(input('enter your number: '))
    if data3==1:
        print(df3)
    elif data3==2:
        print(df3.loc[4])
    elif data3==3:
        print(df3.loc[0])
    elif data3==4:
        print(df3.loc[1])
    elif data3==5:
        print(df3.loc[3])
    elif data3==6:
        print(df3.loc[5])
    else:
        print('if you are looking for data visualisation, press 5 in the first input')
elif data==5:
    print('1. type 1 for line chart')
    print('2. type 2 for bar chart')
    data4=int(input('type your value here: '))
    if data4==1:
        df3.plot(marker='>',markersize=10,linewidth=3,linestyle="-")
        XDATA1=['CHENNAI','DELHI','MUMBAI','BENGULURU','KOLKATA']
        XDATAL=np.arange(len(XDATA1))
        plt.xticks(XDATAL,XDATA1)
        plt.xlabel('CITIES')
        plt.ylabel('CRIME NUMBERS')
        plt.title('crime in all cities from 2018-2020')
        plt.show()
    elif data4==2:
        df3.plot(kind='bar',edgecolor='brown',linewidth=2,linestyle='-',)
        x=['CHENNAI','BANGLORE','MUMBAI','DELHI','KOLKATA']
        xpos=np.arange(len(x))
        plt.xticks(xpos,x)
        plt.xlabel('CITIES')
        plt.ylabel('crime numbers')
        plt.title('crime in all cities from 2018-2020')
        plt.show()
    else:
        print('not available')

elif data==6:
    print('Juvenile crime is a big issuse in the mordern world.\n')
    print('Day by day this is increasing and the concern on youngsters in increasing rapidly \n')
    print('Lets take a look at the stats related to it')
    print(df4)
    df4.plot(marker='*')
    jk=['CHENNAI','BANGLORE','MUMBAI','KOLKATA','DELHI']
    xpos1=np.arange(len(jk))
    plt.xticks(xpos1,jk)
    plt.xlabel('cities')
    plt.ylabel('crime numbers')
    plt.title('JUVENILE CRIME 2018-2020')
            
    
    plt.show()

elif data==7:
    print('Crime against women has been a major concern in India.')
    print('The whole world has been trying to decrease the number no of crimes against women')
    print('Lets look into the stats of crime against women')
    print(df5)
    df5.plot(kind='barh',edgecolor='magenta',)
    jk1=['CHENNAI','BANGLORE','MUMBAI','KOLKATA','DELHI']
    xpos11=np.arange(len(jk1))
    plt.yticks(xpos11,jk1)
    plt.ylabel('cities')
    plt.xlabel('crime numbers')
    plt.title('CRIME AGAINST WOMEN 2018-2020')
    plt.show()


elif data==8:
    print('cyber crimes are increasing in the mordern world')
    print('with development in technology everyday, crime is also increasing. Further digitastion of data has attracted more cyber crime than before')
    print('lets dive into the data we got')
    print('THERE IS NO ASSURANCE THIS IS NOT HACKED')
    print(df6)
    
    
    

        
    
    

else:
    print('goodbye')
    
        
        
         




