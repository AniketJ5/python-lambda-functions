num = [10,70]
sqr = []
filter_records = []

sqr = list(map(lambda x : x*x,num))
print(sqr)

filter_records = list(filter(lambda x : x>40,num))
print(filter_records)