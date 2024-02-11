import os
import pandas as pd
import json


def get_api_list(path):
    api_list = []
    dic = json.load(open(path, "r"))
    for d in dic["api_list"]:
        temp = {}
        temp["category_name"] = "toolver"
        temp["tool_name"] = "sambanova"
        temp["api_name"] = d["name"]
        temp["api_description"] = d["description"]
        temp["required_parameters"] = d["required_parameters"]
        temp["optional_parameters"] = d["optional_parameters"]
        temp["method"] = d["method"]
        api_list.append(temp)
    return api_list


if __name__ == "__main__":
    in_dir = "/Users/dheerajmekala/Work/ToolBench/data/test_instruction/toolbench_sambanova/cat"
    csv_path = os.path.join(in_dir, "test.csv")
    df = pd.read_csv(csv_path)
    api_list = get_api_list("/Users/dheerajmekala/Work/ToolBench/data/toolenv/tools/toolver/sambanova.json")
    final_list = []
    id_counter = 0
    for i, row in df.iterrows():
        query = row["Instruction"]
        query_id = id_counter
        final_list.append(
            {
                "query": query,
                "query_id": query_id,
                "api_list": api_list
            }
        )
        id_counter += 1
    with open(os.path.join(in_dir, "ins.json"), "w") as fp:
        json.dump(final_list, fp)
