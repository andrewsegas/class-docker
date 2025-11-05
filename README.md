## 🧩 1. Docker Playground — Subindo e Testando Serviços

**Objetivo:** entender na prática o que são containers, portas e logs.

Vamos rodar alguns serviços diferentes, todos isolados uns dos outros:

```bash
docker run -d -p 8080:80 nginx
docker run -d -p 3000:80 httpd
docker run -d -p 9090:80 nginx
```

Cada container sobe seu próprio servidor web e responde em uma porta diferente.
Use os comandos abaixo para explorar o que está acontecendo:

```bash
docker ps
docker logs <id>
docker stop <id>
docker rm <id>
```

**O que você aprende aqui:**

* Como containers rodam isolados.
* Como expor portas diferentes.
* Como inspecionar e controlar containers.

---

## ⚙️ 2. Mini Load Balancer Manual

**Objetivo:** entender o que é escalar horizontalmente (ter várias instâncias do mesmo serviço).

Vamos rodar duas versões do mesmo servidor:

```bash
docker run -d -p 8081:80 --name web1 nginx
docker run -d -p 8082:80 --name web2 nginx
```

Abra as duas portas no navegador e veja que são servidores diferentes.
Depois, entenda:

> “Como eu faria para distribuir o tráfego automaticamente entre eles?”

**O que você aprende aqui:**

* O conceito de escalabilidade horizontal.
* Como containers podem ser independentes.
* Por que orquestradores (como Kubernetes) existem.

---

## 🧠 3. Meu Container com Personalidade

**Objetivo:** criar sua própria imagem Docker.

Crie um arquivo `Dockerfile` na mesma pasta do seu `index.html`:

```dockerfile
FROM nginx
COPY index.html /usr/share/nginx/html/index.html
```

Depois rode:

```bash
docker build -t minha-pagina .
docker run -d -p 8080:80 minha-pagina
```

Agora acesse no navegador e veja seu site rodando dentro de um container.

**O que você aprende aqui:**

* Como criar e buildar imagens personalizadas.
* Que mudar o conteúdo exige rebuild da imagem.
* Que o Dockerfile é como uma “receita” do seu ambiente.

**Desafio:** personalize o HTML e mostre seu próprio container rodando.
