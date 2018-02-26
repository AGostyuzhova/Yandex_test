import csv
import sys

file = open('result.txt','w', encoding = 'utf-8')

def task_1(file_name):
	
	print('# Starting Task 1')
	
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
	sorted_query_stats = sorted(user_dict, key = lambda k: user_dict[k], reverse = True)
	
	print('# Saving results to results.txt')
	
	file.write('# Поиск 5ти пользователей, сгенерировавших наибольшее количество запросов\nРешение 1\n')
	for i in range(5):
		file.write('User: {};   Requests: {}\n'.format(sorted_query_stats[i], user_dict[sorted_query_stats[i]]))
	print('# Task 1 - Done')
	
def task_2(file_name):

	print('# Starting Task 2')
	
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
	sorted_data_stats = sorted(user_dict, key = lambda k: user_dict[k], reverse = True)
	
	print('# Saving results to results.txt')
	
	file.write('# Поиск 5ти пользователей, отправивших наибольшее количество данных\nРешение 2\n')
	for i in range(5):
		file.write('User: {};   Traffic: {}\n'.format(sorted_data_stats[i], user_dict[sorted_data_stats[i]]))
	print('# Task 2 - Done')
	
if __name__ == "__main__":
	try:
		if len (sys.argv) > 1:
			file_name = sys.argv[1]
			task_1(file_name)
			task_2(file_name)
		else:
			print('# Please run the program in the format: task_5.py file_name.csv')
	except FileNotFoundError:
		print('# The file {} does not exist. \n# Please run the program in the format: task_5.py file_name.csv'.format(file_name))
