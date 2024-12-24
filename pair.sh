#!/bin/bash

# Activate the conda environment
source $HOME/.bashrc
conda activate copa

# Run the Python script directly with the specified parameters
env HYDRA_FULL_ERROR=1 python -m trident.run experiment=bpm_pair_clf +trainer.log_every_n_steps=10 run.seed=${1}