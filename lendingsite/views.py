from django.http import HttpResponse
from django.shortcuts import render
import random

def first_page(request):
    h1 = "<h1>Hello world</h1>"
    python_list = [
        "В", "этой", "статье", "будут", "рассмотрены", "популярные",
        "алгоритмы", "принципы", "их", "работы", "и", "реализация", "на", "Python",
        "А", "ещё", "сравним", "как", "быстро", "они", "сортируют", "элементы", "в", "списке",
        "В", "качестве", "общего", "примера", "возьмём", "сортировку", "чисел", "в", "порядке", "возрастания",
        "Но", "эти", "методы", "можно", "легко", "адаптировать", "под", "ваши", "потребности"
    ]
    text = random.sample(python_list, 10)
    text = " ,".join(word for word in text)
    return render(request, "./index.html", {
    "h1" : h1,
    "text" : text
    })