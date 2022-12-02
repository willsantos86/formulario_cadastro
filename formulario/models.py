from django.db import models

# Create your models here.
class DadosPessoais(models.Model):
    genero_list = (
        ("maculino", "Masculino"),
        ("feminino", "Feminino"),
        ("outro", "Outro")
    )
    estado_list = (
        ('AC', 'AC'), ('AL', 'AL'), ('AM', 'AM'), ('AP', 'AP'), ('BA','BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), 
        ('GO', 'GO'), ('MA',' MA'), ('MG', 'MG'), ('MS', 'MS'), ('MT', 'MT'), ('PA', 'PA'), ('PB', 'PB'), ('PE','PE'),
        ('PI', 'PI'), ('PR','PR'), ('RJ','RJ'), ('RN','RN'), ('RO', 'RO'),('RR','RR'), ('RS','RS'), ('SC','SC'),
        ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')
        )
    nome = models.CharField(max_length=100, verbose_name="Nome completo")
    email = models.EmailField(verbose_name="Email")
    telefone = models.CharField(max_length=14, verbose_name="Telefone")
    genero = models.CharField(max_length=10, verbose_name="Genero", choices=genero_list)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    cidade = models.CharField(max_length=30, verbose_name="Cidade")
    estado = models.CharField(max_length=2, verbose_name="Estado", choices=estado_list)
    endereco = models.CharField(max_length=100, verbose_name="Endereço")


#Renomear classe
    class Meta:
        verbose_name_plural = "Dados Pessoais"

    #Formato de saída.
    def __str__(self):
        return f'{self.id} - {self.nome}'