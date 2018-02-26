import csv
 

def bankpay(csvfile):
#set a dictionary for Date revenue

	date_revenue={}
	# set variables to hold counters 
	month_count=0
	total_revenue=0
	prior_row=0
	monthly_change=0
	total_change=0

	with open(csvfile, newline="") as revenue_data:
		csvreader= csv.reader(revenue_data,delimiter=",")
		#skip header
		next(csvreader)
		for row in csvreader:
			csvDate= row[0]
			csvrevenue=row[1]
			month_count=month_count+1
			total_revenue=total_revenue+ int(csvrevenue)

			monthly_change=int(csvrevenue)-prior_row
			prior_row=int(csvrevenue)
		#Skip frist row 
			if(month_count >1):
		#Calculate monthly Change
				date_revenue[csvDate]= monthly_change
		#add up monthy cange and average 
		row_sum=(sum(date_revenue.values()))
		average=int(row_sum)/int(month_count)
		# grab max and min values  from date_revenue dictionary 
		max_date=max(date_revenue,key=date_revenue.get)
		max_revenue=date_revenue[max_date]
		min_date=min(date_revenue,key=date_revenue.get)
		min_revenue=date_revenue[min_date] 



	#output
	print ("Financial Analysis")
	print ("-------------------------")
	print("Total Months:"+str(month_count))
	print("Total Revenue:$"+str(total_revenue))
	print("Average Revenue Change: $" + str(int(average)))
	print("Greatest Increase in Revenue: " + str(max_date) + " " + "($ " + str(max_revenue) + ")")
	print("Greatest Decrease in Revenue: " + str(min_date) + " " + "($ " + str(min_revenue) + ")")

csvfile1= 'budget_data_1.csv'
csvfile2= 'budget_data_2.csv'
bankpay(csvfile1)
bankpay(csvfile2)



