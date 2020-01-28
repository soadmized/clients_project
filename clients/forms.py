from django import forms


class ClientsFilterForm(forms.Form):

        ordering = forms.ChoiceField(label='sort', required=False, choices=[
            ['last', 'from A-Z'],
            ['first', 'from A-Z'],
            ['age', 'from bigger'],
            ['-age', 'from smallest'],
        ])
