from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import QuoteForm
from .models import Quote

@login_required
def request_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            return redirect('dashboard')
    else:
        form = QuoteForm()
    return render(request, 'quotes/request_quote.html', {'form': form})

@login_required
def my_quotes(request):
    quotes = Quote.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'quotes/my_quotes.html', {'quotes': quotes})