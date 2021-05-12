from django.db import models

# Create your models here.


class Operator(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    province = models.CharField(max_length=256, null=True, blank=True)
    state = models.CharField(max_length=28, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        # field_values = []
        # for field in self._meta.get_fields():
        #     field_values.append(str(getattr(self, field.name, '')))
        # return ' '.join(field_values)


class Dojo(models.Model):
    name = models.CharField(max_length=256)
    established_date = models.DateField()
    province = models.CharField(max_length=256)
    state = models.CharField(max_length=28)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    weight = models.IntegerField(null=True, blank=True)
    height = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    dojo = models.ForeignKey(Dojo, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
