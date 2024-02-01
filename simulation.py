from dynamic_road_item import DynamicRoadItem


class Simulation:
    def __init__(self, gui=None):
        self.dynamic_road_items = []  # 保存所有动态路面项目
        self.gui = gui
    def update(self, seconds: int):
        # Update status of all dynamic pavement items
        for item in self.dynamic_road_items:
            item.update(seconds)

    def add_dynamic_road_item(self, item):
        # Only Dynamic Items of type should be added
        if isinstance(item, DynamicRoadItem):
            self.dynamic_road_items.append(item)
        else:
            raise ValueError("Only dynamic road items can be added.")