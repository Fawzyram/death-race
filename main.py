import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Racing Game")

# Load images
car_img = pygame.image.load("car.png")
car_img = pygame.transform.scale(car_img, (50, 100))  # Scale image to match player size

enemy_img = pygame.image.load("WhatsApp Image 2024-04-29 at 10.36.49 AM.jpeg")
enemy_img = pygame.transform.scale(enemy_img, (50, 100))  # Scale image to match enemy size

bullet_img = pygame.image.load("WhatsApp Image 2024-04-29 at 10.35.53 AM.jpeg")
bullet_img = pygame.transform.scale(bullet_img, (10, 20))  # Scale image to match bullet size

# Set up the player
player_width = 50
player_height = 100
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height - 50
player_speed = 5
player = pygame.Rect(player_x, player_y, player_width, player_height)

# Set up the enemies
enemy_width = 50
enemy_height = 100
enemy_speed = 3
enemy_list = []

# Set up bullets
bullet_width = 10
bullet_height = 20
bullet_speed = 7
bullet_list = []

# Set up score
score = 0
font = pygame.font.Font(None, 36)

# Set up game level
level = 1
max_enemies = 5

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Player shoots bullet when space key is pressed
                bullet_x = player.x + player.width // 2 - bullet_width // 2
                bullet_y = player.y
                bullet = pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
                bullet_list.append(bullet)

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < screen_width - player.width:
        player.x += player_speed

    # Move the enemies
    for enemy in enemy_list:
        enemy.y += enemy_speed
        if enemy.y > screen_height:
            enemy_list.remove(enemy)
            score -= 10  # Subtract points when enemy reaches the bottom
    # Generate new enemies randomly
    if len(enemy_list) < max_enemies:
        if random.randint(1, 100) == 1:
            enemy_x = random.randint(0, screen_width - enemy_width)
            enemy_y = -enemy_height
            enemy = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
            enemy_list.append(enemy)

    # Move the bullets
    for bullet in bullet_list:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullet_list.remove(bullet)

    # Check for collisions between player and enemies
    for enemy in enemy_list:
        if player.colliderect(enemy):
            running = False  # End the game when player collides with an enemy
            break

    # Check for collisions between bullets and enemies
    for bullet in bullet_list:
        for enemy in enemy_list:
            if bullet.colliderect(enemy):
                bullet_list.remove(bullet)
                enemy_list.remove(enemy)
                score += 10  # Increase score when bullet hits enemy

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player
    screen.blit(car_img, (player.x, player.y))

    # Draw the enemies
    for enemy in enemy_list:
        screen.blit(enemy_img, (enemy.x, enemy.y))

    # Draw the bullets
    for bullet in bullet_list:
        screen.blit(bullet_img, (bullet.x, bullet.y))

    # Display the score
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
