from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Comma-separated tags")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        # Handle tags
        tag_names = [t.strip() for t in self.cleaned_data['tags'].split(',') if t.strip()]
        instance.tags.set([Tag.objects.get_or_create(name=name)[0] for name in tag_names])
        return instance
