# Master building Python package

🚀 Develop, Install and Publish a demo python package - "dapro", stands for "data processing" 🚀

## ✅ Setup Env
- Create Python environment\
`conda create -n env_name python=3.10`\
`conda activate env_name`
- Create Python environment\
`pip install -r .\path_to_requirements\requirements.txt`

## Package development
Below is the package 'dapro' structure with directory tree

    ├───dapro
    │   ├───data_eda
    │   │   ├───pro_eda.py
    │   │   └───__init__.py
    │   ├───data_importing
    │   │   ├───pro_import.py
    │   │   └───__init__.py
    │   ├───data_viz
    │   │   ├───config
    │   │   └───__init__.py
    │   ├───input
    │   │   ├───config
    │   │   │  └───hyperparameter.json
    │   │   └───__init__.py
    │   ├───dapro_engine.py
    │   └───__init__.py
## ✅ Install Package
- Install package 'dapro' locally
````commandline
git clone https://github.com/tanquangduong/master-python-packaging.git
cd ./path_to_this_cloned_repository
pip install -e .
````
- Install package 'dapro' from GitHub repository HTTPS\
`git install git+https://github.com/tanquangduong/master-python-packaging.git`

  