from django.shortcuts import render, redirect
from .models import Clue

def crossword_view(request):
    across_clues = Clue.objects.filter(direction='ACROSS').order_by('number')
    down_clues = Clue.objects.filter(direction='DOWN').order_by('number')
    context = {
        'across_clues': across_clues,
        'down_clues': down_clues,
    }
    return render(request, 'crossword_app/crossword.html', context)

def validate_answer(request):
    if request.method == 'POST':
        final_answer = request.POST.get('final_answer')
        if final_answer.strip().lower() == 'thank you':
            return redirect('success')
        else:
            error_message = '回答が正しくありません。もう一度お試しください。'
            across_clues = Clue.objects.filter(direction='ACROSS').order_by('number')
            down_clues = Clue.objects.filter(direction='DOWN').order_by('number')
            context = {
                'across_clues': across_clues,
                'down_clues': down_clues,
                'error_message': error_message,
            }
            return render(request, 'crossword_app/crossword.html', context)
    else:
        return redirect('crossword')

def success_view(request):
    return render(request, 'crossword_app/success.html')
