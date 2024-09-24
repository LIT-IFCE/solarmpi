# Cluster MPI com Raspberry Pi para Treinamento de Modelos LightGBM e Mapeamento de Sombreamento em Usinas Fotovoltaicas

## Descrição do Projeto

Este projeto, executado no Laboratório de Inovação Tecnológica (LIT) do Instituto Federal do Ceará (IFCE), é proveniente de trabalhos de pós-graduação do Programa de Pós-Graduação em Ciência da Computação (PPGCC IFCE). O objetivo do projeto é implementar um sistema distribuído utilizando um cluster de dispositivos Raspberry Pi para processar dados localmente em uma usina fotovoltaica, com o intuito de realizar predições em tempo real da geração de energia e detecção de anomalias. Além disso, o sistema gera um mapa virtual de sombreamento da usina, utilizando dados coletados de sensores de irradiância e de inversores distribuídos pela planta.

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