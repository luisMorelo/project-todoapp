from rest_framework import serializers
from .models import Task

class taskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task

        fields = ['id', 'titulo', 'descripcion', 'fecha_creacion', 'terminado']

        #le indico que este campo sera solo lectura y no se puede modificar
        read_only_fields = ('fecha_creacion',) 