import pygame
pygame.init()

display_width = 800
display_height = 600
BLACK = ( 0, 0, 0)
WHITE = ( 200, 200, 200)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

img = pygame.image.load('assets/hole.png')
balls = []
balls.append(img)
for x in range(1,7):
	img1 = pygame.image.load('assets/ball_'+str(x)+'.png')
	balls.append(img1)
pegs = []
for x in range(3):
	img1 = pygame.image.load('assets/peg_'+str(x)+'.png')
	pegs.append(img1)

game_display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
guesses = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
results = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
current_guess = [0,0,0,0]
current_color = 0
answer = [2,1,3,4]
turn = 0

def drawboard():
	for x in range(8):
		for y in range(4):
			l1 = 100+y*50
			l2 = 320+y*30
			t = 100+50*x
			game_display.blit(balls[guesses[x][y]],(l1,t))
			game_display.blit(pegs[results[x][y]],(l2,t))
	for x in range(6):
		l = 475+x*50
		t = 280
		game_display.blit(balls[x+1],(l,t))
	for x in range(4):
		l = 520+x*50
		t = 200
		game_display.blit(balls[current_guess[x]],(l,t))
	pygame.draw.rect(game_display, BLACK, (520, 400, 200, 50))

def click_ball(ball_no):
	print 'ball' + str(ball_no)
	global current_color
	current_color = ball_no

def click_slot(slot):
	global current_color
	print 'slot' + str(slot)
	if(current_color==0):
		return
	current_guess[slot] = current_color

	current_color = 0

def click_submit():
	global current_guess,guesses,turn,answer,results,current_color

	for x in range(4):
		if current_guess[x]==0:
			#generate a prompt
			return
	guesses[turn] = current_guess
	blacks = 0
	whites = 0
	freqa=[0,0,0,0,0,0]
	freqg=[0,0,0,0,0,0]

	for x in range(4):
		if answer[x]==current_guess[x]:
			blacks+=1
		else:
			freqa[answer[x]-1]+=1
			freqg[current_guess[x]-1]+=1
	for x in range(6):
		whites+=min(freqg[x],freqa[x])
	if blacks==4:
		print 'win'
		#success. player wins
	for x in range(4):
		if blacks!=0:
			results[turn][x] = 2
			blacks-=1
		elif whites!=0:
			results[turn][x] = 1
			whites-=1
	turn+=1
	current_color = 0
	current_guess = [0,0,0,0]

print 'lol'

while True:
	mx,my = 0,0
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		elif event.type == pygame.MOUSEBUTTONUP:
			mx,my = event.pos
			if mx>=475 and mx<=775 and my>=280 and my<=330:
				click_ball(int((mx-475)/50)+1)
			elif mx>=520 and mx<=720 and my>=200 and my<=250:
				click_slot(int((mx-520)/50))
			elif mx>=520 and mx<=720 and my>=400 and my<=450:
				click_submit()
	game_display.fill(WHITE)
	drawboard()
	pygame.display.flip()
	clock.tick(60)