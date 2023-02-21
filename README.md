# SNAP-3D tiny script

**A python script to generate a network with 3 dimensions ready to be visualize in 3D.**  


[Live Website](https://net-sim.netlify.app/) of the 3D visualization, made with `Three.js`. The code in this repository reads a `.txt` file and write a `.json` file with nodes and edges in 3 dimensions. 

The website for the visualization is not yet open (wip).

## Process

The script reads a network dataset from [SNAP](https://snap.stanford.edu/data/index.html) as a `.txt` file in the format:  
```
0 344   
0 347  
1 48    
1 73
```   

where each value is a node identifier. See `/datasets/original/facebook_combined.txt` for an example.  

From there, depending on the script, it sets up random walkers to isolate communities and thus, generate a subsample of the dataset.  

Via the `NetworkX` library, the script generates a 2D and 3D representation of the network based on a **spring layout**, ready to be visualized with a 3D visualization library. 

## From The CLI 

Below are the arguments, all mandatory:  

```
input_file  
output_file  
max_steps=20  
nb_random_walks=200  
k_index=0.001  
drawing=False  
key=0  
```

### Dependencies

Installing `matplotlib` and `networkx` should be enough and working. Tested with `Python 3.10.10`.  

If you are having issues with dependecies, I suggest you create a python `env` and install the dependencies via:  

`pip install -r requirements.txt`

### Example

`python script.py ./datasets/original/facebook_combined.txt ./datasets/synthetic/facebook_combined_iter 10 50 0.001 False 10` 

Reading the `facebook_combined.txt`, writing to a new dataset starting with `facebook_combined_iter`, setting 10 steps for each of 50 random points. `k_index` being the  _Optimal distance between nodes. If None the distance is set to 1/sqrt(n) where n is the number of nodes. Increase this value to move nodes farther apart._ in a spring layout ([source](https://networkx.org/documentation/stable/reference/generated/networkx.drawing.layout.spring_layout.html)).  

If set to **True**, the script will visualize a 2D spring layout network with `Matplotlib`. Note that it might take extra time based on the size of the network. The last argument is the number of iterations.  

Output example with `max_steps=2`, `nb_random_walks=2`, `k_index=0.001` for `1` iteration:    

```
{
  "nodes": {
    "107": [
      0.013743143865355406,
      0.4438340530634355,
      1
    ],
    "1296": [
      0.022100838457911293,
      0.4380845597977772,
      0.9960678508106035
    ],
    "1654": [
      0.02912112221211066,
      0.43389761571270147,
      0.9941745741615562
    ],
    "2663": [
      -0.013242633496894005,
      -0.4492755909877598,
      -0.9972450614691459
    ],
    "2978": [
      -0.02645170060453683,
      -0.43252164132501814,
      -0.9964643466436035
    ],
    "3231": [
      -0.02527077043394653,
      -0.4340189962611342,
      -0.9965330168594111
    ]
  },
  "edges": [
    [
      [
        0.02912112221211066,
        0.43389761571270147,
        0.9941745741615562
      ],
      [
        0.013743143865355406,
        0.4438340530634355,
        1
      ]
    ],
    [
      [
        0.013743143865355406,
        0.4438340530634355,
        1
      ],
      [
        0.022100838457911293,
        0.4380845597977772,
        0.9960678508106035
      ]
    ],
    [
      [
        -0.02645170060453683,
        -0.43252164132501814,
        -0.9964643466436035
      ],
      [
        -0.013242633496894005,
        -0.4492755909877598,
        -0.9972450614691459
      ]
    ],
    [
      [
        -0.013242633496894005,
        -0.4492755909877598,
        -0.9972450614691459
      ],
      [
        -0.02527077043394653,
        -0.4340189962611342,
        -0.9965330168594111
      ]
    ]
  ]
}
```  

and the file will end with `0.001_0.json` (`k_index` value and `iteration` number).  

Will be available for drawing 6 nodes (with their 3D coordinates) and an array of links with a starting node and an ending node.  

# Resources

- [NetworkX](https://networkx.org/documentation/latest/index.html)
- [SNAP Datasets](https://snap.stanford.edu/data/index.html)
- [Facebook Example](https://snap.stanford.edu/data/ego-Facebook.html) - version `facebook_combined.txt.gz`

# Reuse/Collaboration

Feel free to reach out/issues/PR if you want to improve the code, or think about enhancement for 3D visualizations. Feel free to reuse any part of the code and let me know if you do!