import csv
import os
from datetime import datetime
#set a function for two csvfiles
def bankboss(csvfile):


#List data:
	Emp_ID=[]
	Frist_Name=[]
	Last_Name=[]
	DOB=[]
	SSN=[]
	State=[]



#State Abbreviations
	Stat_abbrev= {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',}

	with open(csvfile)as emp_data:
		csvreader= csv.reader(emp_data, delimiter=",")
	#skip header
		next(csvreader)

		for row in csvreader:
			Emp_ID.append(row[0])

#Split full name in to first name and last name
			Full_Name= row[1].split(" ")
			Frist_Name.append(Full_Name[0])
			Last_Name.append(Full_Name[1])

#Convert DOB from YYYY-MM-DD to MM/DD/YYYY
			csvDOB= datetime.strptime(row[2],"%Y-%m-%d").strftime("%m/%d/%Y")
			DOB.append(csvDOB)

#Convert SSN 
			csvSSN= row[3]
			csvSSN= csvSSN[-4:]
			SSN.append("***-**-" + csvSSN)
#Convert full state to abbreavative state 
			csvState=row[4]
			State.append(Stat_abbrev[csvState])

#Zip lists
	cleaned_csv= zip(Emp_ID,Frist_Name,Last_Name,DOB,SSN,State)
	print(cleaned_csv)
#set output file
	output_file= os.path.join("paybossoutput.csv")
	with open (output_file,'w',newline='')as datafile:
		writer= csv.writer(datafile)
		writer.writerow(["Emp ID","Frist Name","Last Name","DOB","SSN","State"])
		writer.writerows(cleaned_csv)

csvfile1= 'employee_data1.csv'
csvfile2= 'employee_data2.csv'
bankboss(csvfile1)
bankboss(csvfile2)