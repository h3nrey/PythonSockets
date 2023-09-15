# Procurador de pokemon

## Como rodar
Abra 4 instancias do terminal de comando para o seguintes arquivos:
``` py
# dns.py
# udp_server.py
# tcp_server.py
# main.py
```

## Organização do projeto
```py
main_py  # Script chefe que roda os clientes udp e tcp
```

### UDP
```py
udp_server.py
udp_client.py
```

### TCP
```py
tcp_server.py
tcp_client.py
```
### DNS
```py
dns.py # servidor de nomes básico
```

### Utilitários
```py
writetime.py # Fornece funções para escrever e limpar timecapture.txt
costants.py # Informações estáticas como endereços e portas dos hosts
database.py # Dados da aplicação
```

## Captura dos pacotes
<a href="/capture.pcapng"> link do pacote</a>







