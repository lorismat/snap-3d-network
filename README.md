# SNAP-3D tiny script

A python script to generate a ready-to-visualize network in 3D with `Three.js`.

## Process

## From The CLI

There are two scripts to generate 3D representations of nodes and edges. One for a single iteration, one for N iterations. 

### `script.py`

`python script.py ./datasets/original/facebook_combined.txt ./datasets/synthetic/facebook_combined 10 50 0.001 False 0`

### `script_iter.py`

`python script.py ./datasets/original/facebook_combined.txt ./datasets/synthetic/facebook_combined_iter 10 50 0.001 False 10`

# Resources

- [NetworkX](https://networkx.org/documentation/latest/index.html)
- [SNAP Datasets](https://snap.stanford.edu/data/index.html)
- [Facebook Example](https://snap.stanford.edu/data/ego-Facebook.html) - version `facebook_combined.txt.gz`