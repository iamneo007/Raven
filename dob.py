dob = input('enter the date of birth in YYYY-MM-DD-HRSformat : \n ')
date_parts = dob.split('-')
[year,month,day,HRS] = date_parts

#calculate the date timestap in years;
dob_timestamp = float(year) + float(month)/12 + float(day)/365 + float(HRS)/8640

#calculate the today,s timestamp in years

[today_year, today_month, today_day , today_HRS] = ['2017' , '03' ,'17' , '11']
today_timestrap = float(today_year) + float(today_month)/12 + float(today_day)/365 + float(today_HRS)/8640

#compute the difference
years=today_timestrap - dob_timestamp
months = (years - int(years)) * 12
day = (months - int(months)) * 30
HRS = (day - int(day)) * 24

print('your age is %d years %d months %d day %d HRS'% (years , months , day , HRS))

