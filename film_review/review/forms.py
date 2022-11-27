from django import forms


class ReviewForm(forms.Form):
    movie = forms.CharField(max_length=255, required=True, label='Фильм',
                            widget=forms.TextInput(attrs={'class': 'form-input'}))
    review = forms.CharField(widget=forms.Textarea(
        attrs={'cols': 60, 'rows': 10, 'class': 'textarea'}), label='Отзыв', required=True)
