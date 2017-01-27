# 2*2*2 rubiks cube representation



rgw = flu = 0 # (0-th cube; front face)
gwr = luf = 1 # (0-th cube; left face)
wrg = ufl = 2 # (0-th cube; up face)

rwb = fur = 3 # (1-st cube; front face)
wbr = urf = 4 # (1-st cube; up face)
brw = rfu = 5 # (1-st cube; right face)

ryg = fdl = 6 # (2-nd cube; front face)
ygr = dlf = 7 # (2-nd cube; down face)
gry = lfd = 8 # (2-nd cube; left face)

rby = frd = 9 #  (3-rd cube; front face)
byr = rdf = 10 # (3-rd cube; right face)
yrb = dfr = 11 # (3-rd cube; down face)

owg = bul = 12 # (4-th cube; back face)
wgo = ulb = 13 # (4-th cube; up face)
gow = lbu = 14 # (4-th cube; left face)

obw = bru = 15 # (5-th cube; back face)
bwo = rub = 16 # (5-th cube; right face)
wob = ubr = 17 # (5-th cube; up face)

ogy = bld = 18 # (6-th cube; back face)
gyo = ldb = 19 # (6-th cube; left face)
yog = dbl = 20 # (6-th cube; down face)

oyb = bdr = 21 # (7-th cube; back face)
ybo = drb = 22 # (7-th cube; down face)
boy = rbd = 23 # (7-th cube; right face)

'''
7-th cube IS ALWAYS FIXED
INPUT IS TAKEN AFTER 7TH CUBE IS IN OYB ORIENTATION
'''
beg=[0,0]
end=[0,0]
bege=[0,0]
ende=[0,0]

'''
for
beg end
first is position next is level
'''

def update_beg_end(new):
	global beg,end
	if beg[1]==new.level:
		end[0]=end[0]+1
	if beg[1]==(new.level -1):
		beg[1]=new.level
		end[1]=new.level
		beg[0]=end[0]+1
		end[0]=beg[0]

def update_beg_end_end(new):
	global bege,ende
	if bege[1]==new.level:
		ende[0]=ende[0]+1
	if bege[1]== (new.level-1):
		bege[1]=new.level
		ende[1]=new.level
		bege[0]=ende[0]+1
		ende[0]=bege[0]		

colourlist=['r','g','w','r','w','b','r','y','g','r','b','y','o','w','g','o','b','w','o','g','y','o','y','b']

# Identity: equal to (0, 1, 2, ..., 23).
I = (flu, luf, ufl, fur, urf, rfu, fdl, dlf, lfd, frd, rdf, dfr, bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)
F = (fdl, dlf, lfd, flu, luf, ufl, frd, rdf, dfr, fur, urf, rfu, bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)
F3 = (fur, urf, rfu, frd, rdf, dfr, flu, luf, ufl, fdl, dlf, lfd, bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)
L = (ulb, lbu, bul, fur, urf, rfu, ufl, flu, luf, frd, rdf, dfr, dbl, bld, ldb, bru, rub, ubr, dlf, lfd, fdl, bdr, drb, rbd)
L3 = (dlf, lfd, fdl, fur, urf, rfu, dbl, bld, ldb, frd, rdf, dfr, ufl, flu, luf, bru, rub, ubr,  ulb, lbu, bul, bdr, drb, rbd)
U = (rfu, fur, urf, rub, ubr, bru, fdl, dlf, lfd, frd, rdf, dfr, luf, ufl, flu, lbu, bul, ulb, bld, ldb, dbl, bdr, drb, rbd)
U3 = (lbu, bul, ulb, luf, ufl, flu, fdl, dlf, lfd, frd, rdf, dfr, rub, ubr, bru,  rfu,  fur, urf, bld, ldb, dbl, bdr, drb, rbd)



def get_input_colors():
	print('enter the colours in order')
	user_input_lst=[]
	for x in range(24):
		print('enter the colour of postion',x)
		user_input_lst.append(input())
	return user_input_lst	

