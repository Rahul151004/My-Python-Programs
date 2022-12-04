def part1(birth_day,birth_month,birth_year):

    birth_year_days=0
    days=30
    for i in range(1,birth_month+1):
#for leap year...........
        if i == 1 and birth_year%4==0 and (birth_year%100!=0 or birth_year % 400==0) :
            birth_year_days=(31-birth_day+1)+5+(12-birth_month)*30
        elif i == 2 and birth_year%4==0 and (birth_year%100!=0 or birth_year % 400==0) :
            birth_year_days=(29-birth_day+1)+6+(12-birth_month)*30   
        elif i == 3 and birth_year%4==0 and (birth_year%100!=0 or birth_year % 400==0) :
            birth_year_days=(31-birth_day+1)+5+(12-birth_month)*30
        elif i == 4 and birth_year%4==0 and (birth_year%100!=0 or birth_year % 400==0) :
            birth_year_days=(30-birth_day+1)+5+(12-birth_month)*30
        elif i == 5 and birth_year%4==0 and (birth_year%100!=0 or birth_year % 400==0) :
            birth_year_days=(31-birth_day+1)+4+(12-birth_month)*30
        elif i == 6 and birth_year%4==0 and (birth_year%100!=0 or birth_year % 400==0) :
            birth_year_days=(30-birth_day+1)+4+(12-birth_month)*30
        elif i == 7 and birth_year%4==0 and (birth_year%100!=0 or birth_year % 400==0) :
            birth_year_days=(31-birth_day+1)+3+(12-birth_month)*30
        elif i == 8 and birth_year%4==0 and (birth_year%100!=0 or birth_year % 400==0) :
            birth_year_days=(31-birth_day+1)+2+(12-birth_month)*30
        elif i == 9 and birth_year%4==0 and (birth_year%100!=0 or birth_year % 400==0) :
            birth_year_days=(30-birth_day+1)+2+(12-birth_month)*30
        elif i == 10 and birth_year%4==0 and (birth_year%100!=0 or birth_year % 400==0) :
            birth_year_days=(31-birth_day+1)+1+(12-birth_month)*30
        elif i == 11 and birth_year%4==0 and (birth_year%100!=0 or birth_year % 400==0) :
            birth_year_days=(30-birth_day+1)+1+(12-birth_month)*30
        elif i == 12 and birth_year%4==0 and (birth_year%100!=0 or birth_year % 400==0) :
            birth_year_days=(31-birth_day+1)+0+(12-birth_month)*30

#for not leap year...............
        elif i in [1,5] and birth_year%4!=0 and (birth_year%100==0 or birth_year % 400!=0) :
            birth_year_days=(31-birth_day+1)+4+(12-birth_month)*30
        elif i == 6 and birth_year%4!=0 and (birth_year%100==0 or birth_year % 400!=0) :
            birth_year_days=(30-birth_day+1)+4+(12-birth_month)*30
        elif i == 2 and birth_year%4!=0 and (birth_year%100==0 or birth_year % 400!=0) :
            birth_year_days=(28-birth_day+1)+6+(12-birth_month)*30
        elif i == 3 and birth_year%4!=0 and (birth_year%100==0 or birth_year % 400!=0) :
            birth_year_days=(31-birth_day+1)+5+(12-birth_month)*30
        elif i == 4 and birth_year%4!=0 and (birth_year%100==0 or birth_year % 400!=0) :
            birth_year_days=(30-birth_day+1)+5+(12-birth_month)*30    
        elif i == 7 and birth_year%4!=0 and (birth_year%100==0 or birth_year % 400!=0) :
            birth_year_days=(31-birth_day+1)+3+(12-birth_month)*30
        elif i == 8 and birth_year%4!=0 and (birth_year%100==0 or birth_year % 400!=0) :
            birth_year_days=(31-birth_day+1)+2+(12-birth_month)*30
        elif i == 9 and birth_year%4!=0 and (birth_year%100==0 or birth_year % 400!=0) :
            birth_year_days=(30-birth_day+1)+2+(12-birth_month)*30
        elif i == 10 and birth_year%4!=0 and (birth_year%100==0 or birth_year % 400!=0):
            birth_year_days=(31-birth_day+1)+1+(12-birth_month)*30
        elif i == 11 and birth_year%4!=0 and (birth_year%100==0 or birth_year % 400!=0):
            birth_year_days=(30-birth_day+1)+1+(12-birth_month)*30
        elif i == 12 and birth_year%4!=0 and (birth_year%100==0 or birth_year % 400!=0):
            birth_year_days=(31-birth_day+1)+0+(12-birth_month)*30   

    a=birth_year_days
    return(a)

