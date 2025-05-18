# CribNet: Enhancing Infant Safety in Cribs through Vision-based Hazard Detection

## Introduction
[原仓库](https://github.com/ostadabbas/CribNet)    </br>

## Intro

本仓库的毯子遮挡检测逻辑与目录结构与原仓库有优化。

运行毯子遮挡检测(occlusion-detection.py):
```
python Code/occlusion-detection.py <输入图片路径> <输入图片keypoints路径> <输出路径（默认./output）>
```
部分测试用例的输入输出在input/和output/文件夹中。


(为了看起来官方点防止老师检查我留下了原仓库的引用和致谢)

## Citation

If you use our code or models in your research, please cite with:

```
Zhu S, Mathew A, Hatamimajoumerd E, Wan M, Ostadabbas S. CribNet: Enhancing Infant Safety in Cribs through Vision-based Hazard Detection. IEEE International Conference on Automatic Face and Gesture Recognition (FG), 2024
```

## Acknowledgements

This project makes use of several open-source software and frameworks. We extend our gratitude to the developers and contributors of these projects:

- **FIDIP**: For the "Invariant Representation Learning for Infant Pose Estimation with Small Data". This work has been instrumental in advancing infant pose estimation research. [GitHub Repository](https://github.com/ostadabbas/Infant-Pose-Estimation)

- **YOLACT**: A real-time instance segmentation tool that has significantly contributed to the efficiency and accuracy of our object detection tasks. [GitHub Repository](https://github.com/dbolya/yolact)

- **YOLOv8**: For providing a state-of-the-art approach to object detection that is both fast and accurate, facilitating rapid development and testing. [Ultralytics GitHub Repository](https://github.com/ultralytics/ultralytics)

- **Detectron2**: Developed by Facebook AI Research, this framework has been crucial in our segmentation and object detection efforts, thanks to its flexibility and powerful modeling capabilities. [GitHub Repository](https://github.com/facebookresearch/detectron2)

- **Roboflow**: Dwyer, B., Nelson, J., Hansen, T., et. al. (2024). For Roboflow (Version 1.0) [Software], which has significantly streamlined our computer vision workflows. Available from [Roboflow](https://roboflow.com).

Each of these tools has played a vital role in the success of our project, and we are immensely thankful for the community's efforts in developing and maintaining them.


## License 
* This code is for non-commertial purpose only. 
* For further inquiry please contact: Augmented Cognition Lab at Northeastern University: http://www.northeastern.edu/ostadabbas/ 




