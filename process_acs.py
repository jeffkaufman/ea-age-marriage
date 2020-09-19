import csv
from collections import defaultdict

#"PERWT","AGE","YRMARR","EDUC","EDUCD"
#75.0,19,0,6,65


total = defaultdict(lambda : defaultdict(float))
marry = defaultdict(lambda : defaultdict(float))

educations = set()

with open("usa_acs_2018_2.csv") as inf:
    for row in csv.reader(inf):
        perwt, age, yrmarr, educ, educd = row
        if perwt == "PERWT":
            continue

        perwt = float(perwt) / 100
        age = int(age)
        married = int(yrmarr) > 0
        educd = int(educd)

        education = "Other"
        if educd == 101:
            education = "Bachelors"
        elif educd == 114:
            education = "Masters"
        elif educd == 116:
            education = "Doctoral"

        if age < 18:
            continue

        educations.add(education)
        
        total[age][education] += perwt
        if married:
            marry[age][education] += perwt

row = ["age"]
for education in sorted(educations):
    row.append(education)
print("\t".join(row))
            
for age in sorted(total):
    row = [str(age)]
    
    for education in sorted(educations):
        if not total[age][education]:
            row.append("na")
        else:
            row.append("%.2f%%" % (100 * marry[age][education] / total[age][education]))

    print("\t".join(row))
