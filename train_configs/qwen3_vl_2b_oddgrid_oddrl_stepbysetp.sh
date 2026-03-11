#!/bin/bash
set -e  # 出错即停止脚本
set -x  # 打印命令执行日志

MODEL_PATH=""  # 替换为你的模型路径
n_gpus_per_node=4
experiment_name=qwen3_vl_2b_oddgrid_oddrl_stepbystep # 替换为你的实验名称

easy_data_path=easy.jsonl # 替换为你的easy数据路径
medium_data_path=medium_easy.jsonl # 替换为你的medium数据路径
hard_data_path=hard_medium_easy.jsonl # 替换为你的hard数据路径


# === Step 1: easy ===
python3 -m verl.trainer.main \
  config=config.yaml \
  data.train_files=${easy_data_path} \
  worker.actor.model.model_path=${MODEL_PATH} \
  trainer.experiment_name=${experiment_name} \
  worker.actor.global_batch_size=256 \
  worker.actor.micro_batch_size_per_device_for_update=4 \
  data.format_prompt=./format_prompt/oddgrid.jinja \
  worker.rollout.tensor_parallel_size=1 \
  worker.reward.reward_function=./reward_function/math.py:compute_odd_score \
  trainer.n_gpus_per_node=${n_gpus_per_node} \
  trainer.max_steps=20


# === Step 2: medium ===
python3 -m verl.trainer.main \
  config=config.yaml \
  data.train_files=${medium_data_path} \
  worker.actor.model.model_path=${MODEL_PATH} \
  trainer.experiment_name=${experiment_name} \
  worker.actor.global_batch_size=256 \
  worker.actor.micro_batch_size_per_device_for_update=4 \
  data.format_prompt=./format_prompt/oddgrid.jinja \
  worker.rollout.tensor_parallel_size=1 \
  worker.reward.reward_function=./reward_function/math.py:compute_odd_score \
  trainer.n_gpus_per_node=${n_gpus_per_node} \
  trainer.max_steps=60


# === Step 3: hard ===
python3 -m verl.trainer.main \
  config=config.yaml \
  data.train_files=${hard_data_path} \
  worker.actor.model.model_path=${MODEL_PATH} \
  trainer.experiment_name=${experiment_name} \
  worker.actor.global_batch_size=256 \
  worker.actor.micro_batch_size_per_device_for_update=4 \
  data.format_prompt=./format_prompt/oddgrid.jinja \
  worker.rollout.tensor_parallel_size=1 \
  worker.reward.reward_function=./reward_function/math.py:compute_odd_score \
  trainer.n_gpus_per_node=${n_gpus_per_node} \
  trainer.max_steps=100
