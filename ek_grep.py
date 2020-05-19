import sys

def main():
	''' 
	
	'''
	iflag = vflag = cflag = string = False
	
	ctr = 1
	files =[]
	flags = []
	for i in range(1, len(sys.argv)):
		if sys.argv[i][0] == '-':
			for j in range(1, len(sys.argv[i])):
				if sys.argv[i][j] == 'i':
					iflag = True
					flags.append('i')
				elif sys.argv[i][j] == 'v':
					vflag = True
					flags.append('v')
				elif sys.argv[i][j] == 'c':
					cflag = True
					flags.append('c')
				else:
					sys.stderr.write(f'unknown command: {sys.argv[i][j]} \n')
					
			ctr +=1
		else:
			if string == False:
				string = sys.argv[i]
				#print(type(string))
				#print(sys.argv[i])
	ctr += 1
	#print(sys.argv[ctr])	
	#print(sys.argv[ctr:])
	#print(ctr)
	while ctr < len(sys.argv):
		try:
			files.append(open(sys.argv[ctr], 'r'))
		except:
			sys.stderr.write('invalid filename \n')
			return
		ctr += 1

	#print(f'files are {files}, file2 {file2}')
	#print(sys.argv)
	#print(ctr)
	grep(flags, string, files)


	
def grep(flags, string, files):
	'''
	i -> case sensitive
	v -> invert(counts non pattern)
	c -> counts of all mathing lines
	ci -> prints counts of matching lines and non matching lines
	'''
	#print(files)
	if string == False:
		sys.stderr.write(f'need string input\n')
		return

	open_files = list(files)
	
	match_name = []
	output = False
	if len(files)  == 0:
		open_files.append(sys.stdin)
	
	for file in open_files:
		matching = []
		for line in file:
			if 'i' in flags:
				if 'v' in flags:
					if string.lower() not in line.lower():
						matching.append(line)
						#match_name.append(f'{file.name}:{(line)}')
				else:
					if string.lower() in line.lower():
						matching.append(line)
						#match_name.append(f'{file.name}:{(line)}')
						#sys.stdout.write(line)
			else:
				if 'v' in flags:
					if string not in line:
						matching.append(line)
						#match_name.append(f'{file.name}:{(line)}')
				else:
					if string in line:
						matching.append(line)
						#match_name.append(f'{file.name}:{(line)}')
						
		if 'c' in flags:
			#print(matching)
			#print(match_name)

			if len(files) > 1:
				output = f'{file.name}:{len(matching)}\n'
				sys.stdout.write(output)
			else:	
				#if string in line:
				#matching.append(line)
				output = len(matching)
				sys.stdout.write(f'{output}\n')
				

		else:
			#print(open_files)
			#print(files)
			#print(match_name)
			if len(files) > 1:
				for item in matching:
					sys.stdout.write(f'{file.name}:{item}')
			else:
				for item in matching:
					sys.stdout.write(f'{item}')

	if len(files) != 0:
		for file in open_files:
			file.close()
	

if __name__ == '__main__':
	main()