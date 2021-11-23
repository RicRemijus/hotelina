from django import forms


class AvailableForm(forms.Form):
   # ROOM_CATEGORY = (
  #      ('AMB', 'AMBASSADORIAL SUIT'),
  #      ('EXE', 'EXECUTIVE ROOM'),
  #      ('STA', 'STANDARD ROOM'),
 #   )
 #   room_category = forms.ChoiceField(choices=ROOM_CATEGORY, required=True)
    check_in = forms.DateTimeField(
        required=True, input_formats=['%Y-%m-%d%T%H:%M:%S', ])
    check_out = forms.DateTimeField(
        required=True, input_formats=['%Y-%m-%d%T%H:%M:%S', ])
