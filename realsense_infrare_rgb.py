# -*- coding: utf-8 -*-
# encoding: utf-8print

import pyrealsense2 as rs
import numpy as np
import cv2

from camera_parameters.camera_parameters import *
from InfraDetect import detect
from Convert import estimateDepth, project_point, getPointXYZ

pipeline = rs.pipeline()
config = rs.config()

config.enable_stream(rs.stream.infrared, 1, 640, 480, rs.format.y8, 30)  # infrared stream
config.enable_stream(rs.stream.infrared, 2, 640, 480, rs.format.y8, 30)  # infrared stream
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)  # rgb stream

pipe_profile = pipeline.start(config)

align_to = rs.stream.color
align = rs.align(align_to)

while True:
    frames = pipeline.wait_for_frames()
    aligned_frames = align.process(frames)

    """get frame"""
    aligned_color_frame = aligned_frames.get_color_frame()
    alighed_infr_frame1 = aligned_frames.get_infrared_frame(1)
    alighed_infr_frame2 = aligned_frames.get_infrared_frame(2)

    """to numpy"""
    img_color = np.asanyarray(aligned_color_frame.get_data())
    img_infr1 = np.asanyarray(alighed_infr_frame1.get_data())
    img_infr2 = np.asanyarray(alighed_infr_frame2.get_data())

    """detect marker"""
    img1, joints_2d1 = detect(img_infr1)
    img2, joints_2d2 = detect(img_infr2)

    if joints_2d1 is not None and joints_2d2 is not None:
        if len(joints_2d1) == len(joints_2d2):
            Depth = 0
            for i in range(len(joints_2d1)):
                Depth = estimateDepth(joints_2d1[i], joints_2d2[i])
                pointXYZ = getPointXYZ(joints_2d1[i][0], joints_2d1[i][1], intrinsics_infr1, Depth)
                color_point = project_point(joints_2d1[i], intrinsics_infr1, R_infr1_to_color, intrinsics_color, T_infr1_to_color, Depth)
                cv2.circle(img_color, (int(color_point[0]), int(color_point[1])), 5, (0, 0, 255), -1)
                print("第 {} 个3D点坐标为: {}".format(i, pointXYZ))
        else:
            print("左右相机检测到的Marker数不同")

    else:
        print("有红外摄像头未检测到Marker点")

    cv2.imshow("rgb", img_color)
    cv2.imshow("img1", img1)
    cv2.imshow("img2", img2)

    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
