import statistics
def requests_time(f,text):
	f = open(f,"r")
	n = f.readlines()
	final = []	
	for i in n:
		final.append(float(i.strip('\n')))
	print(text + " the mean is: " + str(statistics.mean(final)))
	print(text + " the median is: " + str(statistics.median(final)))
requests_time("times1.txt","requests library")
requests_time("times2.txt","requests library with pagination")
requests_time("times3.txt","urllib3 library")
requests_time("times4.txt","urllib3 library with pagination")
