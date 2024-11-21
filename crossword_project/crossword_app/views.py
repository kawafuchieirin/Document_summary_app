from django.shortcuts import render, redirect, reverse

def crossword_view(request):
    crossword_data = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "c", "l", "o", "u", "d", "f", "r", "o", "n", "t", "#", "p"],
        ["#", "d", "#", "p", "#", "o", "#", "#", "#", "#", "#", "#", "r"],
        ["#", "k", "#", "e", "#", "c", "#", "#", "#", "#", "#", "#", "o"],
        ["#", "#", "#", "n", "q", "u", "i", "c", "k", "s", "i", "h", "t"],
        ["#", "#", "s", "#", "m", "#", "#", "#", "#", "#", "#", "#", "o"],
        ["#", "#", "e", "#", "e", "#", "#", "#", "#", "#", "c", "f", "n"],
        ["#", "#", "r", "#", "n", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["v", "p", "c", "#", "t", "#", "#", "w", "#", "#", "#", "#", "#"],
        ["#", "#", "h", "#", "d", "y", "n", "a", "m", "o", "d", "b", "#"],
        ["#", "#", "#", "#", "b", "#", "#", "f", "#", "#", "#", "#", "#"]
    ]
    
    return render(request, 'crossword_app/crossword.html', {'crossword_data': crossword_data})

def validate_answer(request):
    if request.method == 'POST':
        # ユーザーの回答を取得して処理する（例として 'cloudfront' と比較）
        answer = "".join([request.POST.get(f'answer{i}', '').lower() for i in range(1, 10)])
        if answer == 'cloudfront':  # 正解の回答と比較
            return redirect('success')  # 正解の場合は成功ページへリダイレクト
        else:
            return redirect(reverse('crossword') + '?error=Incorrect answer')  # 不正解の場合はエラーメッセージを表示
    return redirect('crossword')

def success_view(request):
    return render(request, 'crossword_app/success.html')
