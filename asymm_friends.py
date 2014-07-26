import MapReduce
import sys

"""
Asymmetric friends in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line
dict={}

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    #key.append(value)
    #value.append(key)
    mr.emit_intermediate((key, value), 1)
    #record.reverse()
    mr.emit_intermediate((value, key), 1)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    #file=open("output.txt", "a")
    for v in list_of_values:
		total += v
    if total==1:
		#file.write(key)
		#file.write("\n")
		mr.emit((key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
