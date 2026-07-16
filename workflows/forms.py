from django import forms
from .models import GeneratedWorkflow


class GeneratedWorkflowForm(forms.ModelForm):
    class Meta:
        model = GeneratedWorkflow
        fields = ('prompt',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholder and set autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'prompt': 
            ('Describe the trigger, apps, actions, conditions, and desired result.'
            'Example: When someone submits a form, add their details to Google '
            'Sheets, send a confirmation email and notify Slack.'),
        }
        self.fields["prompt"].label = ""

        self.fields["prompt"].widget.attrs.update({
            "placeholder": placeholders['prompt'],
            "autofocus": True,
            "rows": 7,
        })