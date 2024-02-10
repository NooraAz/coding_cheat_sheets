# checking if conda is installed
conda info

# updating conda
conda update -n base -c defaults conda

#if it didn't work, run this first:
conda config --add channels conda-forge

# creating new environment
conda create -n env1 python=x.x 

# removing an environment (make sure it's deactivated first)
conda remove --name ENV_NAME --all

# list of environments
conda env list
conda info -e

# cleaning tmp and cache files
conda clean --all

# installing miniconda 
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh

~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
