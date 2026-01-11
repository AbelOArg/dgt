from django.db import models

class empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    afiliado = models.IntegerField(verbose_name='Afiliado')
    dni = models.IntegerField(verbose_name='DNI', null=True)
    seccion = models.CharField(max_length=50,verbose_name='Seccion')
    turno = models.CharField(max_length=20,verbose_name='Turno')
    reparticion = models.CharField(max_length=50,verbose_name='Reparticion')
    horasquetrabaja = models.IntegerField(verbose_name='Horas que trabaja')
    horadeingreso = models.TimeField(verbose_name='Horario de ingreso', null=True)
    horadeegreso = models.TimeField(verbose_name='Horario de salida', null=True)
    is_active = models.BooleanField(default=True, verbose_name='Activo')

    def __str__(self):
        return f"{self.apellido}, {self.nombre} - Afiliado: {self.afiliado} - seccion: {self.seccion} - turno: {self.turno} - reparticion: {self.reparticion} - activo: {self.is_active}"