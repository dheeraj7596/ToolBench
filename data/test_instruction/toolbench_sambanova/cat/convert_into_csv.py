import pandas as pd
import json

if __name__ == "__main__":
    in_path = "/private/home/dmekala/cores/ContinualToolformer/data/ToolBench_sambanova/cat/test.jsonl"
    out_path = "/private/home/dmekala/cores/ContinualToolformer/data/ToolBench_sambanova/cat/test.csv"
    tool_docs_path = "/private/home/dmekala/cores/ContinualToolformer/data/ToolBench_sambanova/cat/Tool_Documentations_cat.xlsx"

    tool_docs_df = pd.read_excel(tool_docs_path, sheet_name="API")
    endpoint_to_tool = {}
    for i, row in tool_docs_df.iterrows():
        endpoint_to_tool[row["API endpoint"]] = row["Name"]

    final_dic = {"Instruction": [], "api": [], "Name": [], "compare_string_only": []}
    with open(in_path, "r") as f:
        lines = f.readlines()
        for l in lines:
            dic = json.loads(l.strip())
            text = dic["prompt"]
            api = dic["completion"][0]
            compare_str_only = dic["compare_string_only"]
            tool = None
            for e in endpoint_to_tool:
                if e in api:
                    if e == """curl -X POST 'https://api.thecatapi.com/v1/votes'""":
                        if "-1}" in api:
                            tool = "Vote down"
                        elif "1}" in api:
                            tool = "Vote up"
                        else:
                            raise Exception("Wrong string found", api)
                    else:
                        tool = endpoint_to_tool[e]
            try:
                assert tool is not None
            except:
                print(text)
                print(api)
                raise Exception("Tool not found")
            final_dic["Instruction"].append(text)
            final_dic["api"].append(api)
            final_dic["Name"].append(tool)
            final_dic["compare_string_only"].append(compare_str_only)

    final_df = pd.DataFrame.from_dict(final_dic)
    final_df.to_csv(out_path, index=False)
