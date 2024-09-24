import numpy as np
import pandas as pd
from mpi4py import MPI

def generate_shading_map(node_id, data_path):
    """
    Gera um mapa de sombreamento com base nos dados de irradiância e cobertura de nuvens.
    node_id: Identificador do nó (Raspberry Pi)
    data_path: Caminho para os dados simulados
    """
    data = pd.read_csv(data_path)

    # Cria um mapa de sombreamento simplificado (exemplo 100x100)
    shading_map = np.zeros((100, 100))

    for index, row in data.iterrows():
        # Simulação da influência da cobertura de nuvens no sombreamento
        x, y = np.random.randint(0, 100, 2)
        shading_map[x, y] += row['irradiance'] * (1 - row['cloud_coverage'])

    # Normaliza o mapa de sombreamento
    shading_map = shading_map / shading_map.max()

    # Salva o mapa de sombreamento
    np.save(f'shading_maps/shading_map_node_{node_id}.npy', shading_map)
    print(f"Mapa de sombreamento gerado e salvo para o nó {node_id}.")

    return shading_map

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    # Caminho para os dados simulados do nó atual
    data_file = f'data/simulated_data_node_{rank}.csv'

    # Gera o mapa de sombreamento para o nó atual
    shading_map = generate_shading_map(rank, data_file)

    # Agrega os mapas de sombreamento de todos os nós no nó mestre (rank 0)
    if rank == 0:
        full_shading_map = np.zeros_like(shading_map)
    else:
        full_shading_map = None

    comm.Reduce(shading_map, full_shading_map, op=MPI.SUM, root=0)

    if rank == 0:
        np.save("shading_maps/full_shading_map.npy", full_shading_map)
        print("Mapa de sombreamento completo gerado e salvo.")