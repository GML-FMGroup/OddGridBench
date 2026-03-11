#wengtengjin

import os
max_new_tokens = 1024

models_dir = "/data/wengtengjin/models/"

def get_configs(args):
    if args.data_type == "MNIST":
        image_dir = f"../datasets/MNIST/iol_test_data/images"
        json_path = f"../datasets/MNIST/iol_test_data/iol_test_data.json"
    elif args.data_type == "SCC":
        image_dir = f"../datasets/SCC/iol_test_data/images"
        json_path = f"../datasets/SCC/iol_test_data/iol_test_data.json"
    elif args.data_type == "VisA":
        image_dir = f"../datasets/VisA/iol_test_data/images"
        json_path = f"../datasets/VisA/iol_test_data/iol_test_data.json"
    elif args.data_type == "MVtec-AD":
        image_dir = f"../datasets/MVtec-AD/iol_test_data/images"
        json_path = f"../datasets/MVtec-AD/iol_test_data/iol_test_data.json"
    elif args.data_type == "OddGridBench":
        image_dir = f"../datasets/OddGridBench/test_data/image"
        json_path = f"../datasets/OddGridBench/test_data.json"
        
    # 输出路径
    Result_root = args.data_type + "_output/"
        
    if not os.path.exists(Result_root):
        os.mkdir(Result_root)
    return {
        "data_type": args.data_type,
        "image_dir": image_dir,
        "json_path": json_path,
        "Result_root": Result_root,
        "models_dir": models_dir,
        "model_path": os.path.join(models_dir, args.model_name),
        "save_path": os.path.join(Result_root, f"{args.model_name}.json"),
    }