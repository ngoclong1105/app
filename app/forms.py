from .models import CustomUser

from django import forms

from .models import Comic

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email','mobile')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username','email','mobile')


class ComicForm(forms.ModelForm):

    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    image = forms.ImageField(label='Ảnh sản phẩm', required=False)
        
    class Meta:
        model = Comic
        fields = ('code', 'name', 'description', 'unitPrice')

        error_messages = {
            "code" : {
                "unique" : "Mã sản phẩm đã tồn tại"
            }
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        id = self.cleaned_data.get('id')

        if id == None and image == None:
            raise forms.ValidationError('Cần chọn ảnh sản phẩm')

        return image
    
    def save(self):
        comic = super().save()
        image = self.cleaned_data['image']

        if image and image.name:
            comic.saveImage(image)

class PaymentForm(forms.Form):
    fullname = forms.CharField(label='Họ và tên')
    mobile = forms.CharField(label='Số điện thoại')
    email = forms.EmailField(label='Email')
    address = forms.CharField(label='Địa chỉ')
