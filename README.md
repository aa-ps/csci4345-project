# Distributed Computing Using Ray
## Prerequisites

- **Operating System**: Make sure your device is running on Linux as it is recommended for running Ray.
- **Python Version**: Use Python 3.10 as it is the most stable for using Ray.

## Using Anaconda (Optional)

To manage your Python environments and dependencies, I recommend using Anaconda, especially if you are working with different Python versions.

1. **Install Anaconda**: Download and install Anaconda from [the official website](https://www.anaconda.com/products/individual).
2. **Create a Virtual Environment**: Create a new environment specifically for your Ray project:

   ```bash
   conda create -n ray_env python=3.10
   ```

3. **Activate the Virtual Environment**:

   ```bash
   conda activate ray_env
   ```

Now we can install Ray inside this isolated environment.

## Installing Dependencies

```bash
pip install -r requirements.txt
```

## Starting Ray

You can use Ray on a single machine or across a cluster of machines. To start Ray on the head node, run the following command in your terminal:

```bash
ray start --head
```

## Connecting Workers
After starting the head node, you should see instructions in the terminal output for connecting worker nodes to this head node.
```bash
ray start --address='HEAD_IP_ADDRESS:PORT'
```


## Running Scripts on Head Node

Once Ray has been started and you've set up your environment, you can run the provided example scripts.

1. **Navigate to the Script Directory**:
   
   ```bash
   cd CSCI4345-PROJECT
   ```

2. **Running `example1.py`**:

   ```bash
   RAY_ADDRESS='http://127.0.0.1:8265' ray job submit --working-dir . -- python example1.py
   ```
---

For more API references, visit the official [Ray Documentation](https://docs.ray.io/en/latest/).