# Logo Detector

The machine learning model implemented in this project is based on the YOLOv8 architecture, optimized for object detection tasks. It utilizes deep convolutional neural networks to efficiently and accurately detect and localize objects within images or video frames. The model is trained on a dataset containing annotated images of Pepsi and Coca-Cola logos, enabling it to identify and track these logos. Key features include robust detection performance, high-speed processing, and integration with OpenCV for video manipulation and annotation.

## Clone

- Clone the Repository

    ```bash
    git clone git@github.com:Manan21st/LogoDetector.git
    ```

## Installation

###  Effectively configure and run this YOLOv8-based logo detection project. 


- Install Dependencies

    Ensure that you have python and pip installed. 
    It is recommended to set up a virtual environment. 
    ```bash
    python -m venv <name>
    ```
    ```bash
    .env\Scripts\activate
    ```
    ```bash
    pip install -r requirements.txt
    ```

    This will install all the required dependencies to run this model.

    
## Configure Paths 

To run this project you will need to setup just one path. 

The path to the video you want to run this project on.

Located on line 95 of the file "main.py".

Every other path is already been set using relative path handling. 


<img width="398" alt="image" src="https://github.com/user-attachments/assets/8693ea77-5b58-4fc6-9b77-6184e31d5aa2">


## Running Model

To run the model, run the following command

```bash
  python .\main.py
```


## Example Output

After doing all the steps listed above. You will get 2 files in the
_*Output*_ folder.

One is a JSON file containing the time stamp of each logo along with their respective height, width and distance from center of the frame in pixels.
The other is the video.


<img width="194" alt="image" src="https://github.com/user-attachments/assets/23e047d2-a557-4242-84b7-4c4b052dfeaa">


https://github.com/user-attachments/assets/57ac19ca-3368-48d1-a0ae-2f8aa2b8b2e1

<img width="381" alt="image" src="https://github.com/user-attachments/assets/04a1a31b-d9df-4dcc-8ecb-29a3601133c2">


## Acknowledgements

 - [Ultralytics/YoloV8](https://github.com/ultralytics/ultralytics)
 - [Pepsi Data](https://universe.roboflow.com/detectionanas/pepsi-logo-detection/dataset/1)
 - [CocaCola Data](https://universe.roboflow.com/hawkeg/cocacola-puhys/dataset/3)
 - [Example video](https://www.youtube.com/shorts/i2s1b_Usatw)



