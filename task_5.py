# Yandex_test
import csv
from math import isclose
from datetime import datetime

def query_stats(file_name):
	with open(file_name) as inf:
		csv_iter =  csv.reader(inf)
		next(csv_iter)
		user_dict = {}
		for user_line in csv_iter:
			username = user_line[1]
			if not username: 
				continue
			if username in user_dict:
				user_dict[username] += 1
			else:
				user_dict[username] = 1
	return user_dict
	
def data_stats(file_name):
	with open(file_name) as inf:
		csv_iter =  csv.reader(inf)
		next(csv_iter)
		user_dict = {}
		for user_line in csv_iter:
			username = user_line[1]
			bytes = int(user_line[7])
			if not username:
				continue		
			if username in user_dict:
				user_dict[username] += bytes
			else:
				user_dict[username] = bytes
	return user_dict

def user_time(file_name):
	with open(file_name) as inf:
		csv_iter =  csv.reader(inf)
		next(csv_iter)
		user_dict = {}
		for user_line in csv_iter:
			username = user_line[1]
			time = datetime.strptime(user_line[0],'%Y-%m-%dT%H:%M:%S.%f%z')
			if not username:
				continue
			if username in user_dict:
				user_dict[username] += [str(time)]
			else:
				user_dict[username] = [str(time)]
	return user_dict
	
query_stats = query_stats('shkib.csv')
data_stats = data_stats('shkib.csv')

sorted_query_stats = sorted(query_stats, key = lambda k: query_stats[k], reverse = True)
sorted_data_stats = sorted(data_stats, key = lambda k: data_stats[k], reverse = True)

top_query_stats = [sorted_query_stats[i] for i in range(0,5)]
top_data_stats = [sorted_data_stats[i] for i in range(0,5)]

user_time = user_time('shkib.csv')
