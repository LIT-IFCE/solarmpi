import os
from mpi4py import MPI
from data_simulation import simulate_data
from train_model_mpi import train_model
from generate_shading_map import generate_shading_map

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    # Criação das pastas de saída, se não existirem
    if rank == 0:
        os.makedirs('data', exist_ok=True)
        os.makedirs('models', exist_ok=True)
        os.makedirs('shading_maps', exist_ok=True)

    # Sincroniza todos os nós
    comm.Barrier()

    # Simulação dos dados para o nó atual
    simulate_data(rank)

    # Caminho dos dados simulados
    data_file = f'data/simulated_data_node_{rank}.csv'

    # Treinamento do modelo
    train_model(rank, data_file)

    # Geração do mapa de sombreamento
    generate_shading_map(rank, data_file)

    # Sincroniza todos os nós antes de finalizar
    comm.Barrier()

    if rank == 0:
        print("Simulação completa.")

if __name__ == "__main__":
    main()