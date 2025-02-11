import json
from src.components import Composite

class JSONBuilder:
    def build(self, json_file):
        # 读取 JSON 文件内容
        with open(json_file, 'r') as file:
            data = json.load(file)
        # 构建组件树
        return self.buildComponent(data, "root", 0)

    def buildComponent(self, data, name, depth):
        # 如果数据是列表类型
        if isinstance(data, list):
            component = Composite(name, depth)
            for index, item in enumerate(data):
                child = self.buildComponent(item, f"{name}[{index}]", depth + 1)
                component.addChild(child)
        # 如果数据是字典类型
        elif isinstance(data, dict):
            component = Composite(name, depth)
            for key, value in data.items():
                child = self.buildComponent(value, key, depth + 1)
                component.addChild(child)
        # 如果数据是叶子节点
        else:
            if data is not None:
                component = Composite(f"{name}: {data}", depth)
            else:
                component = Composite(name, depth)
        return component
