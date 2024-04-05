from road import Road
from Droad import Car, Truck, TrafficLight
from GUI import MetricGUI, ImperialGUI  
from print_driver import ConsolePrint
from map import Map, CharMatrix
from constants import Constants, Heading
import time

def print_traffic_lights(traffic_lights, char_matrix):
    # 第一个信号灯的行索引
    first_tl_row_index = len(char_matrix.map) - 13
    # 第二个信号灯的行索引应该比第一个信号灯的行索引小 13
    second_tl_row_index = first_tl_row_index - 13

    # 打印第一个信号灯
    symbol = {'red': 'X', 'yellow': '-', 'green': 'O'}[traffic_lights[0].current_color]
    char_matrix.map[first_tl_row_index][traffic_lights[0].mile_marker] = symbol

    # 打印第二个信号灯
    symbol = {'green': 'O','red': 'X', 'yellow': '-' }[traffic_lights[1].current_color]
    char_matrix.map[second_tl_row_index][traffic_lights[1].mile_marker] = symbol



def main():
    sim_input = MetricGUI()
    map_obj = Map()
    cp = ConsolePrint()

    # 创建道路
    uptown = sim_input.create_road("Uptown", 0, -0.09, 0.180, Heading.North)
    map_obj.add_road(uptown)

    # 创建第一个信号灯
    traffic_light1 = TrafficLight(mile_marker=26, red_duration=5, yellow_duration=2, green_duration=3)
    # 创建第二个信号灯，位于第一个信号灯上方13行
    traffic_light2 = TrafficLight(mile_marker=26, green_duration=5, yellow_duration=2, red_duration=3)
    traffic_light2.current_color = 'green'
    # 将两个信号灯放入列表
    traffic_lights = [traffic_light1, traffic_light2]

    # 模拟一段时间，这里设置为1秒，用于测试
    for time_step in range(10):
        # 更新交通灯
        for tl in traffic_lights:
            tl.update()

        # 创建一个新的字符矩阵
        cm = CharMatrix()

        # 更新交通灯在字符矩阵上的显示
        print_traffic_lights(traffic_lights, cm)

        # 使用map_obj的打印方法来打印地图
        map_obj.print(cp, cm)

        for row in cm.map:
            print(''.join(row))

        # 暂停1秒钟
        time.sleep(1)

if __name__ == "__main__":
    main()