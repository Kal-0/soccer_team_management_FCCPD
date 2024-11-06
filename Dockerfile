FROM python:3.10

WORKDIR /container

# Instalar dependências do Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Instalar o cliente MySQL para verificar a disponibilidade do banco
RUN apt-get update && apt-get install -y default-mysql-client

# Copiar o código do projeto
COPY . .

EXPOSE 8000

CMD ["sh", "-c", "cd teamManagement && python manage.py runserver 0.0.0.0:8000"]
