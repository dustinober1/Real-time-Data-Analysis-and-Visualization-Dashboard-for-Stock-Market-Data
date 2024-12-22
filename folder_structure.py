import os

def create_project_structure():
  """Creates the directory structure for the stock dashboard project 
  in the current working directory.
  """

  folders = [
      "templates",
      "static",
  ]

  subfolders = {
      "static": ["css", "js"]
  }

  files = [
      "app.py",
      "data_fetcher.py",
      "data_analyzer.py",
      "visualizer.py",
      "models.py",  
      "requirements.txt",
      ".env",
      "README.md"
  ]

  # Create folders
  for folder in folders:
    # Create folders directly in the current directory
    if not os.path.exists(folder):
      os.makedirs(folder)

    # Create subfolders within the current directory
    if folder in subfolders:
        for subfolder in subfolders[folder]:
            subfolder_path = os.path.join(folder, subfolder)
            if not os.path.exists(subfolder_path):
                os.makedirs(subfolder_path)

  # Create files
  for file in files:
    # Create files directly in the current directory
    if not os.path.exists(file):
      with open(file, "w") as f:
        pass

  print(f"Project structure created in the current directory: {os.getcwd()}")

# Example usage:
if __name__ == "__main__":
  create_project_structure()