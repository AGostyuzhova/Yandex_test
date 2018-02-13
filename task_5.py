# Yandex_test
with open('shkib1.csv') as inf:
	user_list = []
	for line in inf:
		repeat = False
		user_line = line.split(',')
		if not user_list:
			user_stat = {'User_ip':user_line[2],'Count':1,'Bytes_Sum':int(user_line[7])}
			user_list.append(user_stat)
		else:
			for user in user_list:		
				if (user_line[2] == user['User_ip']):
					user['Count'] += 1
					user['Bytes_Sum'] += int(user_line[7])
					repeat = True
			if repeat == False:
				user_stat = {'User_ip':user_line[2],'Count':1,'Bytes_Sum':int(user_line[7])}
				user_list.append(user_stat)
for user in user_list: print (user)
print (len(user_list))
