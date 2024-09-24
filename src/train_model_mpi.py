import lightgbm as lgb
import pandas as pd
from mpi4py import MPI

def train_model(node_id, data_path):
    """
    Treina um modelo LightGBM em dados simulados para um nó específico.
    node_id: Identificador do nó (Raspberry Pi)
    data_path: Caminho para os dados simulados
    """
    # Carrega os dados simulados
    data = pd.read_csv(data_path)

    # Prepara os dados de entrada e saída
    X = data.drop('output_power', axis=1)
    y = data['output_power']

    # Cria o dataset do LightGBM
    train_data = lgb.Dataset(X, label=y)

    # Configura os parâmetros do LightGBM
    params = {
        'objective': 'regression',
        'metric': 'rmse',
        'num_leaves': 31,
        'learning_rate': 0.05,
        'feature_fraction': 0.9
    }

    # Treina o modelo
    bst = lgb.train(params, train_data, num_boost_round=100)

    # Salva o modelo treinado
    model_path = f'models/lightgbm_model_node_{node_id}.txt'
    bst.save_model(model_path)
    print(f"Modelo treinado para o nó {node_id} foi salvo em {model_path}.")

    return bst

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    # Define o caminho dos dados para o nó atual
    data_file = f'data/simulated_data_node_{rank}.csv'

    # Treina o modelo para o nó atual
    model = train_model(rank, data_file)

    # Aqui poderia agregar os modelos de cada nó, dependendo da aplicação específica