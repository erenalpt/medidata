import os
import cv2
import numpy as np
from tqdm import tqdm
from sklearn.utils import shuffle

def load_br35h(img_size=(100, 100)):
    """
    Load the BR35H dataset and return the images and labels.

    This function loads the BR35H dataset from the default directory path
    and returns the resized images and corresponding labels as numpy arrays.

    Parameters:
    - img_size (tuple, optional): A tuple specifying the image size. Default is (100, 100).

    Returns:
    - X (np.array): The images of the BR35H dataset, resized to the specified image size.
    - y (np.array): The labels of the BR35H dataset.
    - labels (dict): A dictionary mapping label indices to label names.

    Note:
    - Label 0 corresponds to "no".
    - Label 1 corresponds to "yes".
    """
    dataset_dir = os.path.join(os.path.dirname(__file__), 'br35h')
    X = []
    y = []
    i = 0
    labels = dict()
    for path in tqdm(sorted(os.listdir(dataset_dir))):
        if not path.startswith('.'):
            labels[i] = path
            for file in os.listdir(os.path.join(dataset_dir, path)):
                if not file.startswith('.'):
                    img = cv2.imread(os.path.join(dataset_dir, path, file))
                    img_resized = cv2.resize(img, img_size)
                    X.append(img_resized)
                    y.append(i)
            i += 1
    X = np.array(X)
    y = np.array(y)

    X, y = shuffle(X, y, random_state=46)
    
    return X, y, labels
