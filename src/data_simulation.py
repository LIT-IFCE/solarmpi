import numpy as np
import pandas as pd

def simulate_data(node_id, num_samples=8000):
    """
    Simula dados de irradiância, corrente e tensão para um nó específico.
    node_id: Identificador do nó (Raspberry Pi)
    num_samples: Número de amostras a serem geradas
    """
    np.random.seed(node_id)  # Para garantir que cada nó tenha um conjunto de dados diferente

    # Simulação dos dados
    irradiance = np.random.uniform(200, 1000, num_samples)  # W/m²
    current = np.random.uniform(0, 10, num_samples)  # Amperes
    voltage = np.random.uniform(100, 600, num_samples)  # Volts
    cloud_coverage = np.random.uniform(0, 1, num_samples)  # Percentual de cobertura de nuvens

    # Calcula a potência de saída (simplificação)
    output_power = irradiance * (current * voltage) * (1 - cloud_coverage)

    # Cria um DataFrame
    data = pd.DataFrame({
        'irradiance': irradiance,
        'current': current,
        'voltage': voltage,
        'cloud_coverage': cloud_coverage,
        'output_power': output_power
    })

    # Salva os dados simulados em um arquivo CSV
    data.to_csv(f'data/simulated_data_node_{node_id}.csv', index=False)
    print(f"Dados simulados para o nó {node_id} foram salvos.")

if __name__ == "__main__":
    for node_id in range(100):  # Simula dados para 100 nós
        simulate_data(node_id)