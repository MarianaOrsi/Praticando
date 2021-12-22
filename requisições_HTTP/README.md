* Método GET - usamos o get quando queremos pedir informações ao servidor ou API.

* Método POST - usamos o post quando queremos adcionar informações ao servidor ou API

* PUT e PATCH - usamos o put e patch quando queremos atualizar informações ao servidor ou API
obs: o PUT atualiza TODAS as informações do cliente. Já o PATCH atualiza somente as informações que você solicitar.


Método OPEN:
* Cria uma conexão entre a aplicação e o servidor. 

sintaxe:
httpRequest.open("MÉTODO", "URL", FLAG)

* MÉTODO:
O nome do método deve ser escrito em maiúsculo, de acordo com o padrão HTTP. Caso contrário, alguns navegadores podem não processar a solicitação, como por exemplo o FireFox.

* URL
O endereço da API / Servidor, que vamos enviar a solicitação;

* FLAG
O flag é opcional, define se a solicitação é assíncrona ou síncrona. Para solicitação síncrona utilizamos a flag como FALSE, e para solicitação assíncrona utilizamos a flag TRUE. Se não for informado nada, será interpretado como TRUE.



Método SEND:
* Ativa a conexção e realiza a devida requisição. Ele é um interprete de comunicação entre nossa página web, nosso sistema e o que queremos acessar, seja API / sistema ou servidor.

sintaxe:
httpRequest.send({DADOS});



Método onreadystatechange:
* Executa toda vez que houver mudança de estado no objeto XMLHttpRequest

sintaxe:
httpRequest.onreadystatechange();

STATUS: 
no 0 (não inicializado) ou (solicitação não inicializada)

no 1 (carregando) ou (conexão do servidor estabelecida)

no 2 (carregado) ou (solicitação recebida)

no 3 (interativo) ou (solicitação de processamento)

no 4 (completo) ou (pedido concluído e resposta pronta)

* FETCH - fornece uma maneira fácil e lógica para buscar recursos de forma assíncrona através da rede. 

sintaxe:
fetch("string_endereço", {
MÉTODO,
CORPO,
CABEÇALHO
});