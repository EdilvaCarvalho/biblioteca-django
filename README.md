<h1 align="center">Projeto Biblioteca como o <em>framework</em> Django</h1>

<ul>
    <li>Clone o repositório;</li>
    <code>
        git clone https://github.com/EdilvaCarvalho/biblioteca-django.git
    </code>
    <li>No terminal: Instale as dependências do ambiente de desenvolvimento;</li>
    <code>
        pip install -r requirements.txt
    </code>    
<<<<<<< HEAD
    <li>No SGBD PostgreSQL: Crie o banco de dados com o nome de "biblioteca-django". Lembrar de alterar o USER e o PASSWORD do seu banco no arquivo settings.py;</li>
=======
    <li>No SGBD PostgreSQL: Crie o banco de dados com o nome de "biblioteca". Lembrar de alterar o USER e o PASSWORD do seu banco no arquivo settings.py;</li>
    <li>Após a criação do banco, lembrar de realizar as migrações para a criação das tabelas no banco de dados;</li>
    <li>No terminal: Crie as migrações:</li>
    <code>
        python manage.py makemigrations
    </code>
    <br>
    <code>
        python manage.py migrate
    </code>
>>>>>>> 94e874c552600479636704a16da3d10a5feae985
</ul>
