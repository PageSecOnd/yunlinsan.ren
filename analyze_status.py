import os
import json

def analyze_json_files(input_directory, output_file):
    # 创建一个列表用于存储提取的数据
    summary_data = []

    # 遍历指定目录中的所有文件
    for filename in os.listdir(input_directory):
        # 确保只处理JSON文件
        if filename.endswith('.json'):
            file_path = os.path.join(input_directory, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)

                    # 提取所需字段
                    extracted_data = {
                        'name': data.get('name'),
                        'alias': data.get('alias'),
                        'logo': data.get('logo'),
                        'cover': data.get('cover'),
                        'status': data.get('status'),
                        'achievement_progress': data.get('achievement_progress'),
                        'achievement_total': data.get('achievement_total'),
                        'types': data.get('types'),
                        'rating': data.get('rating'),
                        'price': data.get('price'),
                        'steamdb': data.get('steamdb'),
                        'url': f"/games/{os.path.splitext(filename)[0]}"  # 去掉文件名中的 .json 后缀
                    }
                    summary_data.append(extracted_data)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    # 将汇总数据写入输出文件
    try:
        with open(output_file, 'w', encoding='utf-8') as output_file:
            json.dump(summary_data, output_file, ensure_ascii=False, indent=4)
        print(f"Summary data written to {output_file.name}")
    except Exception as e:
        print(f"Error writing to output file: {e}")

# 配置输入目录和输出文件
if __name__ == "__main__":
    input_directory = "./public/games"  # 替换为你的目录路径
    output_file = "./public/games/summary/StatsSummary.json"  # 输出文件名

    # 运行分析函数
    analyze_json_files(input_directory, output_file)