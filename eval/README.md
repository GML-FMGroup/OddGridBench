# Evaluation Guidelines

This directory provides the scripts for evaluating models on **OddGridBench**.  
To ensure fair comparison, please follow the same evaluation pipeline and output format as provided in this repository.


## Evaluation Pipeline

The evaluation process mainly includes the following steps:

1. **Load the dataset**
2. **Run model inference**
3. **Extract answers from model outputs**
4. **Compute final accuracy**

We provide example scripts for each step.

---

## Data Loading

You can load the OddGridBench dataset using HuggingFace:

```python
from datasets import load_dataset
dataset = load_dataset("wwwtttjjj/OddGridBench")
```
Alternatively, you can manually download the datasets and place them under the datasets/ directory with the following structure:
datasets/
├── OddGridBench
├── MNIST
├── SCC
├── MVTec-AD
└── VisA
Please ensure that the dataset folders follow the same structure as above before running the evaluation scripts.

## Configuration

Before running the evaluation, please configure the model and dataset settings in `configs.py`.

- **model_dir**: the local path of the model weights  
- **model_name**: the model name used for evaluation  
- **data_type**: the dataset used for evaluation  

Supported datasets include:

- `OddGridBench`
- `MNIST`
- `SCC`
- `MVTec-AD`
- `VisA`

---

## Run Inference

After configuration, run the following script to perform model inference:

```python
python vlm_infer.py
```
