from django.db import models


class Campeonato(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    premiacao = models.CharField(max_length=100)
    dt_inicio = models.DateField()
    dt_termino = models.DateField()

    class Meta:
        db_table = 'campeonatos'  # Nome da tabela no banco de dados

    def __str__(self):
        return self.nome


class Clube(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    dt_fundacao = models.DateField()
    titulos = models.CharField(max_length=255)
    campeonatos = models.ManyToManyField(
        Campeonato,
        through='CampeonatoClube',  # Tabela de associação entre Campeonatos e Clubes
        related_name='clubes'
    )

    class Meta:
        db_table = 'clubes'  # Nome da tabela no banco de dados

    def __str__(self):
        return self.nome


class Jogador(models.Model):
    # Atribuindo chave primária conforme a estrutura
    id = models.AutoField(primary_key=True)
    # CPF único conforme especificado
    cpf = models.CharField(max_length=100, unique=True)
    nome = models.CharField(max_length=255)
    posicao = models.CharField(max_length=50)
    numero = models.IntegerField()
    tempo_contrato = models.CharField(max_length=100)
    titular = models.BooleanField()
    dt_nascimento = models.DateField()
    salario = models.FloatField()
    clube = models.ForeignKey(
        Clube,
        on_delete=models.CASCADE,
        related_name='jogadores'
    )

    class Meta:
        db_table = 'jogadores'  # Nome da tabela no banco de dados

    def __str__(self):
        return self.nome


class Treinador(models.Model):
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=100, unique=True)
    nome = models.CharField(max_length=255)
    categoria = models.CharField(max_length=50)
    tempo_contrato = models.CharField(max_length=100)
    cargo = models.CharField(max_length=30)
    dt_nascimento = models.DateField()
    salario = models.FloatField()
    clube = models.ForeignKey(
        Clube,
        on_delete=models.CASCADE,
        related_name='treinadores'
    )

    class Meta:
        db_table = 'treinadores'

    def __str__(self):
        return self.nome


class Medico(models.Model):
    id = models.AutoField(primary_key=True)
    crm = models.CharField(max_length=100, unique=True)
    nome = models.CharField(max_length=255)
    especializacao = models.CharField(max_length=50)
    dt_nascimento = models.DateField()
    salario = models.FloatField()
    clube = models.ForeignKey(
        Clube,
        on_delete=models.CASCADE,
        related_name='medicos'
    )

    class Meta:
        db_table = 'medicos'

    def __str__(self):
        return self.nome


class CampeonatoClube(models.Model):
    id = models.AutoField(primary_key=True)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)

    class Meta:
        db_table = 'campeonato_clube'

    def __str__(self):
        return f"{self.clube} - {self.campeonato}"
