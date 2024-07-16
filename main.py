from ultralytics import YOLO
import os
import json
import cv2
import numpy as np
import av

def get_video_frames(model, video_path, output_path, json_path):

    # Open the video file
    container = av.open(video_path)
    stream = container.streams.video[0]
    fps = float(stream.average_rate)
    width = stream.width
    height = stream.height

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Initialize timestamp lists
    Pepsi_pts, CocaCola_pts = [], [] 

    for frame in container.decode(video=0):
        
        img = frame.to_image()  
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Run detection
        results = model(img)
        if results is not None and len(results) > 0:
            for box in results[0].boxes:

                # Extracting coordinates
                x1, y1, x2, y2 = box.xyxy[0].tolist() 
                cls = int(box.cls[0])

                # Get the size of the bounding box
                box_width = round(x2 - x1,2)
                box_height = round(y2 - y1,2)
                size = (box_width, box_height)

                # Calculate distance from the center of the frame
                box_center_x = x1 + box_width / 2
                box_center_y = y1 + box_height / 2
                frame_center_x = width / 2
                frame_center_y = height / 2
                distance_from_center = round(np.sqrt((box_center_x - frame_center_x) ** 2 + (box_center_y - frame_center_y) ** 2),2)

                # Get the timestamp of the frame
                timestamp = round(frame.time,2)  

                data_entry = {
                    "timestamp": f"{timestamp} s",
                    "size": {
                        "width": f"{size[0]} px",
                        "height": f"{size[1]} px"
                    },
                    "distance_from_center": f"{distance_from_center} px"
                }

                label = model.names[cls]

                if label == 'pepsi':
                    Pepsi_pts.append(data_entry)  
                if label == 'cocacola':
                    CocaCola_pts.append(data_entry)  

        # Draw bounding boxes and labels on the frame
        annotated_img = results[0].plot()

        # Write the frame with detections to the output video
        out.write(annotated_img)

    # Release everything if job is finished
    out.release()
    print("Video saved successfully!")

    # Save timestamps to JSON
    timestamps_data = {
        "Pepsi_pts": Pepsi_pts,
        "CocaCola_pts": CocaCola_pts
    }
    with open(json_path, 'w') as f:
        json.dump(timestamps_data, f, indent=4)

    print("Timestamps saved successfully!")

def output_video():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    model_path = os.path.join(script_dir, 'Model', 'best.pt')
    model = YOLO(model_path)

    video_path =  {video_path}  # Replace with the actual path
    
    output_path =  os.path.join(script_dir,'Output','DetectionVideo.mp4')
    json_path =  os.path.join(script_dir,'Output','DetectionsTimeStamps.json')
    get_video_frames(model, video_path, output_path, json_path)

if __name__ == "__main__":
    output_video()

