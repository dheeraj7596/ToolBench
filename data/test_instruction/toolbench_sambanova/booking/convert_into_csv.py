import pandas as pd
import json


def modify(api, functions):
    lines = api.strip().split("\n")
    dic = {}
    temp_line = ""
    for l in lines:
        if l.startswith("API."):
            dic[l.strip().split("(")[0]] = temp_line + l.strip()
            temp_line = ""
        else:
            temp_line = temp_line + l.strip() + "\n"
    api_list = []
    for f in functions:
        if f in dic:
            api_list.append(dic[f])
        else:
            api_list.append(f + "('None')")
    return "\n".join(api_list)


if __name__ == "__main__":
    in_path = "/private/home/dmekala/cores/ContinualToolformer/data/ToolBench_sambanova/booking/test.jsonl"
    out_path = "/private/home/dmekala/cores/ContinualToolformer/data/ToolBench_sambanova/booking/test.csv"
    functions_path = "/private/home/dmekala/cores/ContinualToolformer/data/ToolBench_sambanova/booking/function_names.txt"

    with open(functions_path, "r") as f:
        lines = f.readlines()
        functions = [l.strip() for l in lines]
        functions = functions[:-2]

    final_dic = {"Instruction": [], "api": [], "Name": []}
    with open(in_path, "r") as f:
        lines = f.readlines()
        for l in lines:
            dic = json.loads(l.strip())
            text = dic["prompt"]
            api = dic["completion"][0]
            tool = "Booking"
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
