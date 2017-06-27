from django.db import models

import datetime
from django.utils import timezone
import hashlib, random, string

class User(models.Model):
    username = models.CharField(max_length=50) # login name
    lower_name = models.CharField(max_length=50) # login name in lower-case
    password = models.CharField(max_length=128) # hash(originalPassword, staticSalt), generated at frontend
    password_salt = models.CharField(max_length=8) # (password, salt) pattern

    is_active = models.BooleanField()
    is_admin = models.BooleanField() # teacher or something

    register_time = models.DateTimeField("register time")

    nickname = models.CharField(max_length=50) # display name
    email = models.EmailField() # login email
    info = models.ForeignKey('UserInfo', on_delete=models.CASCADE) # Has avatar as foreign key
    avatar = models.ForeignKey('Avatar', on_delete=models.CASCADE) # Has user info as foreign key

    @staticmethod
    def newUser(username, saltedPassword, staticSalt):
        userInfo = UserInfo(school='')
        userInfo.save()
        avatar = Avatar(img='avatar/default.png')
        avatar.save()
        user = User(username=username, lower_name=username.lower(),
                    password=saltedPassword, password_salt=staticSalt,
                    is_active=True, is_admin=False,
                    register_time=timezone.now(),
                    nickname='',
                    email='',
                    info=userInfo,
                    avatar=avatar)
        user.save()
        return user

    def setPassword(self, saltedPassword, staticSalt): # saltedPassword leak may be dangerous
        self.password = saltedPassword
        self.password_salt = staticSalt

    def checkPassword(self, dynamicSaltedSaltedPassword, dynamicSalt):
        return dynamicSaltedSaltedPassword == hashlib.sha512((self.password + dynamicSalt).encode('utf8')).hexdigest()

    @staticmethod
    def mksalt():
        return ''.join(random.sample(string.ascii_letters + string.digits, 8))

    @staticmethod
    def isLoggedIn(request):
        if 'loginState' in request.session and request.session['loginState']:
            return True
        else:
            return False

    def __str__(self):
        return self.username

# User's external info
class UserInfo(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    school = models.CharField(max_length=512)

# User's avatar as User's foreign key
class Avatar(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    img = models.ImageField(upload_to='avatar', default='avatar/default.png')