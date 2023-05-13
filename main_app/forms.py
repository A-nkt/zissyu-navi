from django import forms
from .models import Record, Contact, OtherRecord


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = (
            'hospital_name',
            'sex',
            'year',
            'major',
            'place',
            'url',
            'review',
            'review_people',
            'review_people_comment',
            'review_report',
            'review_report_comment',
            'review_communication',
            'review_communication_comment'
        )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'subject',
            'content'
        )


class OtherRecordForm(forms.ModelForm):
    class Meta:
        model = OtherRecord
        fields = (
            'info'
        )
