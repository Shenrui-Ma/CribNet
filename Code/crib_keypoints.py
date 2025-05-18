import json

# 你的数据文件路径
with open('/data1/shenrui.ma/Infant-Pose-Estimation/syn_generation/data/keypoints/46_keypoints.json') as f:
    data = json.load(f)

# 假设 data["annotations"] 是长度51的list
kpts_flat = data["annotations"]
assert len(kpts_flat) == 51, "关键点数量应为51"

# 扁平list切分成17×3
keypoints = [kpts_flat[i:i+3] for i in range(0, len(kpts_flat), 3)]

# 写成CribNet脚本需要的格式
out_data = {"keypoints": keypoints}

with open('keypoints_for_cribnet.json', 'w') as f:
    json.dump(out_data, f)