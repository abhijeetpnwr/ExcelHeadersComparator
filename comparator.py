# Motive of program is to take 2 excel sheets and to compare them

import pyexcel as pe

records = pe.get_records(file_name="arab.xlsx")

firstfileheaders = []

for key in records[0]:
	firstfileheaders.append(key)

firstfileheaders.sort()


print "Total elements :",len(firstfileheaders)

records2 = pe.get_records(file_name="arab2.xlsx")

secondfileheaders = []

for key in records2[0]:
	secondfileheaders.append(key)

secondfileheaders.sort()

print "total elements in excel 2 :",len(secondfileheaders)

print "Elements not avail  in arab2  : ",set(firstfileheaders)-set(secondfileheaders)


