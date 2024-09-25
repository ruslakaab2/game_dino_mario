import pygame

# Загружаем изображение для экрана "Game Over"
gameover = pygame.image.load('photo/text/gameover.png')

# Инициализация переменных
rocket_conter_speed = 0
score = 0
af1 = True  # Флаг для направления движения влево
af2 = False  # Флаг для направления движения вправо
rocket_y_limit = True  # Ограничение по высоте ракеты (не используется)
gameplay = True  # Флаг для игрового процесса
rocket_spawn = []  # Список для хранения ракет
clock = pygame.time.Clock()  # Создаем объект часов для управления FPS
rocket = pygame.image.load('photo/rocket.png')  # Загружаем изображение ракеты
rocket_x = 1050  # Начальная позиция ракеты по оси X
player_dam = 0  # Урон игрока
speed_player = 10  # Скорость движения игрока
run_player = 150  # Позиция игрока по оси X
rocket_y = 500  # Начальная позиция ракеты по оси Y
rocket_conter_y = 0  # Счетчик для управления высотой ракеты
time_spawn_rocket = 0  # Счетчик времени для спавна ракет
speed_rocket = 15  # Скорость ракеты
pygame.init()  # Инициализация Pygame
screen = pygame.display.set_mode((1000, 563))  # Создаем окно игры
fon_mus = pygame.mixer.Sound('sound/fon_mus.mp3')  # Загружаем фоновую музыку
fon_mus.play()  # Запускаем фоновую музыку
time1 = 4000  # Время спавна ракет
a = True  # Флаг для статистики
runn = False  # Флаг для основного цикла
icon = pygame.image.load('photo/icon.png')  # Загружаем иконку игры

# Загружаем анимацию движения игрока влево
walk_left = [pygame.image.load('photo/left/1.png').convert_alpha(),
             pygame.image.load('photo/left/2.png').convert_alpha(),
             pygame.image.load('photo/left/1.png').convert_alpha(),
             pygame.image.load('photo/left/2.png').convert_alpha()
             ]

# Загружаем анимацию движения игрока вправо
walk_right = [pygame.image.load('photo/right/1.png').convert_alpha(),
              pygame.image.load('photo/right/2.png').convert_alpha(),
              pygame.image.load('photo/right/1.png').convert_alpha(),
              pygame.image.load('photo/right/2.png').convert_alpha()
              ]

# Инициализация переменных для анимации и прыжков
player_walk = 0  # Индекс текущего кадра анимации
player_jump = 500  # Высота прыжка
player_max_jump = 7  # Максимальная высота прыжка
player_jum = False  # Флаг для состояния прыжка
pygame.display.set_icon(icon)  # Устанавливаем иконку окна
fon = pygame.image.load('photo/afon.png').convert_alpha()  # Загружаем фоновое изображение
pygame.display.update()  # Обновляем экран

# Счетчик для выживания
survive_score = 0
rocket_timer = pygame.USEREVENT + 1  # Создаем пользовательское событие
pygame.time.set_timer(rocket_timer, time1)  # Устанавливаем таймер для спавна ракет

# Основной игровой цикл
while runn == False:
    player_rect = walk_left[0].get_rect(topleft=(run_player, player_jump))  # Создаем прямоугольник для игрока
    keys = pygame.key.get_pressed()  # Получаем состояние клавиш

    if gameplay == True:  # Если игра идет
        screen.blit(fon, (0, 0))  # Отображаем фон

        # Отображаем ракеты и проверяем столкновения
        if rocket_spawn:
            for (i, es) in enumerate(rocket_spawn):
                screen.blit(rocket, es)  # Отображаем ракету
                es.x -= speed_rocket  # Двигаем ракету влево
                if es.x < -150:  # Если ракета вышла за экран
                    rocket_spawn.pop(i)  # Удаляем ракету из списка
                if player_rect.colliderect(es):  # Проверка на столкновение с игроком
                    player_dam += 1  # Увеличиваем урон игрока

        # Управление движением игрока
        if keys[pygame.K_LEFT]:
            af1 = True
            af2 = False
            screen.blit(walk_left[player_walk], (run_player, player_jump))  # Движение влево
        elif keys[pygame.K_RIGHT]:
            af1 = False
            af2 = True
            screen.blit(walk_right[player_walk], (run_player, player_jump))  # Движение вправо
        else:
            # Если игрок не двигается, показываем статичное изображение
            if af1 == True and af2 == False:
                screen.blit(walk_left[0], (run_player, player_jump))
            if af1 == False and af2 == True:
                screen.blit(walk_right[0], (run_player, player_jump))

        # Управление прыжком игрока
        if not player_jum:
            if keys[pygame.K_UP]:  # Если нажата клавиша "вверх"
                player_jum = True  # Начинаем прыжок
        else:
            if player_max_jump >= -7:  # Если игрок еще в прыжке
                if player_max_jump > 0:
                    player_jump -= (player_max_jump**2) / 2  # Поднимаем игрока
                else:
                    player_jump += (player_max_jump**2) / 2  # Опускаем игрока
                player_max_jump -= 1  # Уменьшаем счетчик прыжка
            else:
                player_jum = False  # Завершаем прыжок
                player_max_jump = 7  # Сбрасываем максимальную высоту прыжка

        # Проверка на конец игры
        if player_dam == 3:
            gameplay = False  # Если игрок получил 3 урона, игра заканчивается

    pygame.display.update()  # Обновляем экран
    keys = pygame.key.get_pressed()  # Получаем состояние клавиш

    # Движение игрока по горизонтали
    if keys[pygame.K_LEFT] and run_player > 10:
        run_player -= speed_player
    elif keys[pygame.K_RIGHT] and run_player < 970:
        run_player += speed_player

    # Обновление анимации
    if player_walk == 3:
        player_walk = 0
    else:
        player_walk += 1

    # Увеличение скорости ракет
    if rocket_conter_speed == 3:
        speed_rocket += 5
        rocket_conter_speed = 0

    # Управление высотой ракеты
    if rocket_y > 480:
        if rocket_conter_y == 10:
            rocket_y -= 5
            rocket_conter_y = 0

    # Уменьшение времени спавна ракет
    if time1 > 500:
        if time_spawn_rocket == 5:
            time1 -= 500
            time_spawn_rocket = 0

    pygame.display.update()  # Обновляем экран

    if gameplay:  # Если игра идет
        for event1 in pygame.event.get():
            if event1.type == rocket_timer:  # Если сработал таймер спавна ракет
                score += 50  # Увеличиваем счет
                survive_score += 50  # Увеличиваем счет выживания
                rocket_conter_y += 1  # Увеличиваем счетчик для высоты ракеты
                rocket_conter_speed += 1  # Увеличиваем счетчик скорости
                time_spawn_rocket += 1  # Увеличиваем счетчик времени спавна
                print('ваша статисика : ', score)  # Выводим статистику
                print('скорость', speed_rocket)  # Выводим скорость
                print('урон от 1 до 3 ', player_dam)  # Выводим урон
                player_dam = 0  # Сбрасываем урон
                rocket_spawn.append(rocket.get_rect(topleft=(rocket_x, rocket_y)))  # Спавним новую ракету
    else:
        if a:
            print('ваша статисика : ', score)  # Выводим статистику в конце игры
            a = False

    # Обработка событий Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Если пользователь закрыл окно
            running = True  # Устанавливаем флаг для выхода
            pygame.quit()  # Завершаем Pygame

    clock.tick(15)  # Ограничиваем FPS до 15
