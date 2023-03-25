from django.forms import ModelForm
from .views import Pins
from .models import Comments

class PinsForm(ModelForm):
    class Meta:
        model = Pins
        fields = (
            'pic_name', 'pic_description', 'image', 'category', 'user', 'slug'
        )


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'