import sys
count=0
total=0
for i in sys.stdin:
  total+=float(i.strip())
  count+= 1
print(f"bio_data_average : {total/count}")
