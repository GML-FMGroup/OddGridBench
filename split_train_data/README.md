# Split Training Data

This folder provides scripts for preparing the training data used in **OddGrid-GRPO**.

The training data are divided into three difficulty levels (**easy / medium / hard**) for curriculum-guided training.

---

## Step 1: Convert Data Format

First convert the dataset into the RL training format:

```bash
python split_easy_med_hard.py
```