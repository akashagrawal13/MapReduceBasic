import MapReduce
import sys

"""
Trimming DNA sequences in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value=record[1]
    l=len(value)
    value=value[:l-10]
    #value.append(record[0])
    #value.append(record[2:])
    #words = value.split()
    #for w in words:
    mr.emit_intermediate(value, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #total = 0
    #for v in list_of_values:
    #  total += v
    l=len(list_of_values)
    #print l
    i=1
    #nl=[]
    f=open("output.txt","a")
    #while i<l:
		#nl=[]
		#nl.append(str(list_of_values[0]))
		#nl.append(str(list_of_values[i]))
		#cs=''.join(nl[:])
		#list_of_values[0].extend(list_of_values[i])
		#nl=[]
		#nl.append(list_of_values[0]+list_of_values[i])
		#nl.append(list_of_values[i])
		#cs=str(list_of_values[0])
		#cs.join(str(list_of_values[i]))
		#f.write(str(list_of_values[0])+str(list_of_values[i])+"\n")
    f.write(key)
    f.write("\n")
		#mr.emit((str(list_of_values[0])+str(list_of_values[i])))
		#mr.emit((cs))
    mr.emit((key))
	#	i+=1

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
