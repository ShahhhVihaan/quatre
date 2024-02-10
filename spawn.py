#!/usr/bin/python3

import mujoco
import mujoco.viewer
import numpy as np
import time

def main() -> None:
    model = mujoco.MjModel.from_xml_path("unitree_go1/scene.xml")
    data = mujoco.MjData(model)
    
    model.body_gravcomp[:] = 1.0
    
    with mujoco.viewer.launch_passive(
        model=model,
        data=data,
        show_left_ui=True,
        show_right_ui=True,
    ) as viewer:
        mujoco.mjv_defaultFreeCamera(model, viewer.cam)
        
        while viewer.is_running():
            viewer.sync()

if __name__ == "__main__":
    main()
