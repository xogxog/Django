from django import forms
from django.forms.widgets import TextInput, Textarea
from .models import Artist , Albums


class ArtistForm(forms.ModelForm) :
    name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs = {
                'class' : 'member-name form-control',
                'placeholder' : 'Enter the name',
                'maxlength' : 20,
                'style' : 'width : 400px;',
            }
        ),
        error_messages={
            'required': '이름은 필수 항목입니다.'
        }   
    )
    birth = forms.CharField(
        label='년/월/일',
        widget=forms.TextInput(
            attrs = {
                'class' : 'member-birth form-control',
                'placeholder' : 'Enter the birth',
                'maxlength' : 50,
                'style' : 'width : 400px;',
            }
        ),
        error_messages={
            'required': '생년/월/일은 필수 항목입니다.'
        }

    )
    height = forms.CharField(
        label = '키',
        widget=forms.TextInput(
            attrs = {
                'class' : 'member-height form-control',
                'placeholder' : 'Enter the birth',
                'maxlength' : 10,
                'style' : 'width : 400px;',
            }
        )
    )
    image = forms.FileField(
        label ='프로필사진',
        widget=forms.ClearableFileInput(
            attrs = {
                'class' : 'member-porfile form-control',
                'placeholder' : 'Enter the member image',
                'maxlength' : 500,
                'style' : 'width : 400px;',
            }
        )
    )
    content = forms.CharField(
        label ='내용',
        widget=Textarea(
                attrs = {
                'class' : 'member-content form-control',
                'placeholder' : 'Enter the member picture url',
                'rows': 5,
                'cols': 50,
                'style' : 'width : 400px;',
            }
        )
    )
    
    class Meta :
        model = Artist
        fields = '__all__'
        # exclude = ('None',)



class AlbumsForm(forms.ModelForm) :
    title = forms.CharField(
        label='앨범 이름',
        widget=forms.TextInput(
            attrs = {
                'class' : 'album-title form-control',
                'placeholder' : 'Enter the title',
                'maxlength' : 50,
                'style' : 'width : 300px;',
            }
        ),
        error_messages={
            'required': '타이틀 곡 필수!'
        }   
    )

    released = forms.CharField(
        label='발매일',
        widget=forms.TextInput(
            attrs = {
                'class' : 'album-released-date form-control',
                'placeholder' : 'Enter the released date',
                'maxlength' : 50,
                'style' : 'width : 300px;',
            }
        ),
        error_messages={
            'required': '필수!'
        }   
    )

    singer = forms.CharField(
        label='가수',
        widget=forms.TextInput(
            attrs = {
                'class' : 'album-singer form-control',
                'placeholder' : 'Enter the singer',
                'maxlength' : 30,
                'style' : 'width : 300px; ',
            }
        ),
        error_messages={
            'required': '필수!'
        }   
    )
    album_cover = forms.FileField(
        label='앨범커버',
        widget=forms.ClearableFileInput(
            attrs = {
                'class' : 'album-cover form-control',
                'placeholder' : 'album-cover required',
                'maxlength' : 300,
                'style' : 'width : 300px; ',
            }
        ),
        error_messages={
            'required': '앨범커버필수!'
        }   
    )


    class Meta :
        model = Albums
        fields = '__all__'