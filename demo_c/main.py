import json
import simulator_setting
import create_scene
import post_processing
import animate_controller
import path_controller
import position_estimate

def createScene(root_node):

    # f = open("GUI_interface/ceshi.txt", "r", encoding="UTF-8")
    f = open("GUI_interface/info_capsule_elc_soft_stomach.txt", "r", encoding="UTF-8")
    # f = open("GUI_interface/info_capsule_elc_center.txt", "r", encoding="UTF-8")
    # f = open("GUI_interface/info_location.txt", "r", encoding="UTF-8")
    # f = open("GUI_interface/info_Helmholtz_Maxwell.txt", "r", encoding="UTF-8")
    # f = open("GUI_interface/info_wire_elc_hard_brains.txt", "r", encoding="UTF-8")
    # f = open("GUI_interface/info_wire_elc_soft_brains.txt", "r", encoding="UTF-8")
    # f = open("GUI_interface/info_wire_elc_hard_bronchus.txt", "r", encoding="UTF-8")
    # f = open("GUI_interface/info_wire_rob_hard_bronchus.txt", "r", encoding="UTF-8")
    # f = open("GUI_interface/info_wire_elc_hard_arc.txt", "r", encoding="UTF-8")
    # f = open("GUI_interface/info_wire_elc_soft_arc.txt", "r", encoding="UTF-8")

    json_str = f.read()
    initial_info = json.loads(json_str)

    # 环境
    simulator = simulator_setting.Simulator(root_node, info=initial_info)

    # 场景
    scene = create_scene.Scene(root_node, info=initial_info)

    path = None
    pose_estimate = None

    if initial_info[6]:
        # 路径
        path = path_controller.Path(root_node, initial_info, scene)

    if initial_info[7]:
        # 定位
        pose_estimate = position_estimate.Position_Estimate(initial_info, scene)
        root_node.addObject(pose_estimate)

    if path and pose_estimate:
        # 循环
        mag_controller = animate_controller.MagController(root_node, info=initial_info, simulator=simulator, scene=scene, path=path,
                                                          pose_estimate=pose_estimate)
        root_node.addObject(mag_controller)

        # 后处理
        post = post_processing.Post_processing(scene, path, pose_estimate, mag_controller=mag_controller, environment=simulator)
        root_node.addObject(post)
