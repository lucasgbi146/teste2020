from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField('Título', max_length=200)
    texto = models.TextField('Conteúdo')
    autor = models.ForeignKey('User', on_delete=models.CASCADE)
    Data_pub = models.DateTimeField('Data de Publicação', auto_now())
    data_alt = nodels.DateTimeField('Data de Atualização', add_auto_now()) 
    imagem = models.ImageField('Imagem', upload_to='imagens')