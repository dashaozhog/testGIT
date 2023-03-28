from models import *

background = transform.scale(image.load("background.jpg"), WIN_SETTING)
clock = time.Clock()

font.init()
fontlabel = font.SysFont("Terminal", 50)

# comment git


RED = (255,0,0)
GREEN = (0,255,0) 
WHITE = (255,255,255)

r1 = Player(paddle_IMG, 0,0, 15, "left")
r2 = Player(transform.flip(paddle_IMG, True, False), WIN_SETTING[0]-SPSIZE[0],0, 15, "right")

mixer.music.load('01 Time For A Smackdown.mp3')
mixer.music.play()
mixer.music.set_volume(0.2)
ball = Ball()
game = True
finish = False
while game:
	window.blit(background, (0,0))
	if not finish:
		r1.update_position()
		r2.update_position()
		player1_score = fontlabel.render(str(r1.score), True, WHITE)
		player2_score = fontlabel.render(str(r2.score), True, WHITE)
		ball.draw()
		ball.move(r1,r2)
		if ball.rect.x <= 0:
			mixer.Sound.play(game_over)
			r2.score +=1
			ball = Ball()
		if ball.rect.x >= WIN_SETTING[0]:
			mixer.Sound.play(game_over)
			r1.score+=1
			ball = Ball()
		window.blit(player1_score, (WIN_SETTING[0]/2-player1_score.get_width(), 0))
		window.blit(player2_score, (WIN_SETTING[0]/2+player2_score.get_width(), 0))
	for e in event.get():
		if e.type == QUIT:
			game = False
	clock.tick(FPS)
	display.update()

def menu():
	while True:
		window.blit()
	for e in event.get():
			if e.type == QUIT:
				quit()
				sys.exit()
