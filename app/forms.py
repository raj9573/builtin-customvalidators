from django import forms 

from django.core.validators import MaxValueValidator,MinValueValidator,MaxLengthValidator,MinLengthValidator,RegexValidator


from django.core.exceptions import ValidationError
def name_validate(value):


    if len(value)>7:
        

        raise ValidationError("Length Exceeded")


def minlength(value):


    if len(value)<3:

        raise ValidationError("Length is too small")



class userform(forms.Form):

    # name =  forms.CharField(validators= [MaxLengthValidator(7),
    # MinLengthValidator(3),
    # RegexValidator(r'^[a-zA-Z]*$')])
    # age =  forms.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])


    
    # name =  forms.CharField(max_length=10,validators = [name_validate,minlength])
    
    
    name =  forms.CharField(max_length=10)


    age =  forms.IntegerField()


    bot = forms.CharField(max_length=1,widget = forms.HiddenInput,required=False)

    # widget={'bot':forms.HiddenInput}


    


    def clean(self):

        n = self.cleaned_data['name']

        if len(n) <3:


            raise ValidationError("Length is too small")


    def clean_bot(self):
        if len(self.cleaned_data['bot'])>1:


            raise ValidationError("Bot catched")

            




