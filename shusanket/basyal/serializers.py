from dataclasses import field
from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields="__all__"
        
    def validate(self, data):
        nm = data.get("name")
        if nm is not None and nm.lower() == "ram":
            raise serializers.ValidationError("YOU ARE BLOCKED")
        
        return data