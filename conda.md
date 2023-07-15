checking if conda is installed

    conda info

updating conda

    conda update -n base -c defaults conda

if it didn't work, run this first:

    conda config --add channels conda-forge

creating new environment

    conda create -n env1 python=x.x 

removing an environment (make sure it's deactivated first)

    conda remove --name ENV_NAME --all

list of environments

    conda env list

cleaning tmp and cache files

    conda clean --all
