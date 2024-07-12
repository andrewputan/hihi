import pygame
import random
import time

# 初始化Pygame
pygame.init()

# 設置遊戲窗口
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Shooting Game")

# 設置顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 設置字體
font = pygame.font.Font(None, 36)

# 設置遊戲時鐘
clock = pygame.time.Clock()
start_time = None
game_duration = 50  # 遊戲持續時間（秒）
target_score = 35  # 目標分數
health_increase_chance = 0.05  # 增加生命值的機率


# 英雄角色
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (400, 500)
        self.speed = 5
        self.health = 3  # 初始生命值

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.right < 800:
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < 600:
            self.rect.y += self.speed

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()

    def increase_health(self):
        self.health += 1


# 子彈
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()


# 敵人
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 750)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > 600:
            self.kill()


# 生命值增加物品
class HealthPack(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.y += 3
        if self.rect.top > 600:
            self.kill()


# 敵人生成
def spawn_enemy():
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)


# 生命值增加物品生成
def spawn_health_pack():
    x = random.randint(0, 750)
    y = random.randint(-100, -40)
    health_pack = HealthPack(x, y)
    all_sprites.add(health_pack)
    health_packs.add(health_pack)


# 創建精靈組
all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
health_packs = pygame.sprite.Group()

player = Player()
all_sprites.add(player)
players.add(player)

score = 0
game_active = False
game_over = False


def reset_game():
    global score, start_time, game_active, game_over
    score = 0
    start_time = time.time()
    game_active = True
    game_over = False
    player.health = 3
    all_sprites.empty()
    players.empty()
    bullets.empty()
    enemies.empty()
    health_packs.empty()
    all_sprites.add(player)
    players.add(player)


def display_instructions():
    instructions = [
        "Game Rules:",
        "1. Use WASD keys to move the character.",
        "2. Use the left mouse button to shoot enemies.",
        "3. Reach 35 points within 50 seconds to win.",
        "4. Each time you collide with an enemy, you lose 1 health point. Initial health is 3.",
        "5. The game ends when your health reaches 0.",
        "6. Collect green health packs to increase your health.",
        "Press SPACE to start the game.",
    ]
    screen.fill(BLACK)
    for i, line in enumerate(instructions):
        text = font.render(line, True, WHITE)
        screen.blit(text, (50, 50 + i * 40))
    pygame.display.flip()


def display_game_over(message):
    screen.fill(BLACK)
    game_over_text = font.render(message, True, WHITE)
    replay_text = font.render("Press SPACE to play again", True, WHITE)
    screen.blit(game_over_text, (350, 250))
    screen.blit(replay_text, (300, 300))
    pygame.display.flip()


# 遊戲主循環
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_active:
                reset_game()
        elif event.type == pygame.MOUSEBUTTONDOWN and game_active:
            if event.button == 1:  # 左鍵
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

    if game_active:
        # 更新
        all_sprites.update()

        # 碰撞檢測
        hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
        for hit in hits:
            score += 1
            if random.random() < health_increase_chance:
                spawn_health_pack()

        # 玩家碰撞檢測
        player_hits = pygame.sprite.spritecollide(player, enemies, True)
        for hit in player_hits:
            player.take_damage()
            if player.health <= 0:
                game_active = False
                game_over = True

        # 玩家收集生命值增加物品
        health_pack_hits = pygame.sprite.spritecollide(player, health_packs, True)
        for hit in health_pack_hits:
            player.increase_health()

        # 生成敵人
        if random.random() < 0.02:
            spawn_enemy()

        # 檢查遊戲結束條件
        elapsed_time = int(time.time() - start_time)
        if elapsed_time >= game_duration or score >= target_score:
            game_active = False
            game_over = True

    # 繪製
    screen.fill(BLACK)
    all_sprites.draw(screen)

    if game_active:
        # 顯示分數和時間
        elapsed_time = int(time.time() - start_time)
        score_text = font.render(f"Score: {score}", True, WHITE)
        time_text = font.render(f"Time: {elapsed_time}", True, WHITE)
        health_text = font.render(f"Health: {player.health}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (10, 40))
        screen.blit(health_text, (10, 70))
    else:
        if game_over:
            if score >= target_score:
                display_game_over("You Win!")
            else:
                display_game_over("Game Over")
        else:
            display_instructions()

    pygame.display.flip()

    # 控制遊戲速度
    clock.tick(60)

pygame.quit()
