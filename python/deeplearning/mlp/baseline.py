import numpy as np
import pandas as pd
class BaseLineModel:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.lr = learning_rate
        self.n_iterations = n_iterations
        self.loss_history = []

    
    def sigmoid(self, z):
        return 1/(1+np.exp(-z))
    

    def relu(self, z):
        return z if z>0 else 0
    



class DataExtractor:
    def __init__(self, filepath, column_names):
        self.filepath = filepath
        self.column_names = column_names
        

    def read_csv(self):
        df = pd.read_csv(self.filepath,
                    header=None,
                    names=self.column_names,
                    na_values="?",
                    usecols=range(len(self.column_names)))
        print(f"Initial shape : {df.shape}")
        print(df.head())

        return df



def main():
    FILE_PATH = "../data/wisconsin_original.csv"
    COLUMN_NAMES = [
        "id",
        "clump_thickness",
        "cell_size_uniformity",
        "cell_shape_uniformity",
        "marginal_adhesion",
        "epithelial_cell_size",
        "bare_nuclei",
        "bland_chromatin",
        "normal_nucleoli",
        "mitoses",
        "class"
    ]


    dataExtractor = DataExtractor(FILE_PATH, COLUMN_NAMES)
    dataExtractor.read_csv()
    base_line = BaseLineModel(FILE_PATH, COLUMN_NAMES)
    


if __name__ == "__main__":
    main()
