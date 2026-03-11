# Training

The training pipeline of **OddGrid-GRPO** is built upon the  
[EasyR1](https://github.com/hiyouga/EasyR1) reinforcement learning framework.

Most training configurations (model loading, distributed training, optimizer settings, etc.) follow the standard EasyR1 setup.

---

## Environment Setup

Please follow the official EasyR1 instructions to set up the environment:

https://github.com/hiyouga/EasyR1


You may modify these files according to your training setup.

---
## Training Data

OddGrid-GRPO adopts a **curriculum-guided training strategy**, where the training data are divided into three difficulty levels:

- **easy_data_path**  
  Path to the **easy-level training samples**, containing simple discrepancy cases.

- **medium_data_path**  
  Path to the **medium-level training samples**, which include moderately difficult discrepancy patterns.

- **hard_data_path**  
  Path to the **hard-level training samples**, containing complex discrepancy combinations and challenging cases.

During training, the model is optimized progressively from **easy → medium → hard**, enabling more stable learning and better visual discrepancy sensitivity. Please refer to our [split_train_data](split_train_data) folder for more details.

## Run Training

After preparing the environment and data, simply run:

```python
bash oddgrid-grpo.sh
```
