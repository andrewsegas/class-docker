Executar 

# cria a imagem com o nome minhaimagem "." do arquivo dockerfile que está na pasta corrente
docker build -t minhaimagem .

# executa a imagem criando um container (-d) em modo background, (-p) nas portas 8080 do seu computador para a porta 80 do container
docker run -d -p 8080:80 minhaimagem