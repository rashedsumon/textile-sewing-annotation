
### 5. **`data_loader.py`**

import kagglehub
import os

def download_data(dataset_name: str, output_dir: str = 'dataset/'):
    # Check if the output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Download dataset from KaggleHub
    path = kagglehub.dataset_download(dataset_name)
    print(f"Dataset downloaded to {path}")
    
    # Return the path where dataset is stored
    return path

if __name__ == "__main__":
    dataset_path = download_data("belkhirnacim/textiledefectdetection")
    print(f"Data saved at {dataset_path}")
