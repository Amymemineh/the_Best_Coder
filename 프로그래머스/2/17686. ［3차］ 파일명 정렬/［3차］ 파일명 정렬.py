def solution(files):
    answer = []
    return answer

import re
def solution(files):
		answer = []
		file_dict = {}    
		for f in files:   
				p = re.findall(r"\d+", f)[0]
				head = f[:f.index(p)].lower()
				number = int(p)
				file_dict[f] = (head, number)  
		file_list = file_dict.items()  
		file_list = sorted(file_list, key = lambda x: (x[1][0], x[1][1]))
		answer = [i[0] for i in file_list]

		return answer