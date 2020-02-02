from django import forms


class keyConnectForm(forms.Form):
    channel_name = forms.CharField(label='Enter key to connect')
    person_name = forms.CharField(label="Person name(anything)")
