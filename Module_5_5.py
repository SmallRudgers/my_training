from time import sleep

class User:

    def __init__(self,nickname,password,age):
        self.nick = nickname
        self.psw = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nick}, {self.psw}, {self.age}'

class Video:

    def __init__(self,title,duration,adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult = adult_mode

    def __str__(self):
        return f'{self.title}'

class UrTube:

    all_users = []
    all_videos = []

    def __init__(self, current_user=None):
        self.currentUser = current_user

    def log_in(self,nickname, password):
        n = 0
        for i in self.all_users:
            if nickname == i.nick and hash(password) == i.psw:
                self.currentUser = i
                print(f'Добро пожаловать, {i.nick}')
                n+=1
                break

        if n == 0:
            print(f'Указанный пользователь не найден или введен неверный пароль!')



    def register(self, nickname,password,age):
        n = 0
        for i in self.all_users:
            if i.nick == nickname:
                n+=1

        if n >=1:
            print(f'Пользователь с ником "{nickname}" уже существует!')
        else:
            new_user = User(nickname, password, age)
            self.currentUser = new_user
            self.all_users.append(new_user)

    def log_out(self):
        self.currentUser = None


    def add(self, *other):
        if self.all_videos == []:
            for i in other:
                self.all_videos.append(i)

        else:
            for i in other:
                n = 0
                for k in self.all_videos:
                    if k.title == i.title:
                        n+=1

                if n == 0:
                    self.all_videos.append(i)


    def get_video(self,serch):
        n = 0
        for i in self.all_videos:
            if serch.upper() in i.title.upper():
                if n == 0:
                    n+=1
                    print('Найденые видео:')
                print(i)


    def watch_video(self,serch):
        if self.currentUser != None:
            for i in self.all_videos:
                if serch.upper() in i.title.upper():
                    if i.adult == True and self.currentUser.age >= 18:
                        print(f'Воспроизводится: {i}')
                        for k in range(i.duration):
                            print(k+1)
                            sleep(1)
                        print('Конец видео')

                    elif i.adult == True and self.currentUser.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')

                    else:
                        print(f'Воспроизводится: {i}')
                        for k in range(i.duration):
                            print(k+1)
                            sleep(1)
                        print('Конец видео')

        else:
            print("Войдите в аккаунт, чтобы смотреть видео")





v1 = Video('Лучший язык программирования 2024 года', 5)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Пью воду 10ч', 10000)
ur = UrTube()


ur.register('Вася','2123',23)
ur.register('Вася','2213463',21)
ur.register('Вова','2fH23',16)

print(ur.currentUser.nick) #Активный пользователь
ur.log_in('Вася','2123')
print(ur.currentUser.nick,'\n') #Активный пользователь
ur.log_out()

ur.add(v1, v2)
ur.add(v1, v3)
for i in ur.all_videos:
    print(i)

print('\n')
ur.get_video('Програм')

print('\n')

ur.log_in('Вова','2fH23')
ur.watch_video('Для чего девушкам парень программист?')
print('\n')
ur.watch_video('Лучший язык программирования 2024 года')










