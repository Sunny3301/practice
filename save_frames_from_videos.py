# sample runs to check how the different codes work...


import os
import cv2

def extract_frames(video_path, num_frames, output_folder):
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if total_frames < num_frames:
        print(f"Skipping {video_path}: Insufficient frames ({total_frames})")
        return

    frame_indices = [int((total_frames - 1) * i / (num_frames - 1)) for i in range(num_frames)]
    frame_count = 0

    for index in frame_indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, index)
        ret, frame = cap.read()
        if ret:
            frame_count += 1
            frame_filename = f'{os.path.splitext(os.path.basename(video_path))[0]}_frame_{frame_count}.jpg'
            output_path = os.path.join(output_folder, frame_filename)
            cv2.imwrite(output_path, frame)

    cap.release()

def process_videos(source_folder, destination_folder, num_frames_per_video):
    video_files = [file for file in os.listdir(source_folder) if file.endswith(".mp4")]

    for video_file in video_files:
        video_path = os.path.join(source_folder, video_file)
        output_folder = os.path.join(destination_folder, os.path.splitext(video_file)[0])
        os.makedirs(output_folder, exist_ok=True)
        extract_frames(video_path, num_frames_per_video, output_folder)

# Example usage
input_folder_path = "D:/video_quality_assessment/video_references/all/blocked"
output_folder_path = "D:/video_quality_assessment/video_references/all/blocked/images"
num_frames_per_video = 15

process_videos(input_folder_path, output_folder_path, num_frames_per_video)
