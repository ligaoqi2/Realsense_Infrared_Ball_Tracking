# Realsense_Infrared_Ball_Tracking
## Here is an Infrared-Balls Tracking project based on Intel-Realsense, you will get the 2D, 3D position of the balls.

### Attention!!!
Before you running the program, please make sure you have already connected the realsense, attached the visible light shielding sheet on two infrared cameras, blocked the laser dot matrix and placed diffuse infrared light source.

### Result
<img src="./detectResult.gif" width = "400" height = "250" alt="图片名称"/>

### Realsense example
<figure>
<img src="./realsense_diy.jpg" width = "200" height = "150" alt="图片名称"/>
<img src="./flashlight.jpg" width = "200" height = "150" alt="图片名称"/>
<img src="./balls.jpg" width = "200" height = "150" alt="图片名称"/>
</figure>

### Environments
```
conda create -n infrare_detection python=3.9
conda activate infrare_detection
pip install -r requirements.txt
```

### Run the Detection
```
python realsens_infrare_rgb.py
```

### Method
We use two infrared camera and bright spot detection to detect the infrared reflective ball.
Then we calculate the 2D and 3D coordinates of the ball through the camera's internal, external parameters and epipolar geometry.

### DIY
You can modify the line 24 in infraDetect.py with different threshold for detecting different size balls.

### Contact
```
ligaoqi02@gmail.com
```