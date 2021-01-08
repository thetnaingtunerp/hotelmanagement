from django import forms

class AvailabilityForm(forms.Form):
    ROOM_CATEGORY = (
        ('AC','AC'),('NAC','NAC'),('KING','KING'),('QUEEN','QUEEN'),('DELUX','DELUX')
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORY, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M"])
    check_out = forms.DateTimeField(required=True, input_formats=["%Y-%m-%dT%H:%M"])