from django.shortcuts import render
from .apps import ReviewConfig

from .forms import ReviewForm


def index(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            context = dict(**form.cleaned_data)
            text_stemmed = ReviewConfig.stem_text(context['review'])
            print(text_stemmed)
            if not text_stemmed:
                form.add_error(
                    'review', "Текст отзыва не подходит для анализа. Текст должен содержать англоязычные слова!")
                context['form'] = form
                return render(request, 'review/review.html', context=context)
            model = ReviewConfig.model
            review_score = model.predict([text_stemmed])[0]
            stars = [True] * review_score + [False] * (10 - review_score)
            context['review_score'] = review_score
            context['stars'] = stars
            return render(request, 'review/review_result.html', context=context)
        else:
            form.add_error(form.add_error(''))
    else:
        form = ReviewForm()
    context = {'form': form}
    return render(request, 'review/review.html', context=context)
