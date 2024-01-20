#!/usr/bin/env bash

notebooks_dir=` pwd `/notebooks
data_dir=` pwd `/data

echo Using:
echo    ${local_dir} as working directory

docker run  --name backtesting-notebook \
        --rm \
        -v ${notebooks_dir}:/home/jovyan/work \
        -v ${data_dir}:/home/jovyan/work/data \
        -e DATA_DIR=/home/jovyan/work/data \
        -p 8888:8888 \
        elena/backtesting_notebooks

#Test
# docker run --name my-jupyter --rm -ti fransimo/jupyter-elena /bin/bash