class rubik_cube_representation():
	global colourlist
	lst_of_already_reached_configurations=[colourlist]
	lst_containing_levels=[0]
	get_to_parent=['s']
	lst_of_already_reached_configurations_end=[colourlist]
	lst_containing_levels_end=[0]
	get_to_parent_end=['e']


	'''
	here lst_of_already_reached_configurations[x][0] holds the no of moves required to reach that configuration from the starting configuration
	'''
	def __init__(self):

		self.level = 0
		self.colourlist=[]

	def set_all_face_colours(self, user_input_lst):

		self.colourlist = user_input_lst
		self.lst_of_already_reached_configurations[0]=self.colourlist	

	def _1_front_face_rotated_clockwise(self,new):

		global beg
		global end
		if beg == [0,0]:
			beg=[1,1]
			end=[0,1]

		F = (fdl, dlf, lfd, flu, luf, ufl, frd, rdf, dfr, fur, urf, rfu, bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)
		new.colourlist = [self.colourlist[x] for x in F]
		
		if new.colourlist not in self.lst_of_already_reached_configurations:
			new.level=self.level + 1
			self.get_to_parent.append('F3')
			self.lst_of_already_reached_configurations.append(new.colourlist)
			self.lst_containing_levels.append(new.level)
			update_beg_end(new)		

	def _1_front_face_rotated_anticlockwise(self,new):

		F3 = (fur, urf, rfu, frd, rdf, dfr, flu, luf, ufl, fdl, dlf, lfd, bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)

		new.colourlist = [self.colourlist[x] for x in F3]
		if new.colourlist not in self.lst_of_already_reached_configurations:
			new.level=self.level + 1
			self.get_to_parent.append('F')
			self.lst_of_already_reached_configurations.append(new.colourlist)
			self.lst_containing_levels.append(new.level)
			update_beg_end(new)
	

	def _1_Left_face_rotated_clockwise(self,new):
		# Left face rotated clockwise.
		L = (ulb, lbu, bul, fur, urf, rfu, ufl, flu, luf, frd, rdf, dfr, dbl, bld, ldb, bru, rub, ubr, dlf, lfd, fdl, bdr, drb, rbd)

		new.colourlist = [self.colourlist[x] for x in L]
		if new.colourlist not in self.lst_of_already_reached_configurations:
			new.level=self.level + 1
			self.get_to_parent.append('L3')
			self.lst_of_already_reached_configurations.append(new.colourlist)
			self.lst_containing_levels.append(new.level)
			update_beg_end(new)


	def _1_Left_face_rotated_anticlockwise(self,new):
		# Left face rotated anticlockwise.
		L3 = (dlf, lfd, fdl, fur, urf, rfu, dbl, bld, ldb, frd, rdf, dfr, ufl, flu, luf, bru, rub, ubr,  ulb, lbu, bul, bdr, drb, rbd)
	  
		new.colourlist = [self.colourlist[x] for x in L3]
		if new.colourlist not in self.lst_of_already_reached_configurations:
			new.level=self.level + 1
			self.get_to_parent.append('L')
			self.lst_of_already_reached_configurations.append(new.colourlist)
			self.lst_containing_levels.append(new.level)
			update_beg_end(new)

	def _1_Upper_face_rotated_clockwise(self,new):
		# Upper face rotated clockwise.
		U = (rfu, fur, urf, rub, ubr, bru, fdl, dlf, lfd, frd, rdf, dfr, luf, ufl, flu, lbu, bul, ulb, bld, ldb, dbl, bdr, drb, rbd)

		new.colourlist = [self.colourlist[x] for x in U]
		if new.colourlist not in self.lst_of_already_reached_configurations:
			new.level=self.level + 1
			self.get_to_parent.append('U3')
			self.lst_of_already_reached_configurations.append(new.colourlist)
			self.lst_containing_levels.append(new.level)
			update_beg_end(new)

	def _1_Upper_face_rotated_anticlockwise(self,new):
		# Upper face rotated anticlockwise.
		U3 = (lbu, bul, ulb, luf, ufl, flu, fdl, dlf, lfd, frd, rdf, dfr, rub, ubr, bru,  rfu,  fur, urf, bld, ldb, dbl, bdr, drb, rbd)

		new.colourlist = [self.colourlist[x] for x in U3]
		if new.colourlist not in self.lst_of_already_reached_configurations:
			new.level=self.level + 1
			self.get_to_parent.append('U')
			self.lst_of_already_reached_configurations.append(new.colourlist)
			self.lst_containing_levels.append(new.level)
			update_beg_end(new)

	def call_all_moves(self,new):
		self._1_front_face_rotated_clockwise(new)
		self._1_front_face_rotated_anticlockwise(new)
		self._1_Left_face_rotated_clockwise(new)
		self._1_Left_face_rotated_anticlockwise(new)
		self._1_Upper_face_rotated_clockwise(new)
		self._1_Upper_face_rotated_anticlockwise(new)

	def _1_front_face_rotated_clockwise_end(self,new):
			global bege
			global ende
			if bege == [0,0]:
				bege=[1,1]
				ende=[0,1]

			F = (fdl, dlf, lfd, flu, luf, ufl, frd, rdf, dfr, fur, urf, rfu, bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)
			new.colourlist = [self.colourlist[x] for x in F]
			if new.colourlist not in self.lst_of_already_reached_configurations_end:
				new.level=self.level + 1
				self.get_to_parent_end.append('F3')
				self.lst_of_already_reached_configurations_end.append(new.colourlist)
				self.lst_containing_levels_end.append(new.level)
				update_beg_end_end(new)			
	def _1_front_face_rotated_anticlockwise_end(self,new):

		F3 = (fur, urf, rfu, frd, rdf, dfr, flu, luf, ufl, fdl, dlf, lfd, bul, ulb, lbu, bru, rub, ubr, bld, ldb, dbl, bdr, drb, rbd)

		new.colourlist = [self.colourlist[x] for x in F3]
		if new.colourlist not in self.lst_of_already_reached_configurations_end:
			new.level=self.level + 1
			self.get_to_parent_end.append('F')
			self.lst_of_already_reached_configurations_end.append(new.colourlist)
			self.lst_containing_levels_end.append(new.level)
			update_beg_end_end(new)
	

	def _1_Left_face_rotated_clockwise_end(self,new):
		# Left face rotated clockwise.
		L = (ulb, lbu, bul, fur, urf, rfu, ufl, flu, luf, frd, rdf, dfr, dbl, bld, ldb, bru, rub, ubr, dlf, lfd, fdl, bdr, drb, rbd)

		new.colourlist = [self.colourlist[x] for x in L]
		if new.colourlist not in self.lst_of_already_reached_configurations_end:
			new.level=self.level + 1
			self.get_to_parent_end.append('L3')
			self.lst_of_already_reached_configurations_end.append(new.colourlist)
			self.lst_containing_levels_end.append(new.level)
			update_beg_end_end(new)


	def _1_Left_face_rotated_anticlockwise_end(self,new):
		# Left face rotated anticlockwise.
		L3 = (dlf, lfd, fdl, fur, urf, rfu, dbl, bld, ldb, frd, rdf, dfr, ufl, flu, luf, bru, rub, ubr,  ulb, lbu, bul, bdr, drb, rbd)
	  
		new.colourlist = [self.colourlist[x] for x in L3]
		if new.colourlist not in self.lst_of_already_reached_configurations_end:
			new.level=self.level + 1
			self.get_to_parent_end.append('L')
			self.lst_of_already_reached_configurations_end.append(new.colourlist)
			self.lst_containing_levels_end.append(new.level)
			update_beg_end_end(new)

	def _1_Upper_face_rotated_clockwise_end(self,new):
		# Upper face rotated clockwise.
		U = (rfu, fur, urf, rub, ubr, bru, fdl, dlf, lfd, frd, rdf, dfr, luf, ufl, flu, lbu, bul, ulb, bld, ldb, dbl, bdr, drb, rbd)

		new.colourlist = [self.colourlist[x] for x in U]
		if new.colourlist not in self.lst_of_already_reached_configurations_end:
			new.level=self.level + 1
			self.get_to_parent_end.append('U3')
			self.lst_of_already_reached_configurations_end.append(new.colourlist)
			self.lst_containing_levels_end.append(new.level)
			update_beg_end_end(new)

	def _1_Upper_face_rotated_anticlockwise_end(self,new):
		# Upper face rotated anticlockwise.
		U3 = (lbu, bul, ulb, luf, ufl, flu, fdl, dlf, lfd, frd, rdf, dfr, rub, ubr, bru,  rfu,  fur, urf, bld, ldb, dbl, bdr, drb, rbd)
		new.colourlist = [self.colourlist[x] for x in U3]
		if new.colourlist not in self.lst_of_already_reached_configurations_end:
			new.level=self.level + 1
			self.get_to_parent_end.append('U')
			self.lst_of_already_reached_configurations_end.append(new.colourlist)
			self.lst_containing_levels_end.append(new.level)
			update_beg_end_end(new)

	def call_all_moves_end(self,new):
		self._1_front_face_rotated_clockwise_end(new)
		self._1_front_face_rotated_anticlockwise_end(new)
		self._1_Left_face_rotated_clockwise_end(new)
		self._1_Left_face_rotated_anticlockwise_end(new)
		self._1_Upper_face_rotated_clockwise_end(new)
		self._1_Upper_face_rotated_anticlockwise_end(new)

