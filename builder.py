import json
from components import Composite, Leaf

class JSONBuilder:
    def __init__(self, style_factory, icon_factory):
        self.style_factory = style_factory
        self.icon_factory = icon_factory

    def build(self, json_file):
        # 读取 JSON 文件内容
        with open(json_file, 'r') as file:
            data = json.load(file)
        # 构建组件树
        return self.build_component(data, "root")

    def build_component(self, data, name):
        # 如果数据是字典类型
        if isinstance(data, dict):
            component = self.style_factory.create_component(name, False)
            for key, value in data.items():
                child = self.build_component(value, key)
                component.add(child)
        else:
            # 如果数据是叶子节点
            if data is not None:
                component = self.style_factory.create_component(f"{name}: {data}", True)
            else:
                component = self.style_factory.create_component(name, True)
        return component
