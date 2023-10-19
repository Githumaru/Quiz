from django.http import HttpResponse
from .models import Quiz
import requests
from datetime import datetime

def create_quiz_entry(request, questions_num):
    for _ in range(questions_num):
        while True:
            response = requests.get('https://jservice.io/api/random?count=1')
            data = response.json()[0]
            if not Quiz.objects.filter(question=data['question']).exists():
                quiz = Quiz(id=data['id'], question=data['question'], answer=data['answer'], created_at=datetime.now())
                quiz.save()
                break
    return HttpResponse("Quiz entries created successfully.", content_type="text/plain")

def get_latest_quiz(request):
    try:
        latest_quiz = Quiz.objects.order_by('-created_at').first()
        return HttpResponse(f"id: {latest_quiz.id}"
                            f"\nquestion: {latest_quiz.question}"
                            f"\nanswer: {latest_quiz.answer}"
                            f"\ncreated_at: {latest_quiz.created_at.strftime('%d-%m-%Y %H:%M')}", content_type="text/plain")
    except AttributeError:
        return HttpResponse("")
# Create your views here.
