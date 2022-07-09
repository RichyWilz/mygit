from django.forms import ModelForm
from .models import Borrow

class BorrowForm(ModelForm):
    class Meta:
        model = Borrow
        fields = [#'student_name',
            'book_title',
            'borrow_date',
            'return_date',
            'email_address',
            'fine',
        ]

