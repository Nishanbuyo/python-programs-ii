class Mario:
    def __init__(self, life, level, obstacle,point=0):
        self.life = life
        self.level = level
        self.obstacle = obstacle
        self.point = point
        
    def move_forward(self):
        self.point+=1
        if self.obstacle==False:
            print("Move Forward")
            
        else:
            self.jump()



    def jump(self):
        print("Jump")

    def game_over(self, life):
        if life ==0:
            print("Game Over")
            return True
        else:
            print("Continue")
            return False

    def hit_by_enemy(self, life):
        self.life-=1

    def detect_obstacle(self):
        self.obstacle = not self.obstacle

mario_object = Mario(4, 0, False)

while mario_object.game_over(mario_object.life)==False:
    mario_object.move_forward()
    mario_object.hit_by_enemy(mario_object.life)
    mario_object.detect_obstacle()

print("Your point is ", mario_object.point)




