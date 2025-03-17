info1={'first_name':'Leo','last_name':'Hua','location':'HK'}
info2={'first_name':'Andrew','last_name':'Ng','location':'US'}
info3={'first_name':'Roman','last_name':'Lau','location':'UK'}
peoples=[]

full_name1=f"{info1['first_name']} {info1['last_name']}"
full_name2=f"{info2['first_name']} {info2['last_name']}"
full_name3=f"{info3['first_name']} {info3['last_name']}"

peoples.append(full_name1)
peoples.append(full_name2)
peoples.append(full_name3)
print(peoples)

for people in peoples:
    print(people)