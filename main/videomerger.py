from moviepy.editor import VideoFileClip,concatenate_videoclips,CompositeVideoClip

#list to store all the frames
clips=[]
#appending each frame to the list 
for i in range(172):
    #path to the output frames that we want to merge
    p="output_frames/out_"+ str(i+1)+".mp4" 
    clips.append(VideoFileClip(p))
#taking first frame into c
c=clips[0]
for i in range(171):
    final_clip=concatenate_videoclips([c,clips[i+1]]) #attaching frame by frame
    c=final_clip                                      #taking attached frames and giving it to attach next frames
#writing the final video to your desired destination
final_clip.write_videofile("output/merged.mp4")
#written the output to output folder as merged.mp4
#after this add the audio by using any online software
