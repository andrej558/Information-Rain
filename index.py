import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Media Literacy Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Player
player_size = 50
player_rect = pygame.Rect((width - player_size) // 2, height - 2 * player_size, player_size, player_size)
player_speed = 10

# Trustworthy Information
trust_info_width = 50
trust_info_height = 30
trust_info_speed = 5
trust_info_list = []

# Fake News
fake_news_width = 50
fake_news_height = 30
fake_news_speed = 7
fake_news_list = []

# Number of falling boxes
num_boxes = 5

# Score
score = 0

# Function to draw the player
def draw_player():
    pygame.draw.rect(screen, green, player_rect)

# Function to draw trustworthy information
def draw_trust_info(x, y):
    pygame.draw.rect(screen, blue, [x, y, trust_info_width, trust_info_height])

# Function to draw fake news
def draw_fake_news(x, y):
    pygame.draw.rect(screen, red, [x, y, fake_news_width, fake_news_height])

# Function to display the score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, [10, 10])

# Initialize trustworthy information and fake news
def initialize_elements():
    trust_info_list.clear()
    fake_news_list.clear()
    for _ in range(num_boxes):
        trust_info_list.append([random.randint(0, width - trust_info_width), random.randint(-height, 0)])
        fake_news_list.append([random.randint(0, width - fake_news_width), random.randint(-height, 0)])

# Game loop
def game():
    global player_rect, score

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT] and player_rect.right < width:
            player_rect.x += player_speed

        # Update trustworthy information
        for trust_info in trust_info_list:
            trust_info[1] += trust_info_speed
            trust_rect = pygame.Rect(trust_info[0], trust_info[1], trust_info_width, trust_info_height)
            if trust_info[1] > height:
                trust_info[1] = random.randint(-height, 0)
                trust_info[0] = random.randint(0, width - trust_info_width)

        # Update fake news
        for fake_news in fake_news_list:
            fake_news[1] += fake_news_speed
            fake_rect = pygame.Rect(fake_news[0], fake_news[1], fake_news_width, fake_news_height)
            if fake_news[1] > height:
                fake_news[1] = random.randint(-height, 0)
                fake_news[0] = random.randint(0, width - fake_news_width)

        # Check for collisions with trustworthy information
        for trust_info in trust_info_list:
            trust_rect = pygame.Rect(trust_info[0], trust_info[1], trust_info_width, trust_info_height)
            if player_rect.colliderect(trust_rect):
                trust_info[1] = random.randint(-height, 0)
                trust_info[0] = random.randint(0, width - trust_info_width)
                score += 1

        # Check for collisions with fake news
        for fake_news in fake_news_list:
            fake_rect = pygame.Rect(fake_news[0], fake_news[1], fake_news_width, fake_news_height)
            if player_rect.colliderect(fake_rect):
                fake_news[1] = random.randint(-height, 0)
                fake_news[0] = random.randint(0, width - fake_news_width)
                score -= 1

        # Draw the game elements
        screen.fill(white)
        draw_player()
        display_score(score)

        for trust_info in trust_info_list:
            draw_trust_info(trust_info[0], trust_info[1])

        for fake_news in fake_news_list:
            draw_fake_news(fake_news[0], fake_news[1])

        pygame.display.flip()
        clock.tick(60)  # Limit the frame rate to 60 frames per second

# Initialize trustworthy information and fake news
initialize_elements()

# Run the game
game()
