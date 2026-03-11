#wengtengjin
from pathlib import Path
import json
import os
import re
from concurrent.futures import ProcessPoolExecutor, as_completed


def build_prompt(data: dict) -> str:
    rows, cols = data.get("grid_size", [0, 0])
    shape = "object"
    odd_types = data.get("odd_type", [])
    odd_desc = ", ".join(odd_types) if odd_types else "appearance"
    prompt = f"\n <image> Identify the object that differs from others in the {rows}×{cols} grid. Count from the top-left as Row 1, Column 1. Give your answer in the form: \\boxed{{Row X, Column Y}}."

    return prompt

def build_prompt_rl(data: dict) -> str:
    rows, cols = data.get("grid_size", [0, 0])
    shape = data.get("shape", "object")

    # 如果 shape 是纯数字且在 0~100000 之间，都归为 "object"
    if isinstance(shape, str) and shape.isdigit():
        num = int(shape)
        if 0 <= num <= 100000:
            shape = "object"
    shape = "object"
    odd_types = data.get("odd_type", [])
    odd_desc = ", ".join(odd_types) if odd_types else "appearance"

    prompt = (
        f"Identify the {shape} that differs from others in the {rows}×{cols} grid. "
        f"The difference is in {odd_desc}. "
        f"Count from the top-left as Row 1, Column 1. "
        f"Give your answer in the form: \\boxed{{Row X, Column Y}}."
    )
    return prompt


def build_prompt_oddgridbench(data: dict) -> str:
    rows, cols = data.get("grid_size", [0, 0])
    shape = "object"
    odd_types = data.get("odd_type", [])
    
    odd_desc = ", ".join(odd_types) if odd_types else "appearance"

    prompt = f"""
    You are solving an **Odd-One-Out Visual Perception** task.

    You are given an image showing a {rows}×{cols} grid of {shape}s.
    All {shape}s look identical except one that differs in its {odd_desc}.

    This is a **pure visual perception** task — no reasoning or calculation is required.

    ### Task
    - Carefully inspect the grid.
    - Identify the {shape} that looks different.
    - Report its grid position (Row and Column), counting from the top-left corner as Row 1, Column 1.

    ### Output Format
    Only output the result in **exactly** this format:

    \\boxed{{Row X, Column Y}}

    Replace X and Y with the correct row and column numbers.
    For example:

    \\boxed{{Row 2, Column 3}}
    """
    return prompt

def Extract_answer(predict_answer: str) -> str:
    """
    Extract the final boxed answer of the form \boxed{Row X, Column Y}.
    X and Y must be integers.
    """
    # 匹配 \boxed{Row X, Column Y}，允许空格，大小写忽略
    matches = re.findall(
        r"\\boxed\{\s*Row\s+(\d+)\s*,\s*Column\s+(\d+)\s*\}", 
        predict_answer, 
        flags=re.IGNORECASE
    )

    if len(matches) == 1:
        row, col = matches[0]
        return f"Row {row}, Column {col}"
    elif len(matches) > 1:
        return "Many answers found"
    else:
        return "No answer found"


def remove_existing_file(save_path):
    """
    Remove the file at the specified path if it exists.

    Args:
        save_path (str): Path of the file to remove.
    """
    if os.path.exists(save_path):
        os.remove(save_path)
        print(f"Existing file removed: {save_path}")

def write_json(save_json_path, save_json_data):
    if os.path.exists(save_json_path):
        with open(save_json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            data.append(save_json_data)
        else:
            data = [data, save_json_data]
    else:
        data = [save_json_data]

    with open(save_json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)