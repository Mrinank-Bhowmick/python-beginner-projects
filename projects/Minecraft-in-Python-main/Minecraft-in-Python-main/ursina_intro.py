from ursina import *

# Test Cube
class Test_cube(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'cube',
			texture = 'white_cube',
			rotation = Vec3(45,45,45))

# Test button
class Test_button(Button):
	def __init__(self,scale = 0.1):
		super().__init__(
			parent = scene,
			model = 'cube',
			texture = 'brick',
			color = color.white,
			highlight_color = color.red,
			pressed_color = color.lime)

	def input(self,key):
		if self.hovered:
			if key == 'left mouse down':
				punch_sound.play()


# update is run every frame
def update():
	#print('test')
	if held_keys['a']:
		cube.x -= 1 * time.dt

# basic window
app = Ursina()

# basic cube 
cube = Entity(model='quad', color=color.orange, scale = (2,5), position = (5,1))

# quad with texture
#sans_image = load_texture('Sans.png')
#sans = Entity(model = 'quad', texture = sans_image)
#sans = Entity(model = 'quad', texture = 'Sans.png')

# creating a block properly
test = Test_cube()

# creating a button
btn = Test_button()
punch_sound = Audio('assets/punch', loop=False, autoplay=False)

app.run()

