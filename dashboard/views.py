from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

import os
from dashboard.forms import UploadFileForm
from submit_data.models import Contribution
from utils.QueryHandler import handle_new_sdf


@login_required(redirect_field_name='next')
def dash_index(request):
    contributors = Contribution.objects.all()
    context = {
        'title': 'Dashboard',
        'contributors': contributors
    }
    return render(request, 'dashboard/dash.html', context=context)


@login_required(redirect_field_name='next')
def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_file(request.FILES['file'], request.POST['plant'])
            messages.success(request, "Upload File Successfully")
            return redirect('dashboard')

    messages.success(request, "File Upload Failed")
    return HttpResponse(
        "<h2>You are not permitted to view this page.</h2>"
    )


def show_submitted_files(request, cid):
    contribution = get_object_or_404(Contribution, pk=cid)
    new_df = handle_new_sdf(contribution.file, change_db=False)
    context = {
        'new_data': new_df.values.tolist(),
        'contributor': contribution.user.first_name + ' ' + contribution.user.last_name,
        'plant': contribution.plant_name
    }
    return render(request, 'dashboard/show_data.html', context=context)


# Not path view
def handle_file(f, plant=None):
    filename = f.__str__()

    if not os.path.isdir('media/upload'):
        os.mkdir('media')
        os.mkdir('media/upload')
    with open('media/upload/' + filename, 'wb') as des:
        for chunk in f.chunks():
            des.write(chunk)
    try:
        sdf_file = 'media/upload/' + filename
        handle_new_sdf(sdf_file, plant)
    finally:
        os.remove('media/upload/' + filename)
