import csv

counts = {}
totals = {}

genders = ["Female", "Male", "Other"]

with open("2018-ea-survey-anon-currencied-processed.csv") as inf:
    for row in csv.reader(inf):
        #for i, x in enumerate(row):
        #    print("%s: %s" % (i,x))
        #raise Exception("bp")
        
        age = row[160]
        rel = row[64]
        gender = row[53]
        religion = row[62]

        if age == "age":
            continue

        if gender not in ["Female", "Male"]:
            gender = "Other"
        
        if age == "NA" or rel == "NA" or rel == "Prefer not to answer":
            continue

        married = rel in ["Married", "Widowed", "Divorced", "Separated"]
        
        if age not in counts:
            counts[age] = {}
            totals[age] = {}
            for gender in genders:
                counts[age][gender] = 0
                totals[age][gender] = 0
            
        totals[age][gender] += 1
        if married:
            counts[age][gender] += 1

row = ["age"]
row.extend(genders)
print("\t".join(row))
    
for age in sorted(totals):
    row = [str(age)]
    for gender in genders:
        row.append("%.0f%%" % (
            100.0 * counts[age][gender] / totals[age][gender]))
    print("\t".join(row))
