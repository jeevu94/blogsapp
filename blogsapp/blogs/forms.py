from ..utils.forms import AppModelForm
from .models import Blog


class BlogForm(AppModelForm):
    class Meta(AppModelForm.Meta):
        fields = [
            "cover_image",
            "title",
            "description",
            "ta_title",
            "ta_description",
        ]
        model = Blog

    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop("author")
        super().__init__(*args, **kwargs)
        self.fields["cover_image"].label = "Cover Photo"
        self.fields["ta_title"].label = "தலைப்பு"
        self.fields["ta_description"].label = "விளக்கம்"

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        return title
