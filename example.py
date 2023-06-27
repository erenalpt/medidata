from medidata import dataset

# Load the dataset
X, y, labels = dataset.load_br35h(img_size=(100, 100))

# Check the dataset shape
print("X shape:", X.shape)
print("y shape:", y.shape)
print("Labels:", labels)
