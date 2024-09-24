# Cluster MPI com Raspberry Pi para Treinamento de Modelos LightGBM e Mapeamento de Sombreamento em Usinas Fotovoltaicas

## Descrição do Projeto

Este projeto visa implementar um sistema distribuído utilizando um cluster de Raspberry Pi, cada um equipado com sensores de irradiância e conectados a inversores de uma usina fotovoltaica. O objetivo é processar localmente, com o uso de MPI (Message Passing Interface), os dados coletados para treinar modelos de Machine Learning (LightGBM) que preveem a geração de energia e detectam anomalias na produção. Além disso, os dados de irradiância são usados para gerar um mapa virtual de sombreamento da usina.

A utilização de um cluster distribuído permite uma análise rápida e eficiente, sem a necessidade de processamento em nuvem, reduzindo latências e custos operacionais. O projeto também integra um pipeline CI/CD que automatiza as operações de MLOps, garantindo um fluxo contínuo de desenvolvimento e atualização dos modelos.

## Objetivos

- **Treinamento Distribuído de Modelos LightGBM:** Implementar um sistema de treinamento distribuído utilizando LightGBM em um cluster de Raspberry Pi, permitindo a previsão de geração de energia e detecção de anomalias em tempo real.
- **Mapeamento de Sombreamento:** Criar um modelo paralelo para converter as informações dos sensores de irradiância em um mapa virtual de sombreamento da usina fotovoltaica.
- **Pipeline CI/CD e MLOps:** Automatizar o ciclo de vida do desenvolvimento e implantação dos modelos de ML, incluindo coleta de dados, treinamento, validação e deployment.

## Estrutura do Projeto

```plaintext
Cluster-MPI-LightGBM/
│
├── src/
│   ├── main.py                 # Código principal do projeto
│   ├── data_preprocessing.py    # Script para pré-processamento dos dados
│   ├── shading_map.py           # Script para geração do mapa de sombreamento
│   └── model_training.py        # Script para treinamento do modelo LightGBM
│
├── data/
│   ├── irradiance_data_node_0.csv  # Dados de irradiância para o nó 0 (exemplo)
│   ├── irradiance_data_node_1.csv  # Dados de irradiância para o nó 1 (exemplo)
│   └── ...
│
├── .github/
│   └── workflows/
│       └── ci_cd_pipeline.yml   # Definição do pipeline CI/CD
│
├── .gitignore                   # Arquivo para ignorar arquivos desnecessários no repositório
├── requirements.txt             # Dependências do projeto
└── README.md                    # Documentação do projeto