
# Website Sentinel

Este projeto é uma aplicação simples para monitorar alterações em um site específico. Ele verifica periodicamente o conteúdo do site, detecta mudanças no `<body>` do HTML e exibe os resultados em uma interface web. O monitoramento e a interface web são separados em dois componentes, tornando o sistema modular e escalável.

## Funcionalidades

- Monitoramento de alterações no conteúdo principal (`<body>`) de um site.
- Armazenamento do histórico de verificações em um banco de dados SQLite.
- Interface web para exibir o histórico de verificações.
- Destaque visual para linhas que indicam alterações detectadas.

## Tecnologias Utilizadas

- **Python**
- **Flask**
- **BeautifulSoup4**
- **Requests**
- **SQLite**

## Estrutura do Projeto

```plaintext
.
├── config.py              # Arquivo de configuração compartilhado
├── monitor.py             # Monitoramento do site e salvamento no banco de dados
├── server.py              # Interface web para exibir os dados monitorados
├── data_storage.db        # Banco de dados SQLite (criado automaticamente)
├── requirements.txt       # Lista de dependências do projeto
├── Dockerfile             # Configuração do container Docker
├── templates/
│   └── index.html         # Interface web do monitoramento
├── README.md              # Documentação do projeto
```

## Requisitos

- **Python 3.12+**
- **Dependências Python**:
  - Flask
  - BeautifulSoup4
  - Requests
  - SQLite (embutido no Python)

## Instalação

### Localmente

1. Clone este repositório:
   ```bash
   git clone https://github.com/thiagomendes/website-sentinel.git
   cd website-sentinel
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o monitoramento:
   ```bash
   python monitor.py
   ```

4. Inicie o servidor web:
   ```bash
   python server.py
   ```

5. Acesse a interface web:
   - Navegue para [http://127.0.0.1:5000](http://127.0.0.1:5000).

### Usando Docker

1. Construa a imagem Docker:
   ```bash
   docker build -t website-sentinel .
   ```

2. Execute o container:
   ```bash
   docker run -p 5000:5000 website-sentinel
   ```

3. Acesse a interface web:
   - Navegue para [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Configurações

As configurações compartilhadas estão no arquivo `config.py`:

- **URL do site monitorado**:
  ```python
  SITE_URL = "https://iaa.ufpr.br/"
  ```

- **Intervalo de verificação**:
  ```python
  CHECK_INTERVAL = 300  # Intervalo em segundos
  ```

- **Banco de dados SQLite**:
  ```python
  DATABASE = "data_storage.db"
  ```

## Exemplo de Funcionamento

### Interface Web (Monitoramento)

A tabela exibe:
- **Timestamp**: Data e hora da verificação.
- **Status**: "Sem alterações", "Erro ao acessar o site" ou "Alteração detectada".
- **Hash do Conteúdo**: Hash calculado a partir do `<body>`.

Linhas com **alterações detectadas** são destacadas com fundo amarelo.

### Monitoramento e Histórico

1. **Monitoramento**:
   O `monitor.py` verifica periodicamente o site definido no `config.py` e salva os resultados no banco de dados SQLite.

2. **Histórico**:
   O `server.py` consulta o banco de dados e exibe o histórico na interface web.

### Simulação de Alterações

Para simular alterações no site monitorado:
1. Altere manualmente o conteúdo do site em `config.SITE_URL` para um arquivo local ou URL acessível.
2. O monitor detectará a alteração e exibirá o resultado na interface web.
