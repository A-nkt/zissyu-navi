from django import forms
from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('hospital_name','sex','year','major','place','url','review','review_people','review_people_comment',
                    'review_report','review_report_comment','review_communication','review_communication_comment')
