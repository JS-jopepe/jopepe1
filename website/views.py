from django.shortcuts import render

# Create your views here.
def home(request):
    nome = 'Jovenel'
    lema = 'Formando um futuro melhor'
    lista_de_cursos = [
        'Inglês',
        'Francês',
        'Informática',
        'Português',
    ]

    context = {
        'nome' : nome
        'lema' : lema
        'cursos' : lista_de_cursos
    }

    return render(request, 'home.html', context)

