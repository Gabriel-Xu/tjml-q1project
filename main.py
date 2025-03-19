data=[row.split(';') for row in open("cpd-crash-incidents.csv").read().strip().split("\n")]
print(len(data))
new_data=[]
to_delete=["tamainid", "records", "fatality", "year", "possblinj", "lat", "lon", "location_description", "tract", "contributing_factor", "vehicle_type", "ta_date", "crash_date", "geo_location"]
for row in data:
  a=[]
  for i, x in enumerate(row):
    if data[0][i] not in to_delete:
      a.append(x)
  if a[-3]=="Yes": a.append("fatalities")
  elif a[-2]=="Yes": a.append("injury")
  else: a.append("crash")
  a=a[:-4]+a[-2:]
  new_data.append(a)
new_data[0][-1]="class"

for i in range(len(new_data)):
  for j in range(len(new_data[0])):
    if new_data[i][j] in ["NONE", "OTHER *", "UNKNOWN"]:
      new_data[i][j]=""
    if new_data[i][j]=="" and j==13:
      new_data[i][j]="0"

for i in range(1, len(new_data)):
  count=0
  for j in range(len(new_data[0])):
    if new_data[0][j][:-1]=="vehicle" and new_data[i][j]!="":
      count+=1
  new_data[i]=new_data[i][:-1]+[count]+new_data[i][-1:]
new_data[0]=new_data[0][:-1]+["vehicles"]+new_data[0][-1:]

for i in range(1, len(new_data)):
  for j in range(len(new_data[0])):
    if new_data[0][j]=="ta_time":
      new_time=int(new_data[i][j][:new_data[i][j].index(':')])
      if new_data[i][j][-2:]=="PM":
        if new_time!=12:
          new_time+=12
      elif new_time==12:
        new_time=0
      new_data[i][j]=new_time

print(new_data[0])
print(len(new_data))

with open("new_dataset.csv", "w") as f:
  for row in new_data:
    f.write(";".join(map(str, row))+"\n")
