#----------------------------------------- 4 - Arquitetura Cliente-Servidor
## É uma Estrutura de computação distribuída que distribui tarefas e cargas e trabalho entre fornecedores de serviço, chamados de servidores, e os requerentes dos serviços, chamados de clientes.


#-----------------------------------------5 - Protocolo HTTP e seus verbos
##Um dos protocolos mais importantes e utilizados no mundo, o Protocolo de Transferência de Hipertexto
###é o que usamos todos os dias, mesmo sem saber, para fazer acesso a todos os websites e redes
####sociais que conhecemos.
#####Os serviços que implementam este protocolo, chamados de serviços HTTP, ou servidores HTTP, se
######comunicam nas portas 80 para HTTP ou 443 para HTTPS.
#######Você encontra toda a referência para este protocolo, atualmente na versão 2, na RFC 7540[1] que foi
########definida pela IETF - Internet Engineering Task Force.
#########[1]https://tools.ietf.org/html/rfc7540


#O protocolo HTTP define métodos para indicar a ação desejada a ser realizada no recurso identificado.
##Estes métodos são chamados de verbos HTTP quando utilizados como aplicações web.
### GET -> Buscar recursos/Cache
#### POST -> Criar um novo recurso
##### PUT/PATCH -> Atualizar um recurso existente 
##### (PUT ultilizamos quando estamos atualizando todos os dados)
##### (PATCH ultilizamos quando estamos atualizando parte dos dados)
###### DELETE -> Remover um recurso



#-----------------------------------------6 - Programação Backend x Frontend x Full-Stack
##No mundo do desenvolvimento de software existem três termos muito comuns que provavelmente
###você já se deparou: frontend, backend e full-stack.
####É muito comum vermos vagas de empregos com os títulos:
####Programador Frontend;
####Programador Backend;
####Programador FullStack; 

##Frontend
###Quando falamos em frontend, estamos falando da aplicação responsável pela apresentação do
###software, chamado de client-side (lembra do cliente-servidor?).
###Se tratando de aplicações web, é exatamente o código do sistema que roda no navegador.
###Um desenvolvedor frontend, geralmente, trabalha com linguagens como HTML, CSS e JavaScript,
###além de frameworks e bibliotecas, como Angular, React, Vue.JS, etc.
###Embora estes programadores não precisem conhecer como desenvolver código de backend, é
###extremamente importante que eles conheçam os fundamentos sobre a arquitetura de software, afinal
###de contas, o código que eles produzem faz parte de um todo e se comunica com o backend.

#Frontend
##Desenvolvedores frontend não lidam diretamente com banco de dados, servidores de aplicação
##complexos e várias outras coisas que só quem trabalha com backend conhece.
##Os desafios para quem trabalha com frontend são outros: Criar páginas ou telas com boa usabilidade
##e carregamento rápido, garantir o funcionamento nos diferentes navegadores, integrar com os serviços
##do backend, etc.


#Backend
##O código que é escrito para rodar no servidor (HTTP), também conhecido como server-side, é o
##backend.
##É o backend que fornece e garante todas as regras de negócio, acesso a banco de dados, segurança
##e escalabilidade.
##Embora o frontend também possa ter algumas regras e validações, é o backend que deve garantir a
##integridade dos dados.
##Programação


#Backend
##Desenvolvedores que se especializam apenas em backend, geralmente, não são muito bons em
##deixar páginas web bonitas e com boa usabilidade, mas são melhores em regras de negócio, banco de
##dados e todas as cosias que rodam no servidor.
##Estes desenvolvedores trabalham com linguagem de programação como, Python, Java, C#, Ruby ou
##até mesmo JavaScript.


#FullStack
##Quem trabalha tanto como frontend quanto como backend é conhecido como FullStack.
##Este é um tipo de profissional mais completo, que pode entregar um projeto do início ao fim, sem
##necessariamente precisar de ajuda de outra pessoa para criar uma parte do sistema.
##De certa foram é um profissional mais valorizado no mercado, especialmente se for realmente bom em
##frontend e backend.


#----------------------------------- 7. Programação Estática x Dinâmica.

