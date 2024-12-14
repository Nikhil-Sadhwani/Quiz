from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, QuizSession, Answer
import random
from django.views.decorators.cache import cache_control

def start_quiz(request):
    questions = list(Question.objects.all())
    random.shuffle(questions)
    questions = questions[:10]

    quiz_session = QuizSession.objects.create(
        user="User",
        total_questions=len(questions)
    )

    request.session['quiz_session_id'] = quiz_session.id
    request.session['quiz_questions'] = [{'id': q.id, 'answered': False, 'answer': None} for q in questions]
    request.session['current_index'] = 0 

    return redirect('quiz:get_question')

def get_question(request):
    quiz_questions = request.session.get('quiz_questions', [])
    current_index = request.session.get('current_index', 0)

    if not quiz_questions:
        return redirect('quiz:start_quiz')

    if 0 <= current_index < len(quiz_questions):
        question_id = quiz_questions[current_index]['id']
        question = get_object_or_404(Question, id=question_id)

        context = {
            'question': {
                'id': question.id,
                'text': question.question_text,
                'options': {
                    'A': question.option_a,
                    'B': question.option_b,
                    'C': question.option_c,
                    'D': question.option_d,
                },
            },
            'current_index': current_index,
            'total_questions': len(quiz_questions),
            'question_range': range(len(quiz_questions)),
            'selected_option': quiz_questions[current_index]['answer'],
        }
        return render(request, 'question.html', context)
    else:
        return redirect('quiz:get_question')

def save_answer(request):
    if request.method == 'POST':
        selected_option = request.POST.get('selected_option')
        current_index = request.session.get('current_index', 0)
        quiz_questions = request.session.get('quiz_questions', [])

        if quiz_questions and 0 <= current_index < len(quiz_questions):
            quiz_questions[current_index]['answer'] = selected_option
            quiz_questions[current_index]['answered'] = True
            request.session['quiz_questions'] = quiz_questions

        action = request.POST.get('action', 'next')
        if action == 'next':
            request.session['current_index'] = min(current_index + 1, len(quiz_questions) - 1)
        elif action == 'previous':
            request.session['current_index'] = max(current_index - 1, 0)
        elif action == 'submit':
            return redirect('quiz:submit_quiz')
        else:
            request.session['current_index'] = int(action)

    return redirect('quiz:get_question')

def submit_quiz(request):
    quiz_session_id = request.session.get('quiz_session_id')
    quiz_questions = request.session.get('quiz_questions', [])

    if not quiz_session_id or not quiz_questions:
        return redirect('quiz:start_quiz')

    quiz_session = get_object_or_404(QuizSession, id=quiz_session_id)

    correct_answers = 0
    incorrect_answers = 0

    for item in quiz_questions:
        question = get_object_or_404(Question, id=item['id'])
        is_correct = (item['answer'].lower() == question.correct_option.lower()) if item['answer'] else False

        Answer.objects.create(
            quiz_session=quiz_session,
            question=question,
            selected_option=item['answer'] or '',
            is_correct=is_correct
        )

        if item['answer']:
            if is_correct:
                correct_answers += 1
            else:
                incorrect_answers += 1

    quiz_session.correct_answers = correct_answers
    quiz_session.incorrect_answers = incorrect_answers
    quiz_session.score = correct_answers/quiz_session.total_questions * 100
    quiz_session.save()

    request.session.pop('quiz_session_id', None)
    request.session.pop('quiz_questions', None)
    request.session.pop('current_index', None)

    context = {
        'total_questions': quiz_session.total_questions,
        'attempted': correct_answers + incorrect_answers,
        'correct': correct_answers,
        'incorrect': incorrect_answers,
        'skipped': quiz_session.total_questions - (correct_answers + incorrect_answers),
        'score': quiz_session.score,
    }
    return render(request, 'results.html', context)
