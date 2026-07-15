from django.conf import settings
from django.db import models


class N8nConnection(models.Model):
    """
    Model to store user n8n connection details.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name="n8n_connection")
    instance_url = models.URLField(models.URLField)
    api_key = models.TextField()
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.instance_url}"


STATUS_CHOICES = [("pending", "Pending"), ("created", "Created"), ("failed", "Failed")]

class GeneratedWorkflow(models.Model):
    """
    Model to store details of the generated workflow.
    """
    n8n_connection = models.ForeignKey(N8nConnection, on_delete=models.CASCADE,
                                       related_name="workflows")
    prompt = models.TextField()
    workflow_id = models.CharField(max_length=255, blank=True)
    workflow_url = models.URLField(blank=True)
    documentation = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Workflow {self.workflow_id} - {self.status}"