##Usamos o termo programação estática ou dinâmica para nos referir do uso de linguagens de
##programação que não são processados no servidor (estática) ou que são processados no servidor
##(dinâmica).
##Como exemplos de linguagens estáticas temos HTML, CSS e JavaScript, etc.
##Como exemplos de linguagens dinâmicas temos Python, Java, Ruby, PHP, C#, JavaScript, etc.


#------------------------------------8. O mínimo que você precisa saber sobre HTML

##HTML é a sigla para Hypertext Markup Language, ou Linguagem de Marcação para Hipertexto.
##Utilizamos HTML para criar estruturas para páginas web: seções, parágrafos, cabeçalhos, divisões,
##links e etc.
##Toda página na internet que você acessa se você clicar com o botão do mouse no navegador e pedir
##para ver o código fonte será mostrado o conteúdo HTML da página

#Ao trabalhar com HTML nós codificamos estruturas (tags e atributos) para marcar a página de um
##site, por isso o HTML é chamado de linguagem de marcação. Um arquivo HTML tem extensão ‘.html’.

##De forma geral, uma página web é dividida em 3 área principais: header, body e footer.
##Uma página web é renderizada pelo navegador de cima para baixo, linha a linha.
##Header: Usado para tags de informação sobre o
##site, aplicação de estilos css e etc.

###Body: Conteúdo do site que é apresentado ao cliente.
###Footer: Geralmente usado para carregamento de
###scripts Javascript e apresentação de dados de rodapé.
###OBS: O footer fica dentro da área de conteúdo


#Podemos iniciar um servidor web simples com Python utilizando o comando abaixo:
##python3 -m http.server 8000


#As tags HTML são subdivididas em dois grupos principais:
##Elementos de bloco: Utilizam todo o espaço disponível e começam uma nova linha no documento.
##Elementos em linha: Utilizam apenas o espaço necessário e não criam uma quebra de linha.
###OBS: Iremos entender melhor a diferença entre eles nos exemplos desta aula

#Tags mais utilizadas nos elementos de bloco:
##<html> </html>: É o elemento de maior nível que está em todas as páginas HTML.
##<head> </head>: Possui informações do meta como título e charset da página.
##<body> </body>: Engloba todos os elementos que são mostrados na página.
##<h1> </h1>, <h2> </h2>, <h3> </h3>, <h4> </h4>, <h5> </h5>, <h6> <h6>: Cabeçalhos com níveis de 1 a 6, onde o 1 é o maior nível e o 6 o menor.
##<div> </div>: Divisões de seções de conteúdo.
##<p> </p>: Parágrafo.
##<blockquote> </blockquote>: Bloco de citações.
##<ol> </ol>: Listas ordenadas.
##<ul> </ul> Listas não ordenadas.
##<li> </li>: Item de listas.


#<strong> </strong>: Renderiza um texto em negrito.
#<em> </em>: Renderiza um texto em itálico.
#<a> </a>: Cria um link para outra página ou documento.
#<img>: Adiciona imagem na página. 

#O HTML foi criado pelo pesquisador Tim Berners-Lee no CERN e atualmente é mantido pelo W3C -
#World Wide Web Consortium contanto inclusive com um escritório no Brasil. 


#------------------------- 9. O mínimo que você precisa saber sobre CSS

##CSS é a sigla de Cascading Style Sheets, ou Folha de Estilo em Cascata e é usado para aplicar estilos nas páginas HTML.
##Desenvolvido pelo W3C em 1996 para formatar as páginas HTML, já que as tags HTML foram projetadas para realizar marcação das páginas.
##A relação entre HTML e CSS é bem forte. Como o HTML é uma linguagem de marcação (o alicerce de um site) e o CSS é focado no estilo (toda a estética de um site), eles andam juntos.


#Basicamente existem duas formas de se adicionar estilos CSS em uma página HTML:
##1 - Inline, ou seja, diretamente na página HTML (não recomendado);

#Basicamente existem duas formas de se adicionar estilos CSS em uma página HTML:
##2 - Externo, ou seja, em arquivo externo ou mesmo diretamente da internet (recomendado)


