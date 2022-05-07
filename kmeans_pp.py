import numpy as np
import pandas as pd
import sys 
import math

np.random.seed(0)

def invalid_input():
    sys.exit("Invalid Input!")

def an_error_has_occurred():
    sys.exit("An Error Has Occurred")

def files_to_dataframe(file_name_1,file_name_2):
    file1 = pd.read_csv(file_name_1)
    size1=file1.shape[1]
    file2 = pd.read_csv(file_name_1)
    size = [str(i) for i in range(file1.shape[1])]
    file1 = pd.read_csv(file_name_1, names=size)
    size = [str(i+size1-1) for i in range(file2.shape[1])]
    size[0] = str(0)
    file2 = pd.read_csv(file_name_2, names=size)

    data = pd.merge(file1, file2, on ='0')
    data=data.drop(['0'],axis=1)
    return data.to_numpy()

def kmeanspp(matrix, k):
    matrix_idx = range(len(matrix))
    first_idx = np.random.choice(matrix_idx)
    centroids = []
    centroids.append(matrix[first_idx])
    while (len(centroids)<k):
        D = np.full((len(matrix)),float('inf'))
        for l,datapoint in enumerate(matrix):
            for j,centroid in enumerate(centroids):
                dist = calculate_distance(centroid, datapoint)
                if (dist<D[l]):
                    D[l] = dist
        Dm = sum(D)
        P = [D[i]/Dm for i in matrix_idx]
        idx_chosen = np.random.choice(matrix_idx, p=P)
        print(idx_chosen)
        centroids.append(matrix[idx_chosen])
        init_centroids = np.stack(centroids)
    return init_centroids

def calculate_distance(centroid, data_point):
    return sum([pow(centroid[i]-data_point[i],2) for i in range(len(centroid))])

def check_is_natural(num):
    try:
        # Convert it into float
        
        val_f = float(num)
        val_int=int(float(num))
    
    except ValueError:
        invalid_input()
    
    if val_f!=val_int or val_int<=0:
        invalid_input()

def main():
    k = 3
    file_name_1 = "test_data\input_1_db_1.txt"
    file_name_2 = "test_data\input_1_db_2.txt"
    input_matrix = files_to_dataframe(file_name_1, file_name_2)
    centroids = kmeanspp(input_matrix,3)
    print(centroids)

main()