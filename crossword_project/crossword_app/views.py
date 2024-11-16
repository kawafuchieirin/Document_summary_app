# crossword_app/views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import AcrossClue, DownClue

def crossword_view(request):
    across_clues = AcrossClue.objects.all()
    down_clues = DownClue.objects.all()
    error_message = request.GET.get('error', None)

    # グリッド構造
    grid_structure = [
        [1, 2, 3, 4],
        [0, 5, 1, 1],
        [6, 7, 1, 8],
        [9, 10, 0, 1],
        [11, 1, 1, 1],
    ]

    return render(request, 'crossword_app/crossword.html', {
        'across_clues': across_clues,
        'down_clues': down_clues,
        'error_message': error_message,
        'grid_structure': grid_structure,
    })

def validate_answer(request):
    if request.method == 'POST':
        answer = "".join([request.POST.get(f'answer{i}', '') for i in range(1, 5)])
        if answer.lower() == 'thank':
            return redirect('success')
        else:
            return redirect(reverse('crossword_puzzle') + '?error=Incorrect answer')
    return redirect('crossword_puzzle')

def success_view(request):
    return render(request, 'crossword_app/success.html')
