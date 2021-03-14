# audio_video_tutorial
import cv2
import os
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, concatenate_videoclips


video_file = 'msh_video.mp4'
image_sequence_path = 'image_sequences/'
audio_path = 'audio_file/'
clips_path = 'clips/'
merge_path = 'merged_video/'
video_output_path='./'

# ============ Extract image sequence from a video ================
def extract_image_sequence(video_file, image_sequence_path):
	vidcap = cv2.VideoCapture(video_file)

	if not os.path.exists(image_sequence_path):
		os.makedirs(image_sequence_path)

	i = 0
	while(vidcap.isOpened()):
		frameId = vidcap.get(1) #current frame
		ret, frame = vidcap.read()
		if ret != True:
			break
		filename = image_sequence_path+str(int(i))+'.jpg'
		i+=1
		cv2.imwrite(filename, frame)

	vidcap.release()
	print("Done!")
	cv2.destroyAllWindows()

# =================== Make video from image sequences =============
def frames_to_video(image_sequence_path,outputpath,fps):
   image_array = []
   files = [f for f in os.listdir(image_sequence_path) if os.path.isfile(os.path.join(image_sequence_path, f))]
   files.sort(key = lambda x: int(x.split(".")[0]))
   # files.sort()
   # print(files)
   for i in range(len(files)):
       img = cv2.imread(os.path.join(image_sequence_path, files[i]))
       size =  (img.shape[1],img.shape[0])
       img = cv2.resize(img,size)
       image_array.append(img)
   fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
   out = cv2.VideoWriter(outputpath,fourcc, fps, size)
   for i in range(len(image_array)):
       out.write(image_array[i])
   out.release()
   print("Done!")

# ===================== Clip Video ================================

# clip from 1sec to 3 sec
def clip_video(video_file, t1, t2, target_path, target_name):
	# from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
	if not os.path.exists(target_path):
		os.makedirs(target_path)
	ffmpeg_extract_subclip(video_file, t1, t2, targetname=target_path+target_name)
	print("Done!")


# =================== Merge video clips ============================

def merge_clips(clip1_path, clip2_path, merge_path, merge_fie_name): # you can extend till clip n
	# from moviepy.editor import VideoFileClip, concatenate_videoclips
	if not os.path.exists(merge_path):
		os.makedirs(merge_path)
	clip1 = VideoFileClip(clip1_path)
	clip2 = VideoFileClip(clip2_path)
	# you can extend till clip n
	# Merge clips
	final_clip = concatenate_videoclips([clip1, clip2])
	# Save merged clip
	final_clip.write_videofile(merge_path+merge_fie_name)
	print("Done!")

# =========== Extract Audio from Video ============================

def extract_audio(video_file, audio_path, audio_name):
	# from moviepy.editor import *
	clip = VideoFileClip(video_file)
	# extract audio
	audioclip = clip.audio
	# save audio to (.mp3)
	audioclip.write_audiofile(audio_path+audio_name)
	print("Done!")


if __name__ == '__main__':

	## ======= calling extraction image seqence function: ========
	extract_image_sequence(video_file, image_sequence_path)

	## ======== calling frames_to_video ==========================
	frames_to_video(image_sequence_path, video_output_path, 29)

	## ======== calling clip video: ==============================
	# clip_video(video_file, 1, 3, clips_path, 'clip1.mp4')
	# clip_video(video_file, 3, 5, clips_path, 'clip2.mp4')

	## ======== calling merge_clip: ==============================
	# merge_clips(clips_path+'clip1.mp4', clips_path+'clip2.mp4', merge_path, 'output_video.mp4')

	## ======== calling extract_audio ============================
	# extract_audio(video_file, audio_path, 'output.mp3')












