# Cluster MPI com Raspberry Pi para Treinamento de Modelos LightGBM e Mapeamento de Sombreamento em Usinas Fotovoltaicas

## Descrição do Projeto

Este projeto, executado no Laboratório de Inovação Tecnológica (LIT) do Instituto Federal do Ceará (IFCE), é proveniente de trabalhos de pós-graduação do Programa de Pós-Graduação em Ciência da Computação (PPGCC IFCE). O objetivo do projeto é implementar um sistema distribuído utilizando um cluster de dispositivos Raspberry Pi para processar dados localmente em uma usina fotovoltaica, com o intuito de realizar predições em tempo real da geração de energia e detecção de anomalias. Além disso, o sistema ge...

A solução proposta visa superar as limitações de infraestrutura de comunicação, frequentemente encontradas em áreas remotas onde as usinas estão localizadas, minimizando a necessidade de processamento em nuvem e garantindo respostas rápidas a condições ambientais variáveis. O projeto também integra um pipeline CI/CD que automatiza as operações de MLOps, facilitando a atualização e implantação contínua dos modelos de aprendizado de máquina.

## Objetivos

- **Treinamento Distribuído de Modelos LightGBM:** Implementar um sistema de treinamento distribuído utilizando LightGBM em um cluster de Raspberry Pi, permitindo a predição de geração de energia e detecção de anomalias em tempo real.
- **Mapeamento de Sombreamento:** Criar um modelo paralelo para converter as informações dos sensores de irradiância em um mapa virtual de sombreamento da usina fotovoltaica.
- **Pipeline CI/CD e MLOps:** Automatizar o ciclo de vida do desenvolvimento e implantação dos modelos de ML, incluindo coleta de dados, treinamento, validação e deployment.

## Estrutura do Projeto

```plaintext
solarmpi/
│
├── src/
│   ├── main.py                 # Código principal do projeto
│   ├── data_simulation.py       # Script para simulação de dados
│   ├── train_model_mpi.py       # Script para treinamento distribuído do modelo LightGBM
│   └── generate_shading_map.py  # Script para geração do mapa de sombreamento
│
├── data/
│   ├── simulated_data_node_0.csv  # Dados simulados para o nó 0 (exemplo)
│   ├── simulated_data_node_1.csv  # Dados simulados para o nó 1 (exemplo)
│   └── ...
│
├── .github/
│   └── workflows/
│       └── ci_cd_pipeline.yml   # Definição do pipeline CI/CD
│
├── .gitignore                   # Arquivo para ignorar arquivos desnecessários no repositório
├── requirements.txt             # Dependências do projeto
└── README.md                    # Documentação do projeto

## Requisitos

- **Hardware:**
  - 100 dispositivos Raspberry Pi (com WiFi 6 habilitado) distribuídos em uma fazenda fotovoltaica de 10 hectares
  - Sensores de irradiância conectados a cada Raspberry Pi
  - Inversores conectados aos sensores e Raspberries
  - Rede WiFi Mesh para comunicação eficiente entre os dispositivos

- **Software:**
  - Python 3.x
  - Bibliotecas: `lightgbm`, `mpi4py`, `pandas`, `numpy`
  - Git para controle de versão
  - Docker (opcional) para containerização do projeto
  - VSCode (recomendado) para desenvolvimento e integração com GitHub

## Instalação

1. **Clone o Repositório:**
   \`\`\`bash
   git clone https://github.com/LIT-IDCE/solarmpi.git
   cd solarmpi
   \`\`\`

2. **Crie e Ative um Ambiente Virtual:**
   \`\`\`bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   \`\`\`

3. **Instale as Dependências:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Configure as Raspberries:**
   - Certifique-se de que cada Raspberry Pi está configurada corretamente e conectada à rede WiFi Mesh.
   - Copie os arquivos de dados para cada Raspberry Pi em suas respectivas pastas `data/`.

## Configuração e Teste da Simulação

### 1. Simulação de Dados

Antes de iniciar o treinamento e a geração do mapa de sombreamento, é necessário simular os dados de irradiância, corrente e tensão para cada nó (Raspberry Pi). Para isso, execute o seguinte comando:

\`\`\`bash
mpiexec -n 100 python src/data_simulation.py
\`\`\`

Esse comando irá gerar arquivos CSV contendo os dados simulados para cada um dos 100 nós.

### 2. Treinamento Distribuído com MPI

Após a simulação dos dados, execute o código principal para iniciar o treinamento distribuído do modelo LightGBM em todas as Raspberry Pi:

\`\`\`bash
mpiexec -n 100 python src/train_model_mpi.py
\`\`\`

Esse comando distribuirá o treinamento do modelo entre os 100 nós, utilizando os dados simulados.

### 3. Geração do Mapa de Sombreamento

Uma vez que o treinamento estiver concluído, você pode gerar o mapa de sombreamento utilizando os dados de irradiância e cobertura de nuvens:

\`\`\`bash
mpiexec -n 100 python src/generate_shading_map.py
\`\`\`

Este comando criará um mapa de sombreamento agregado a partir dos dados de todos os nós e salvará o resultado final.

### 4. Verificação dos Resultados

Após a execução dos scripts, você poderá verificar os modelos treinados e os mapas de sombreamento gerados nos diretórios `models/` e `shading_maps/`, respectivamente.

## Integração com CI/CD

O pipeline CI/CD já está configurado usando GitHub Actions. Toda vez que você fizer um \`push\` para o repositório, o pipeline será acionado para rodar testes e, se necessário, treinar o modelo novamente.



## Licença

Este projeto é licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato:
- Vagner: [vagner@lit.ifce.edu.br](mailto:vagner@lit.ifce.edu.br)
- Wendell: [wendell@ifce.edu.br](mailto:wendell@ifce.edu.br)