# BEAM - Blockchain Explorer and Analyzer Module

## Visão Geral

BEAM é uma ferramenta poderosa e flexível para explorar e analisar transações de criptomoedas na blockchain. Desenvolvida em Python, ela oferece funcionalidades para rastrear endereços, analisar transações e gerar insights valiosos sobre atividades na blockchain.

## Características

- Rastreamento de endereços Bitcoin
- Análise detalhada de transações
- Geração de relatórios em CSV
- Cálculo de estatísticas de transações (total recebido, enviado, etc.)
- Interface de linha de comando intuitiva

## Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório:

```git clone https://github.com/eduardocastilho/BEAM.git cd BEAM```


2. Instale as dependências:

```pip install -r requirements.txt```


## Uso

Execute o script principal:

```python main.py```


Siga as instruções na tela para inserir um endereço Bitcoin ou usar o endereço padrão fornecido.

## Estrutura do Projeto

- `main.py`: Ponto de entrada do programa
- `config.py`: Configurações e constantes
- `api_client.py`: Gerencia as chamadas à API da blockchain
- `data_processor.py`: Processa os dados brutos das transações
- `analyzer.py`: Realiza análises nas transações processadas
- `utils.py`: Funções utilitárias

## Configuração

Edite `config.py` para ajustar as configurações da API e outros parâmetros globais.

## Contribuindo

Contribuições são bem-vindas! Por favor, leia o arquivo CONTRIBUTING.md para detalhes sobre nosso código de conduta e o processo para enviar pull requests.

## Próximos Passos

- [ ] Implementar interface gráfica do usuário (GUI)
- [ ] Adicionar suporte para múltiplas criptomoedas
- [ ] Desenvolver análises avançadas usando machine learning
- [ ] Integrar com APIs de exchanges populares
- [ ] Implementar geração de relatórios em PDF
- [ ] Adicionar sistema de alertas e notificações
- [ ] Criar visualização de rede de transações

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.

## Contato

Seu Nome - [@duca404](https://twitter.com/duca404) - br.eduardocastilho@gmail.com

Link do Projeto: [https://github.com/eduardocastilho/BEAM](https://github.com/eduardocastilho/BEAM)

## Agradecimentos

- [Blockchain.info API](https://www.blockchain.com/api)
- [Pandas](https://pandas.pydata.org/)
- [Requests](https://docs.python-requests.org/en/master/)