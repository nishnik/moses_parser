class Moses_parser(object):
	_parse_dict = {}
	_assignment = {}
	str_list = []
		
	def parse(self, str_name):
		with open(str_name) as f:
			self.str_list = f.readlines()
		return m._parse()
		
	def _parse(self):
		for i in range(len(self.str_list)):
			stripped = self.str_list[i].strip()
			if(stripped):
				if stripped[0] == '#':
					self._parse_dict[i] = "comment"
				elif "if" in stripped:
					self._parse_dict[i] = "condition"
				elif "echo" in stripped:
					self._parse_dict[i] = "printing"
				elif self.str_list[i].find('=') != -1:
					a = self.str_list[i].find('=')
					if(self.str_list[i][a+1] == "=" or self.str_list[i][a-1] == "!"):
						self._parse_dict[i] = "something else"
					else:
						self._parse_dict[i] = "assignment"
						self._assignment[i] = [self.str_list[i][:a], self.str_list[i][a+1:]]
				else:
					self._parse_dict[i] = "something else"
			else:
				self._parse_dict[i] = "newline"
		return self._parse_dict, self._assignment

	def options(self):
		lis = []
		for i,j in self._assignment.values():
			lis.append(i.strip())
		return lis
	
	def value_of(self, str_in):
		for a, i in self._assignment.items():
			if(i[0].strip() == str_in):
				print (i[1])
				break
	
	def change_value(self, str_in, str_out):
		for a, i in self._assignment.items():
			if(i[0].strip() == str_in):
				i[1] = '"' + str_out + '"' + "\n"
				break

	def write(self, fname):
		f = open(fname, 'w')
		for i in range((len(self.str_list))):
			if(self._parse_dict[i] != "assignment"):
				f.write(self.str_list[i])
			else:
				f.write(self._assignment[i][0] + "=" + self._assignment[i][1])
		f.close()

	def show_params(self):
		for i in self._assignment.values():
			print (i[0].strip() + " -> " + i[1])


m = Moses_parser()
m.parse("mt-location-1.00")
print ("\nWe can change the following options:\n")
for i in m.options():
	print (i)
print ("\nWe have the following parameters set:\n")
m.show_params()
print ("\nNow we change `mtdir` to `$HOME/Desktop`\n")
m.change_value("mtdir", "$HOME/Desktop")
print ("\nNow `mtdir` has value: ")
m.value_of("mtdir")
print ("\nAnd we have the following parameters set:\n")
m.show_params()
print ("Now we write it to a file named `mt-location-1.00(new)`")
m.write("mt-location-1.00(new)")