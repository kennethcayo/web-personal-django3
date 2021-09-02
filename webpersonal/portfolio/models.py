from django.db import models
from django.db.models.fields import URLField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Titulo')
    description = models.TextField(verbose_name = 'Descripcion')
    image = models.ImageField(verbose_name = 'Imagen', upload_to='projects')
    # Campo de cuando se creo el registro
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creacion')
    #cuando se modifico
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de edicion')
    link = models.URLField(null=True, blank=True,  verbose_name='Mas Informacion') 
    
    class Meta:
        #vamos a cambiar el nombre projects
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        #Para que los proyectos salgan de forma ordenada
        ordering = ['-created'] #del mas actual al mas antiguo.
    
    #cambiamos a 'almacenaje de grano'
    def __str__(self):
        return self.title