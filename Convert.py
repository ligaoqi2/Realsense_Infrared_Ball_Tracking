import numpy as np


def project_point(point, camera1_intrinsics, camera1_extrinsics, camera2_intrinsics, T, Depth):
    point_homogeneous = np.append(point, 1) * Depth
    camera1_intrinsics_ni = np.linalg.inv(camera1_intrinsics)
    point_world = camera1_intrinsics_ni @ point_homogeneous
    point_camera2_homogeneous = camera1_extrinsics @ point_world + T
    point_camera2 = camera2_intrinsics @ point_camera2_homogeneous
    point_camera2 = point_camera2[:2] / point_camera2[2]
    return point_camera2


def estimateDepth(point_left, point_right):
    camera_baseline = 4.9985144287347794
    camera_left_f = 384.613
    depth = camera_baseline * camera_left_f / (point_left[0] - point_right[0])
    return depth


def getPointXYZ(u, v, camera_matrix, d):
    X = (u - camera_matrix[0][2]) * d / camera_matrix[0][0]
    Y = (v - camera_matrix[1][2]) * d / camera_matrix[1][1]
    Z = d
    return [X, Y, Z]
