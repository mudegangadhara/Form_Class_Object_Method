from django import forms




class StudentForms(forms.Form):
    Name = forms.CharField(max_length=100)
    Age = forms.IntegerField()
    Email=forms.EmailField()
    Re_Enter_Email=forms.EmailField()
    botcatcher=forms.CharField(max_length=20,required=False,widget=forms.HiddenInput)
    

    def clean(self):
        na=self.cleaned_data['Name']
        if na[0].lower()=='m':
            raise forms.ValidationError('invalid name')
        
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError('botcatcher must be greater than 0')
    def clean(self):
        e=self.cleaned_data['Email']
        r=self.cleaned_data['Re_Enter_Email']
        if e!=r:
            raise forms.ValidationError('Re_Enter_Email must be a valid email address')