#Usamos CSS para formatar nossas páginas HTML de 3 formas diferentes:
##1 - Por elemento (tag) html: Usado quando queremos que todas as tags especificadas recebem a mesma formatação.
##2 - Por classe: Usado quando queremos que todo elemento que incorporar a determinada classe receba a formatação.
##3 - Por id: Usado quando queremos que elementos individuais recebem a formatação.


#Anatomia de um comando CSS:
##Um comando básico CSS é composto por seletor e declarações que contém propriedade e valor.

##SELETOR {
## propriedade: valor;
##}


##O seletor seleciona quais elementos da página receberão a formatação da propriedade com o valor
##especificado. Vimos a pouco que o seletor pode ser uma tag HTML, uma classe ou um id.
##São muitas as propriedades e valores possíveis para formatação de uma página. Podemos formatar praticamente qualquer coisa, lembrando que estamos falando de aplicação de estilos, que envolve escolher tipo/tamanho/cores de fonte, cores de páginas, alinhamento, posicionamento de seções e etc. Programador backend sofre com estas coisas



#------------------10. O mínimo que você precisa saber sobre JavaScript

##A linguagem JavaScript foi criada por Brendan Eich na empresa Netscape.
##Atualmente é mantida pela European Computer Manufacturer’s Association e seu nome “oficial" é ECMAScript, mas continua sendo mais conhecida, principalmente pelos mais leigos, como JavaScript.
#OBS: JavaScript não é Java!

#O JavaScript completa a tríade da Web se encarregando dos comportamentos e ações das páginas.
#HTML -> Estrutura;
#CSS -> Estilos;
#JavaScript -> Comportamento/ações;
#Vamos entender melhor sobre comportamentos/ações nos exemplos a seguir…



#------------------------11. O mínimo que você precisa saber sobre frameworks frontend
#Um framework frontend nada mais é do que um conjunto de ferramentas que oferecem diversos recursos para desenvolvedores ##frontend, ou seja, para realizar as criações de html, css e javascript.
##Um dos frameworks mais famosos e utilizamos atualmente é o Bootstrap[1] criado pela empresa por traz do Twitter e ##disponibilizado para toda a comunidade. 



#----------------------12. A salvação de programadores backend: Templates

# https://themeforest.net/

# https://onepagelove.com/templates/html-templates


#----------------------13. Instalando e configurando o git no Windowns
    
    #É um software de versionamento do código 



#------------------18. Criando um ambiente virtual e instalado o Django

# Digite o código no cmd do windows para verificar o versão do python que está instalada 
#Comand:   python --version

# Digite o código no terminal do pycharm para que possa instalar o framework do Django
#Comand:   pip install django

# Digite o código no terminal do pycharm para que possa instalar o framework do Django e suas bibliotecas 
#Comand:    pip freeze > requirements.txt

#-------------19. Criando um projeto Django com SQLite3 e conhecendo sua estrutura

#Comand:     django-admin startproject django1 core      #Criar um diretório, comando feio no terminal do Pycharm

#-------------20. Criando uma Aplicação Django  e Conhecendo sua Estrutura

#-------------21. Django: Projeto x  Aplicações

#Quando trabalhamos com Django FrameWork devemos levar emm conta a forma de trabalho do mesmo que posssui um projeto que engloba o todo e aplicações plugáveis.
# Ou seja, em um projeto Django, podemos ter várias aplicações, cada uma com sua tarefa específica, e estas aplicações depois de criadas podem ser utilizadas por outros projetos.



#django-admin startproject ------------> Projeto  xyz
#django-admin startapp


#-------------23. Configurações do Django e o arquivo settings.py
#dir   #Verificar os diretórios  
#pytho manage.py runserver  #Para start a aplicação


#-------------24. Views no Django e o arquivo  views.py
#Dentro do arq. View fazemos uma pequena parte do código  , para fazer a requisição no  index.html ou seja criando a view. 
# Uma view nada mais é do que uma função que recebe uma variavel chamada request  e  retorna a renderização desse request passando um template  ou seja uma página HTML

def index(request):
    return render(request, 'index.html'

def index(request):
    return render (request, 'contato.html')
