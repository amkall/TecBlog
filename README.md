# TecBlog

Aqui temos a construção de um blog utilizando o framework django, onde será trabalhada com maior foco no front-end


* deve-se criar um ambiente virtual env, para que o projeto possa ser inicializado, a criação do ambiente se da pelo comando:

    python3 -m venv env
    
* Apos sua criação o ambiente virtual deve ser inicializado 

    LINUX/MAC: source env/Scripts/activate               WINDOWS:  env\Scripts\Activate.bat

* para iniciar um projeto em django é necessario instalar as bibliotecas encontradas no arquivo requetiments.txt, basta abrir o terminal e navegar ate onde o arquivo se encontra e executar o seguinte comando:

    pip install -r requeriments.txt

* apos a instalção dos pacotes necessarios deve-se inicializar o projeto em django o seguinte comenado deve ser utilizado para essa criação:
    
    django-admin startproject NomeProjeto

* apos a criação do projeto um conjunto de pastas ira aparecer contendo o laytout inicial do projeto, onde aplicações serão introduzidas de acordo com a necessidade do proogramador atraves do comando:

    python manage.py startapp nome_da_app

O arquivo manage.py estara dentro da pasta criada pelo comando de criação do projeto
