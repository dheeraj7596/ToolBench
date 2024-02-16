import pandas as pd


def modify(api, tool):
    if tool in ["Forecast Air Pollution",
                "Current Air Pollution",
                "Geographical Coordinates",
                "Current Weather City",
                "Forecast Weather City",
                "Forecast Weather Latitude Longitude",
                "Forecast Weather Zipcode",
                "Current Weather Latitude Longitude",
                "Current Weather Zipcode"]:
        pred_dataset = "weather"
    elif tool in ["Delete image from favorites",
                  "Find images",
                  "Get favorite cat images",
                  "Post to favorites",
                  "Vote down",
                  "Vote up"]:
        pred_dataset = "cat"
    else:
        pred_dataset = None

    if pred_dataset is None:
        return api
    elif pred_dataset == "weather":
        if api.startswith("curl"):
            return "curl -X GET " + api.strip().split("curl -X GET ")[-1].lower()
        else:
            return f"curl -X GET '{api.lower()}'"
    elif pred_dataset == "cat":
        if api.startswith("curl"):
            return api
        else:
            if tool == "Delete image from favorites":
                return f"curl -X DELETE '{api}'"
            elif tool in ["Find images", "Get favorite cat images"]:
                return f"curl -X GET '{api}'"
            else:
                return api


def parse_api(outer_lines, dataset, tool):
    ind = 0
    if dataset != "home" and dataset != "booking":
        api = outer_lines[ind].strip().split("API:")[1].strip()
    else:
        lines = outer_lines[ind:]
        api_lines = []
        for i, l in enumerate(lines):
            if i == 0:
                l_strip = l.split("API:")[1].strip()
            elif l.strip() == "###":
                break
            else:
                l_strip = l.strip()
            api_lines.append(l_strip)
            if l_strip == "API.search()":
                break
        api = "\n".join(api_lines)
    mod_api = modify(api, tool)
    return mod_api


if __name__ == "__main__":
    dataset = "weather"
    in_file_path = f"/Users/dheerajmekala/Work/ToolBench/data/test_instruction/toolbench_sambanova/{dataset}/logs/out.txt"
    test_csv_path = f"/Users/dheerajmekala/Work/ToolBench/data/test_instruction/toolbench_sambanova/{dataset}/test.csv"
    out_path = f"/Users/dheerajmekala/Work/ToolBench/data/test_instruction/toolbench_sambanova/{dataset}/pred_api_toollama.csv"

    f = open(in_file_path, "r")
    df = pd.read_csv(test_csv_path)
    gt_tools = list(df["Name"])

    lines = f.readlines()
    pred_tools = {}
    pred_apis = {}
    instructions = {}
    instruction_found = False
    tool = None
    api = None
    task_id = None
    ins = None
    first_one = True
    for idx, l in enumerate(lines):
        l = l.strip()
        if l.startswith("process[0] doing task"):
            if instruction_found:
                if api is None:
                    print("API is None:", ins)
                    api = ""
                    print("Pred tool:", tool)
                if tool is None:
                    print("Tool is None:", ins)
                    tool = ""
                assert task_id is not None
                assert ins is not None
                pred_apis[task_id] = api
                pred_tools[task_id] = tool
                instructions[task_id] = ins
                instruction_found = False
                tool = None
                api = None
                ins = None
            elif not first_one:
                task_id = int(l.split("real_task_id_")[-1].strip())
                print("Task ID INS missing", task_id)
            first_one = False
            task_id = int(l.split("real_task_id_")[-1].strip())
        elif l.startswith("INS:"):
            ins = l.split("INS:")[-1].strip()
            instruction_found = True
        elif l.startswith("TOOL:"):
            tool = l.split("TOOL:")[-1].strip()
        elif l.startswith("API:"):
            if tool is None:
                if "API.set_location" in l:
                    tool = "Home search"
                elif "API.select_booking_type" in l:
                    tool = "Booking"
            assert tool is not None
            api = parse_api(lines[idx:], dataset, tool)

    if instruction_found:
        if api is None:
            print("API is None:", ins)
            api = ""
            print("Pred tool:", tool)
        if tool is None:
            print("Tool is None:", ins)
            tool = ""
        assert task_id is not None
        assert ins is not None
        pred_apis[task_id] = api
        pred_tools[task_id] = tool
        instructions[task_id] = ins
        instruction_found = False
        tool = None
        api = None
        ins = None
    else:
        print("Task ID INS missing", task_id)

    out_dic = {"Instruction": [], "Pred": [], "Tool_Pred": []}
    num_total = len(gt_tools)
    for i in range(num_total):
        gt_tool = gt_tools[i]
        try:
            ins = instructions[i]
        except:
            print("INS missing", i)
            ins = ""
        try:
            pred_api = pred_apis[i]
        except:
            pred_api = ""
        try:
            pred_tool = pred_tools[i]
        except:
            pred_tool = ""
        if pred_tool == gt_tool:
            tool_pred = 1
        else:
            tool_pred = 0
        out_dic["Instruction"].append(ins)
        out_dic["Pred"].append(pred_api)
        out_dic["Tool_Pred"].append(tool_pred)

    print("Tool Accuracy:", sum(out_dic["Tool_Pred"]))
    pd.DataFrame.from_dict(out_dic).to_csv(out_path, index=False)
