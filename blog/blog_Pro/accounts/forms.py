from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
# UserCreationForm: 기본 유저 생성 폼(pw1 pw2를 제공)

class SignUpForm(UserCreationForm):

    class Meta():
        # AUTH_USER_MODEL이라고 settings.py에 정의한 user모델을 가져온다는 의미
        model = get_user_model()
        fields = ['username', 'email', 'nickname']