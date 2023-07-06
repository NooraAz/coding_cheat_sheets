checking if conda is installed

    conda info

updating conda

    conda update -n base -c defaults conda

if it didn't work, run this first:

    conda config --add channels conda-forge

creating new environment

    conda create -n env1 python=x.x 

