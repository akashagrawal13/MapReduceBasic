import MapReduce
import sys

"""
Matrix multiplication in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    i=0
    while i<5:
		if record[0]=='a':
			mr.emit_intermediate((record[1], i), (record[0], record[2], record[3]))
		else:
			mr.emit_intermediate((i, record[2]), (record[0], record[1], record[3]))
		i+=1

def reducer(key, list_of_values):
    l1=[elem for elem in list_of_values if elem[0]=='a']
    l2=[elem for elem in list_of_values if elem[0]=='b']
    sum=0
    for elem1 in l1:
		#flag=0
		for elem2 in l2:
			if elem1[1]==elem2[1]:
				sum+=elem1[2]*elem2[2]
				#flag=1
				break
    f=open("output.txt","a")
    f.write(str(key)+" "+str(sum))
    f.write("\n")
    mr.emit((key+(sum, )))
	

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