def initialise():
	global colourlist
	user_input_lst=get_input_colors()
	start = rubik_cube_representation()
	start.set_all_face_colours(user_input_lst)
	end = rubik_cube_representation()
	end.colourlist=colourlist
	return start,end

def solve(start,endm):
	global end,beg,ende,bege
	new = rubik_cube_representation()
	if(start.colourlist==endm.colourlist):
		print('it is done!')
		exit(0)
	print(beg)
	print(end)
	print(bege)
	print(ende)	
	start.call_all_moves(new)
	for x in range(beg[0],end[0]+1,1):
		for y in range(bege[0],ende[0]+1,1):
			print(beg)
			print(end)
			print(bege)
			print(ende)
			if start.lst_of_already_reached_configurations[x] == endm.lst_of_already_reached_configurations_end[y]:
				return x,y		
	endm.call_all_moves_end(new)
	for x in range(bege[0],ende[0]+1,1):
		for y in range(beg[0],end[0]+1,1):
			if endm.lst_of_already_reached_configurations_end[x] == start.lst_of_already_reached_configurations[y]:
				return y,x
	instance_start = rubik_cube_representation()
	instance_end = rubik_cube_representation()
	while(1):
		c=beg[0]-1
		b=beg[0]
		e=end[0]
		for x in range(b,e+1,1):
			instance_start.colourlist=start.lst_of_already_reached_configurations[x]
			instance_start.level=start.lst_containing_levels[x]
			instance_start.call_all_moves(new)
			print(beg)
			print(end)
			while(c<end[0]):
				c=c+1
				y=bege[0]		
				while(y<=ende[0]):
					if instance_start.lst_of_already_reached_configurations[c] == endm.lst_of_already_reached_configurations_end[y]:
						return c,y
					y=y+1	
		c=bege[0]-1
		b=bege[0]
		e=ende[0]
		for x in range(b,e+1,1):
			instance_end.colourlist=instance_end.lst_of_already_reached_configurations_end[x]
			instance_end.level=instance_end.lst_containing_levels_end[x]
			instance_end.call_all_moves_end(new)
			print(bege)
			print(ende)
			while(c<ende[0]):
				c=c+1
				y=beg[0]
				while(y<=end[0]):
					if instance_start.lst_of_already_reached_configurations[y] == endm.lst_of_already_reached_configurations_end[c]:	
						return y,c
					y=y+1		




