from django.forms import Form, FileField


class TestPhotoUploadForm(Form):
    file = FileField(required=True)
