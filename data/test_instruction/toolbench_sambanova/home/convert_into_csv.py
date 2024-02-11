import pandas as pd
import json


def modify(api, functions):
    lines = api.strip().split("\n")
    dic = {}
    for l in lines:
        dic[l.strip().split("(")[0]] = l.strip()
    api_list = []
    for f in functions:
        if f in dic:
            api_list.append(dic[f])
        else:
            api_list.append(f + "('None')")
    return "\n".join(api_list)


if __name__ == "__main__":
    in_path = "/private/home/dmekala/cores/ContinualToolformer/data/ToolBench_sambanova/home/test.jsonl"
    out_path = "/private/home/dmekala/cores/ContinualToolformer/data/ToolBench_sambanova/home/test.csv"
    functions_path = "/private/home/dmekala/cores/ContinualToolformer/data/ToolBench_sambanova/home/function_names.txt"

    with open(functions_path, "r") as f:
        lines = f.readlines()
        functions = [l.strip() for l in lines]

    final_dic = {"Instruction": [], "api": [], "Name": []}
    with open(in_path, "r") as f:
        lines = f.readlines()
        for l in lines:
            dic = json.loads(l.strip())
            text = dic["prompt"]
            api = dic["completion"][0]
            tool = "Home search"
            try:
                assert tool is not None
            except:
                print(text)
                print(api)
                raise Exception("Tool not found")
            final_dic["Instruction"].append(text)
            api_modified = modify(api, functions)
            final_dic["api"].append(api_modified)
            final_dic["Name"].append(tool)

    final_df = pd.DataFrame.from_dict(final_dic)
    final_df.to_csv(out_path, index=False)
