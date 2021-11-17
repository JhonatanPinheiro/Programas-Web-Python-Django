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
#d#o backend, etc.


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