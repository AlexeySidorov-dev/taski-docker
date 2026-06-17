"""Serializers for app api."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializers for task."""

    class Meta:
        """Meta."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
