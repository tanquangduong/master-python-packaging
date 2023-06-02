# Master building Python package

🚀 Develop, Install and Publish a demo python package - "dapro", stands for "data processing" 🚀

In this repository, I will walk you through the steps to build a Python package for your development in software engineering and/or data science. Let's test/install/use it firstly, then learn how to build it from scratch. Therefore, I organize this README as follows:
- Install package LOCALLY and test/use the package
- Install package via GITHUB REPOSITORY and test/use the package
- Package development
    - Overview of package structure
    - What a package needs
    - Test your python development before installation
- Next steps

## ✅ Install package LOCALLY and test/use the package 
- Clone this repo and go inside. If you have not yet done this step, do the following commands. Otherwise, skip this step.
```
git clone https://github.com/tanquangduong/master-python-packaging.git
cd ./path_to_this_cloned_repository
```
- Create Python environment: for example,  'env_package_local'
```
conda create -n env_package_local python=3.10
conda activate env_package_local
```
- Install package 'dapro' locally
```
pip install -e .
```

- Test installed package 'dapro' inside the environment 'env_package_local'
```
## Go to the subfolder 'test-package'
cd test-package

## Open the file 'test-package-installation.ipynb' in notebook. In the terminal, use the following cmd and open the notebook file
jupyter notebook

## Finally, run all the notebook cells. If it works, it means that your installation locally works and the your package development works just fine.
```

## ✅ Install package from GITHUB REPOSITORY and test/use the package 
- Clone this repo and go inside. If you have not yet done this step, do the following commands. Otherwise, skip this step.
```
git clone https://github.com/tanquangduong/master-python-packaging.git
cd ./path_to_this_cloned_repository
```
- Create NEW Python environment: for example,  'env_package_github'
```
conda create -n env_package_github python=3.10
conda activate env_package_github
```
- Install package 'dapro' from github link
```
pip install git+https://github.com/tanquangduong/master-python-packaging.git
```

- Test installed package 'dapro' inside the environment 'env_package_github'
```
## Go to the subfolder 'test-package'
cd test-package

## Open the file 'test-package-installation.ipynb' in notebook. In the terminal, use the following cmd and open the notebook file
jupyter notebook

## Finally, run all the notebook cells. If it works, it means that your installation locally works and the your package development works just fine.
```


## ✅  Package development
### Overview of package structure

    ├───dapro
    │   ├───data_eda
    │   │   ├───pro_eda.py
    │   │   └───__init__.py
    │   ├───data_importing
    │   │   ├───pro_import.py
    │   │   └───__init__.py
    │   ├───data_viz
    │   │   ├───pro_dataviz.py
    │   │   └───__init__.py
    │   ├───input
    │   │   ├───config
    │   │   │  └───hyperparameter.json
    │   │   └───__init__.py
    │   ├───__init__.py
    │   ├───dapro_engine.py
    │   ├───requirements.txt
    │   ├───pyproject.toml
    │   ├───MANIFEST.in
    │   └───README.md

### What a package needs
- Package folder with its name. In this demo, it is the folder 'dapro' for the package 'dapro'
- File: "\_\_init\_\_.py" to let python know that this is a python package
- File: 'package_main.py' contains all functions of this package. In this demo, it is 'dapro_engine.py'
- File: 'requirements.txt' contains all the required packages that are used inside our package 'dapro'
- File: 'pyproject.toml' contains information for package version, author, ... necessary for installation step
- File: 'MANIFESRT.in' allows to include the sub-package and sub-folder during installation
- File: 'README.md'. This is the file that you are reading. The indispensible.
- Sub-folder: 'input'. This is optional, but it allows you to add/manage hyperparameters and/or sample datasets for package usage. Inside it, we have:  
    - sub-folder 'config'
        - file: 'hyperparameter.json'
    - file '\_\_init\_\_.py' to let python know that it is sub-package
- Sub-package: 'data_eda'. It includes:
    - file: 'pro_eda.py' contains functions for data exploratory data analysis
    - file '\_\_init\_\_.py' to let python know that it is sub-package
- Sub-package: 'data_importing'. It includes:
    - file: 'pro_import.py' contains functions for data importing
    - file '\_\_init\_\_.py' to let python know that it is sub-package
- Sub-package: 'data_viz'. It includes:
    - file: 'pro_dataviz.py' contains functions for data visualization
    - file '\_\_init\_\_.py' to let python know that it is sub-package

### Test your python development before installation
- We prepare a sub-folder 'datasets', containing 'iris.csv', for testing our developement. 
- We prepare the file 'test-package-development.ipynb'. 
    - Come back to the root folder of this package: cd ..
    - In terminal, open notebook: jupyter notebook
    - Open the notebook file 'test-package-development.ipynb'
    - Run all the notebook cell. If it works, it means that your developments work as expected.

# Next steps
- Public our package to 'pypi.org' so it can be install by standard method: "pip install dapro"