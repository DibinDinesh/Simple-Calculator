from django import forms


class RegistrationForm(forms.Form):

    username=forms.CharField()
        #creating object
        #username=reference name(variable name)
        #.charfield()=object name
    password=forms.CharField()

    email=forms.EmailField()




class BmrForm(forms.Form):

    weight=forms.IntegerField()

    height=forms.IntegerField()

    age=forms.IntegerField()

    options=(
        ("male","male"),
        ("female","female")
    )

    gender=forms.ChoiceField(choices=options)

    choices=(

        (1,"Sedentary"),
        (2,"LightlyActive"),
        (3,"ModerativelyActive"),
        (4,"VeryActive"),
        (5,"ExtraActive"),
    )

    activity_level=forms.ChoiceField(choices=choices)

    weight_loss_per_month=forms.IntegerField()

    target_weight=forms.IntegerField()


class TemperatureForm(forms.Form):

    temp_in_deg=forms.IntegerField(required=False)

    temp_in_fh=forms.IntegerField(required=False)