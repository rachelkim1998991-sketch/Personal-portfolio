from django import forms
from .models import Message

INPUT = "w-full rounded border border-gray-300 px-3 py-2 focus:outline-none focus:ring-2 focus:ring-purple-500"

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "text"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Ismingiz", "class": INPUT}),
            "email": forms.EmailInput(attrs={"placeholder": "Email manzilingiz", "class": INPUT}),
            "text": forms.Textarea(attrs={"placeholder": "Xabaringiz", "rows": 5, "class": INPUT}),
        }