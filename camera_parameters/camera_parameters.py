import numpy as np

# infr1 -> 中间的红外摄像头
# infr2 -> 左边的红外摄像头
# infr1 -> infr2:
R_infr1_to_infr2 = np.array([[1.0, 0.0, 0.0],
                             [0.0, 1.0, 0.0],
                             [0.0, 0.0, 1.0]])
T_infr1_to_infr2 = np.array([-0.049985144287347794, 0.0, 0.0])

# infr2 -> infr1:
R_infr2_to_infr1 = np.array([[1.0, 0.0, 0.0],
                             [0.0, 1.0, 0.0],
                             [0.0, 0.0, 1.0]])
T_infr2_to_infr1 = np.array([0.049985144287347794, 0.0, 0.0])

# infr1 -> color:
R_infr1_to_color = np.array([[0.9999839067459106, -0.005434882361441851, 0.0016148093855008483],
                             [0.005436081439256668, 0.9999849796295166, -0.0007390331011265516],
                             [-0.0016107684932649136, 0.0007477994658984244, 0.9999984502792358]])

T_infr1_to_color = np.array([0.014913409948348999, -7.743491005385295e-05, -0.00016766598855610937])

# color -> infr1
R_color_to_infr1 = np.array([[0.9999839067459106, 0.005436081439256668, -0.0016107684932649136],
                             [-0.005434882361441851, 0.9999849796295166, 0.0007477994658984244],
                             [0.0016148093855008483, -0.0007390331011265516, 0.9999984502792358]])
T_color_to_infr1 = np.array([-0.014913320541381836, -3.760677373065846e-06, 0.00019174566841684282])

# color -> infr2:
R_color_to_infr2 = np.array([[0.9999839067459106, 0.005436081439256668, -0.0016107684932649136],
                             [-0.005434882361441851, 0.9999849796295166, 0.0007477994658984244],
                             [0.0016148093855008483, -0.0007390331011265516, 0.9999984502792358]])
T_color_to_infr2 = np.array([-0.06489846110343933, -3.760677373065846e-06, 0.00019174566841684282])

# infr2 -> color:
R_infr2_to_color = np.array([[0.9999839067459106, -0.005434882361441851, 0.0016148093855008483],
                             [0.005436081439256668, 0.9999849796295166, -0.0007390331011265516],
                             [-0.0016107684932649136, 0.0007477994658984244, 0.9999984502792358]])

T_infr2_to_color = np.array([[0.06489774584770203, -0.000349098292645067, -8.694950520293787e-05]])

# infr1 -> 内参:
intrinsics_infr1 = np.array([[384.613, 0.0, 319.544],
                             [0.0, 384.613, 240.34],
                             [0.0, 0.0, 1.0]])
# infr2 -> 内参:
intrinsics_infr2 = np.array([[384.613, 0.0, 319.544],
                             [0.0, 384.613, 240.34],
                             [0.0, 0.0, 1.0]])
# color -> 内参:
intrinsics_color = np.array([[610.91, 0.0, 325.979],
                             [0.0, 610.187, 228.505],
                             [0.0, 0.0, 1.0]])

"""intrinsics"""
# intrin_depth = aligned_depth_frame.profile.as_video_stream_profile().intrinsics
# intrin_color = aligned_color_frame.profile.as_video_stream_profile().intrinsics
# intrin_infr1 = alighed_infr_frame1.profile.as_video_stream_profile().intrinsics
# intrin_infr2 = alighed_infr_frame2.profile.as_video_stream_profile().intrinsics

"""extrinsics"""
# extrin_depth_to_color = aligned_depth_frame.profile.get_extrinsics_to(aligned_color_frame.profile)
# extrin_infr_to_color1 = alighed_infr_frame1.profile.get_extrinsics_to(aligned_color_frame.profile)
# extrin_infr_to_color2 = alighed_infr_frame2.profile.get_extrinsics_to(aligned_color_frame.profile)
# extrin_infr1_to_intr2 = alighed_infr_frame1.profile.get_extrinsics_to(alighed_infr_frame2.profile)
