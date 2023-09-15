# Procurador de pokemon

O serviço simples de busca, o cliente coloca o tipo de pokemon e o servidor retorna pokemons desse tipo. O tipo de protocolo não influenciou significamente o tempo total de sessão, não há um determinante visível que implica no tempo da sessão, sendo bem "aleatório" o tempo que será.

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
<a href="/capture.pcapng"> link da captura de pacotes</a>







