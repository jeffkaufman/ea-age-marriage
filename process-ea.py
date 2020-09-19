import csv

counts = {}

with open("2018-ea-survey-anon-currencied-processed.csv") as inf:
    for row in csv.reader(inf):
        age = row[160]
        rel = row[64]

        if age == "age":
            continue

        if age == "NA" or rel == "NA" or rel == "Prefer not to answer":
            continue

        if rel in ["Married", "Widowed", "Divorced", "Separated"]:
            rel = "Ever Married"

        if rel == "In a relationship (monogamous)":
            rel = "mono relationship"

        if rel == "In a relationship(s) (polyamorous)":
            rel = "poly relationship(s)"
        
        if age not in counts:
            counts[age] = {}

        if rel not in counts[age]:
            counts[age][rel] = 0
            
        counts[age][rel] += 1

for age, age_counts in sorted(counts.items()):
    total = sum(age_counts.values())
    for rel, count in sorted(age_counts.items()):
        print("%s\t%s\t%.2f%%\t%s" % (rel, age, count / total * 100, count))
