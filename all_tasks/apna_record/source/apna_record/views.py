from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import requests, csv, uuid, os.path, pandas as pd
from django.db import connection


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
@renderer_classes([TemplateHTMLRenderer])
def show_records(request):
    file_name = 'apna_records.csv'
    data = pd.read_csv(file_name, skipinitialspace=True, usecols=['Name', 'Roll Number', 'Age', 'Gender'])
    data_html = data.to_html(index=False)
    final_data = {'loaded_data': data_html}
    return render(request, 'show_record_template.html', final_data)

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
@renderer_classes([TemplateHTMLRenderer])
def add_record(request):
    cols_list = ['Id', 'Name', 'Roll Number', 'Age', 'Gender']
    vals_objs = request.POST.values()
    vals_list = []
    for v in vals_objs:
        vals_list.append(v)
    file_name = 'apna_records.csv'
    if len(vals_list):
        unique_id = []
        unique_id.append(uuid.uuid1())
        vals_list = unique_id + vals_list
        if not os.path.exists(file_name):
            with open(file_name, 'a') as writefile:
                csvwriter = csv.writer(writefile)
                csvwriter.writerow(cols_list)
                csvwriter.writerow(vals_list)
        else:
            with open(file_name, 'a') as writefile:
                csvwriter = csv.writer(writefile)
                csvwriter.writerow(vals_list)
    return render(request, 'add_record_template.html')
