from django.shortcuts import render, redirect, get_object_or_404
from .models import Preamble, FundamentalRights, FundamentalDuties, DirectivePrinciples, UserFeedback
from .forms import UserFeedbackForm
from django.http import JsonResponse


# Home Page View
def index(request):
  return render(request, 'samvidhan/index.html')

def about(request):
    return render(request, 'samvidhan/about.html')

def games(request):
    return render(request, 'samvidhan/games.html')

def quiz(request):
    return render(request, 'samvidhan/quiz.html')

def interactive_learning(request):
    return render(request, 'samvidhan/learning.html')

def preamble(request):
    preamble = Preamble.objects.first()  # Fetch the first instance or adjust as needed
    return render(request, 'samvidhan/preamble.html', {'preamble': preamble})

def fundamental_rights(request):
    rights = FundamentalRights.objects.all()  # Fetch all instances of Fundamental Rights
    return render(request, 'samvidhan/fundamental_rights.html', {'rights': rights})

def fundamental_duties(request):
    duties = FundamentalDuties.objects.all()  # Fetch all Fundamental Duties from the database
    return render(request, 'samvidhan/fundamental_duties.html', {'duties': duties})

def directive_principles(request):
    principles = DirectivePrinciples.objects.all()  # Fetch all Directive Principles from the database
    return render(request, 'samvidhan/directive_principles.html', {'principles': principles})

def memorycards(request):
    return render(request, 'samvidhan/memorycards.html')

def stages(request):
    return render(request, 'samvidhan/stages.html')

def wheel(request):
    return render(request, 'samvidhan/wheel.html')

def feedback(request):
    if request.method == 'POST':
        form = UserFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')  # Redirect to a thank you page
    else:
        form = UserFeedbackForm()

    return render(request, 'samvidhan/feedback.html', {'form': form})

def thanks(request):
    return render(request, 'samvidhan/thanks.html')

def guess(request):
    return render(request, 'samvidhan/guess.html')


def wheel_article(request, article_name):
    # Define the template name based on the article_name passed in the URL
    template_name = f'wheel/{article_name}'
    return render(request, template_name)
   
