from django.shortcuts import render, get_object_or_404
from .models import Course, Question, Submission, Enrollment

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    # Lấy đáp án user chọn
    selected_ids = []
    for question in course.question_set.all():
        choice_id = request.POST.get(f'choice_{question.id}')
        if choice_id:
            selected_ids.append(choice_id)
    
    # Ở đây thường có logic lưu Submission và chấm điểm, sau đó redirect
    # Ví dụ mock đơn giản:
    return show_exam_result(request, course_id, selected_ids)

def show_exam_result(request, course_id, selected_ids=None):
    course = get_object_or_404(Course, pk=course_id)
    context = {
        'course': course,
        'score': 100, # Mock score
        'passed': True
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
