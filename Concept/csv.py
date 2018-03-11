import csv
 
myfile = file("C:/my_python/new.txt",'w')
f = open("C:/my_python/service_field.csv")
reader = csv.reader(f)
for c1,c2 in reader:
    for item in c2.split(','):
        print >> myfile, c1,item +"\n", 
f.close()
myfile.close()