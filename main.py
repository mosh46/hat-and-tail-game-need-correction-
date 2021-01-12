import random
class hat_tail_game:
	hat_tail = ['hat','tail']
	bat_ball_choice = ['bat','ball']
	player_score = 0
	comp_score = 0
	p_target = 0
	c_target = 0
	win = 0
	lose = 0
	draw = 0
	balls_for_bat = 0
	balls_for_ball = 0
	def __init__(self, names):
		self.name = names

	def for_highscore(self, highscore):
		with open('high_score.txt','w') as f:
			print('you have achieved highscore')
			f.write(f'{highscore}\n')
			f.write(f'{self.name} make {highscore} runs in {self.balls_for_bat} balls')
	def hat_tail_choice(self):
		rand = random.choice(self.hat_tail)
		bat_ball = random.choice(self.bat_ball_choice)
		input1 = input('please enter your choice hat or tail ;')
		if rand == input1:
			input2 = input('you won the toss what do you want to do bat or ball ;')
			if input2 == 'bat':
				self.for_bat()
				self.for_ball()
			elif input2 == 'ball':
				self.for_ball()
				self.for_bat()
			else:
				print('invalid input')
				self.hat_tail_choice()
		else:
			print(f'you lose the toss and computer chooses to do {bat_ball}')
			if bat_ball == 'bat':
				self.for_ball()
				self.for_bat()
			elif bat_ball == 'ball':
				self.for_bat()
				self.for_ball()
			
	def high_check(self, score):
		with open('high_score.txt', 'r') as f:
			b = f.readline()
			if score > int(b):
				self.for_highscore(score)
		
	def for_ball(self):					
		out = False
		while out == False:
			
			comp_choice = random.randint(1,6)
			
			try:
				input_ball = int(input('\nits your ball choose a number from 1 to 6 ; '))
			except Exception as e:
				print(e)
				self.for_ball()
				
			print(f'computer_choice is {comp_choice}')
			self.balls_for_ball += 1
			if self.p_target > 0:
				if self.comp_score > self.p_target:
					self.lose+= 1
					print(f'you lose the match {self.lose} times')
					break
			if (comp_choice == input_ball):
				if self.p_target > 0:
					if self.comp_score > self.p_target:
						self.lose +=1
						
						print(f'computer won the match {self.lose} times')
						break
					elif self.comp_score == self.player_score:
						self.draw += 1										
						print(f'the match is draw {self.draw} times')
					else:
						self.win += 1
						
						print(f'you win the match {self.win} times')
				else:
					print('computet is out')
					self.c_target = self.comp_score+1
					print(f'computer total is {self.comp_score} and target to you  is {self.c_target}')
				out = True
			else:
				if (input_ball > 6):
					print('please choose from 1 to 6')
				elif (input_ball < 0):
					print('please choose from 1 to 6')
				
				else:
					self.comp_score += comp_choice
					print(f'batsman run: {self.comp_score} ')
					print(f'balls : {self.balls_for_ball}')
					
	def for_bat(self):					
		out = False
		while out == False:
			
			comp_choice = random.randint(1,6)
			try:
				input_bat = int(input('\nits your bat choose a number from 1 to 6 ; '))
			except Exception as e:
				print(e)
				self.for_bat()
			
			print(f'computer_choice is {comp_choice}')
			self.balls_for_bat += 1
			if self.c_target > 0:
				if self.player_score > self.c_target:
					self.win += 1
					
					print(f'you win the match {self.win} times')
					self.high_check(self.player_score)
					break
			if (comp_choice == input_bat):
				if self.c_target > 0:
					if self.player_score > self.c_target:
						self.win += 1
						
						print(f'you win the match {self.win} times')
						self.high_check(self.player_score)
						break
					elif self.player_score == self.comp_score:
						self.draw += 1
						
						print(f'the match is draw {self.draw} times')
															
					else:
						self.lose += 1
						
						print(f'you lose the match {self.lose} times')
				else:
					print('you are out')
					self.high_check(self.player_score)
					self.p_target = self.player_score+1
					print(f'your total is {self.player_score} and target to computer is {self.p_target}')
				out = True
			else:
				if (input_bat > 6):
					print('please choose from 1 to 6')
				elif (input_bat < 0):
					print('please choose from 1 to 6')
				
				else:
					self.player_score += input_bat
					if self.c_target > 0:
						if self.player_score > self.c_target:
							self.win +=1
					
					print(f'batsman run: {self.player_score} ')
					print(f'balls : {self.balls_for_bat}')
		
if __name__ =='__main__':
	print('\n\nWELCOME TO HAT AND TAIL GAME\n\n')
	user_name = input('please enter your name ;')
	while True:
		player = hat_tail_game(user_name)
		player.hat_tail_choice()
		