start=rubik_cube_representation()
endm=rubik_cube_representation()
start,endm=initialise()
start_index,end_index = solve(start,endm)
'''
front
'''
START_LIST=[]
END_LIST=[]

instance=rubik_cube_representation()
while start_index!=0:
	current_colourlist = instance.lst_of_already_reached_configurations[start_index]
	move=instance.get_to_parent[start_index]
	
	if move == 'F':
		temp = [current_colourlist[x] for x in F]
		start_index = instance.lst_of_already_reached_configurations.index(temp)
		START_LIST.append('F3')

	if move == 'F3':
		temp = [current_colourlist[x] for x in F3]
		start_index = instance.lst_of_already_reached_configurations.index(temp)
		START_LIST.append('F')

	if move == 'L':
		temp = [current_colourlist[x] for x in L]
		start_index = instance.lst_of_already_reached_configurations.index(temp)
		START_LIST.append('L3')

	if move == 'L3':
		temp = [current_colourlist[x] for x in L3]
		start_index = instance.lst_of_already_reached_configurations.index(temp)
		START_LIST.append('L')

	if move == 'U':
		temp = [current_colourlist[x] for x in U]
		start_index = instance.lst_of_already_reached_configurations.index(temp)
		START_LIST.append('U3')

	if move == 'U3':	
		temp = [current_colourlist[x] for x in U3]
		start_index = instance.lst_of_already_reached_configurations.index(temp)
		START_LIST.append('U')

while end_index!=0:
	current_colourlist = instance.lst_of_already_reached_configurations_end[end_index]
	move=instance.get_to_parent[end_index]
	
	if move == 'F':
		temp = [current_colourlist[x] for x in F]
		end_index = instance.lst_of_already_reached_configurations_end.index(temp)
		END_LIST.append('F')

	if move == 'F3':
		temp = [current_colourlist[x] for x in F3]
		end_index = instance.lst_of_already_reached_configurations_end.index(temp)
		END_LIST.append('F3')

	if move == 'L':
		temp = [current_colourlist[x] for x in L]
		end_index = instance.lst_of_already_reached_configurations_end.index(temp)
		END_LIST.append('L')

	if move == 'L3':
		temp = [current_colourlist[x] for x in L3]
		end_index = instance.lst_of_already_reached_configurations_end.index(temp)
		END_LIST.append('L3')

	if move == 'U':
		temp = [current_colourlist[x] for x in U]
		end_index = instance.lst_of_already_reached_configurations_end.index(temp)
		END_LIST.append('U')

	if move == 'U3':	
		temp = [current_colourlist[x] for x in U3]
		end_index = instance.lst_of_already_reached_configurations_end.index(temp)
		END_LIST.append('U3')

START_LIST.reverse()
for x in END_LIST:
	START_LIST.append(x)

print(START_LIST)



