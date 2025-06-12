import os
import json
from collections import defaultdict
from typing import Any

# 配置你的 games 目录路径
GAMES_DIR = './public/games'
OUTPUT_FILE = './public/games/summary/TagSummary.json'

def main():
    tag_map: dict[str, dict[str, Any]] = defaultdict(lambda: {"count": 0, "games": []})

    for filename in os.listdir(GAMES_DIR):
        # 跳过统计文件
        if not filename.endswith('.json') or filename == 'tag-summary.json':
            continue
        path = os.path.join(GAMES_DIR, filename)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            types = data.get('types', [])
            game_name = data.get('name', '[未知游戏]')
            # 链接去掉.json
            link = f"/games/{filename[:-5]}"
            for tag in types:
                if not isinstance(tag_map[tag]["count"], int):
                    tag_map[tag]["count"] = 0
                tag_map[tag]["count"] += 1
                tag_map[tag]["games"].append({"name": game_name, "link": link})
        except Exception as e:
            print(f"跳过 {filename}，原因：{e}")

    # 排序，生成输出结构
    tag_summary = []
    for tag, info in sorted(tag_map.items(), key=lambda x: -x[1]['count']):
        tag_summary.append({
            "tag": tag,
            "count": info["count"],
            "games": info["games"]
        })

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(tag_summary, f, ensure_ascii=False, indent=2)

    print(f"已生成标签统计文件：{OUTPUT_FILE}")

if __name__ == '__main__':
    main()