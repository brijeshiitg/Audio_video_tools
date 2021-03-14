# Audio_video_tools
 
 "audio_video_tutorial.py" provides basic operations for videos.
 It contains five functions:

## 1. extract_image_sequence(video_file, image_sequence_path):
This function takes video file path (including video file name), 
converts it to temporal sequence of images, and saves it to "image_sequence_path" location.

## 2. frames_to_video(image_sequence_path, outputpath, fps):
This function takes temportal image sequence located at "image_seqence_path" and converts
and saves it to "outputpath" location. It also takes "fps" which is by default = 29.

## 3. clip_video(video_file, t1, t2, target_path, target_name):
This function takes the video file located at "video_file" path, from time (t1), to time (t2), 
the path to store output video clip ("target_path"), and name of target file "target_name".

## 4. merge_clips(clip1_path, clip2_path, merge_path, merge_file_name):
Input paths of video clips to be joined  ("clip1_path, clip2_path")
"merge_path" and "merge_file_name" are path to store merged file and name of that file, respectively.

## 5. extract_audio(video_file, audio_path, audio_name):
Takes path of video files "video_file" and sotres the audio at location "audio_path" with name "audio_name".

Go to main below the function and uncomment the call of specific function you want to use.