def part2(birth_year,current_year):

    days=365
    total_days=0
    for i in range(birth_year+1,current_year):
        if i%4==0 and (i%100!=0 or i%400==0):
            days=days+1
            total_days+=366
        else:
            days=days
            total_days+=365
    return(total_days)

def part3(current_day,current_month,current_year):

    current_year_days=0
    days=30
    for i in range(1,current_month+1):
#for leap year........    
        if i == 1 and current_year%4==0 and (current_year%100!=0 or current_year % 400==0) :
            current_year_days=current_day+(current_month-1)*30
        elif i in [6,7] and current_year%4==0 and (current_year%100!=0 or current_year % 400==0) :
            current_year_days=current_day+2+(current_month-1)*30
        elif i in [2,4,5] and current_year%4==0 and (current_year%100!=0 or current_year % 400==0) :
            current_year_days=current_day+1+(current_month-1)*30
        elif i == 8 and current_year%4==0 and (current_year%100!=0 or current_year % 400==0) :
            current_year_days=current_day+3+(current_month-1)*30
        elif i in [9,10] and current_year%4==0 and (current_year%100!=0 or current_year % 400==0) :
            current_year_days=current_day+4+(current_month-1)*30
        elif i in [11,12] and current_year%4==0 and (current_year%100!=0 or current_year % 400==0) :
            current_year_days=current_day+5+(current_month-1)*30
        elif i == 3 and current_year%4==0 and (current_year%100!=0 or current_year % 400==0) :
            current_year_days=current_day+(current_month-1)*30

#for non leap year............
        elif i == 1 and current_year%4!=0 and (current_year%100==0 or current_year % 400!=0) :
            current_year_days=current_day+(current_month-1)*30
        elif i in [2,6,7] and current_year%4!=0 and (current_year%100==0 or current_year % 400!=0) :
            current_year_days=current_day+1+(current_month-1)*30
        elif i in [4,5] and current_year%4!=0 and (current_year%100==0 or current_year % 400!=0) :
            current_year_days=current_day+0+(current_month-1)*30
        elif i == 8 and current_year%4!=0 and (current_year%100==0 or current_year % 400!=0) :
            current_year_days=current_day+2+(current_month-1)*30
        elif i in [9,10] and current_year%4!=0 and (current_year%100==0 or current_year % 400!=0) :
            current_year_days=current_day+3+(current_month-1)*30
        elif i in [11,12] and current_year%4!=0 and (current_year%100==0 or current_year % 400!=0) :
            current_year_days=current_day+4+(current_month-1)*30
        elif i == 3 and current_year%4!=0 and (current_year%100==0 or current_year % 400!=0) :
            current_year_days=current_day-1+(current_month-1)*30
    return(current_year_days)

name=input("Enter Your Name:")
birth_date=input("Enter your birth date in the following format DD/MM/YYYY: ")
birth_day=int(birth_date.split("/")[0])
birth_month=int(birth_date.split("/")[1])
birth_year=int(birth_date.split("/")[2])


current_date=input("Enter current date in the following format DD/MM/YYYY: ")
current_day=int(current_date.split("/")[0])
current_month=int(current_date.split("/")[1])
current_year=int(current_date.split("/")[2])


final=(part1(birth_day,birth_month,birth_year)+part2(birth_year,current_year)+part3(current_day,current_month,current_year))
print("Total Number of Days",name,"has survived:",final)
