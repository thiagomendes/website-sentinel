
# Website Sentinel

Este projeto é uma aplicação simples para monitorar alterações em um site específico. Ele verifica periodicamente o conteúdo do site, detecta mudanças no `<body>` do HTML e exibe os resultados em uma interface web.

## Funcionalidades

- Monitoramento de alterações no conteúdo principal (`<body>`) de um site.
- Interface web para exibir o histórico de verificações.
- Destaque visual para linhas que indicam alterações detectadas.
- Possibilidade de simular um site local para testes.

## Tecnologias Utilizadas

- **Python**
- **Flask**
- **BeautifulSoup4**
- **Requests**
- **HTML/CSS**

## Requisitos

- **Python 3.x**
- **Dependências Python**:
  - Flask
  - BeautifulSoup4
  - Requests

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/thiagomendes/website-sentinel.git
   cd website-sentinel
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o aplicativo:
   ```bash
   python app.py
   ```

## Uso

1. Acesse o monitoramento:
   - Acesse [http://127.0.0.1:5000](http://127.0.0.1:5000) no navegador para visualizar o histórico de verificações.

2. Simule um site para teste:
   - Acesse [http://127.0.0.1:5001/fake-site.html](http://127.0.0.1:5001/fake-site.html) para ver o site simulado.

3. Modifique o arquivo `fake-site.html`:
   - Alterações no conteúdo do `<body>` serão detectadas e exibidas no monitoramento.

## Estrutura do Projeto

```plaintext
.
├── app.py                 # Código principal do aplicativo
├── templates/
│   └── index.html         # Interface web do monitoramento
│   └── fake-site.html     # Página HTML para simulação de alterações
├── requirements.txt       # Lista de dependências do projeto
├── README.md              # Documentação do projeto
```

## Configurações

- **URL do site monitorado**:
  Por padrão, o aplicativo monitora o arquivo `fake-site.html` rodando localmente. Para alterar o site monitorado, modifique a variável `site_url` em `app.py`:
  ```python
  site_url = "http://exemplo.com"
  ```

- **Intervalo de verificação**:
  Por padrão, o intervalo de verificação é de **60 segundos**. Para alterar, modifique a constante `CHECK_INTERVAL` em `app.py`:
  ```python
  CHECK_INTERVAL = 120  # Intervalo em segundos
  ```

## Exemplo de Funcionamento

### Interface Web (Monitoramento)

A tabela exibe:
- **Timestamp**: Data e hora da verificação.
- **Status**: "Sem alterações", "Erro ao acessar o site" ou "Alteração detectada".
- **Hash do Conteúdo**: Hash calculado a partir do `<body>`.

Linhas com **alterações detectadas** são destacadas com fundo amarelo.

### Simulação de Alterações

1. Conteúdo inicial no `fake-site.html`:
   ```html
   <p>Este é o conteúdo inicial do site.</p>
   ```

2. Após a modificação:
   ```html
   <p>Este é o conteúdo atualizado do site.</p>
   ```

3. Resultado no monitoramento:
   - O status será alterado para **"Alteração detectada"** e a linha será destacada na tabela.
