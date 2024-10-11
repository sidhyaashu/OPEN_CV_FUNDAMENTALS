import os

# Define the project structure
project_structure = {
    "data": ["raw", "processed", "annotations", "augmentation", "external"],
    "notebooks": ["exploration.ipynb", "experiments.ipynb"],
    "src": ["__init__.py", "data_loader.py", "model.py", "train.py", "evaluate.py", "predict.py", "utils.py"],
    "models": ["checkpoints", "final", "pre-trained"],
    "logs": ["tensorboard", "training.log"],
    "results": ["predictions", "visualizations"],
    "configs": ["config.yaml"],
    "scripts": ["convert_data.py"],
    "tests": ["__init__.py", "test_data_loader.py", "test_model.py", "test_utils.py"],
}

# Create the base project directory
project_name = "OpenCV"
os.makedirs(project_name, exist_ok=True)

# Create folders and files based on the defined structure
for folder, contents in project_structure.items():
    folder_path = os.path.join(project_name, folder)
    os.makedirs(folder_path, exist_ok=True)
    
    for item in contents:
        item_path = os.path.join(folder_path, item)
        
        if "." in item:  # It's a file
            with open(item_path, "w") as f:
                pass
        else:  # It's a subdirectory
            os.makedirs(item_path, exist_ok=True)

# Create the remaining files at the root level
root_files = ["README.md", "requirements.txt", "requirements_dev.txt","Dockerfile"]
for file in root_files:
    file_path = os.path.join(project_name, file)
    with open(file_path, "w") as f:
        pass

print(f"Project structure for '{project_name}' has been created.")
