import cv2
import face_recognition

#importing video file
video =cv2.VideoCapture("video/cod_trailer.mp4")

#frame count of the video
length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

#recognize faces and encode them
img_alex=face_recognition.load_image_file("samples/alex.png")
enc_alex=face_recognition.face_encodings(img_alex)[0]

img_badguy=face_recognition.load_image_file("samples/badguy.png")
enc_badguy=face_recognition.face_encodings(img_badguy)[0]

img_farah=face_recognition.load_image_file("samples/farah.png")
enc_farah=face_recognition.face_encodings(img_farah)[0]

img_laswell=face_recognition.load_image_file("samples/laswell.png")
enc_laswell=face_recognition.face_encodings(img_laswell)[0]

img_captain=face_recognition.load_image_file("samples/price.png")
enc_captain=face_recognition.face_encodings(img_captain)[0]

#encoded faces list
enc_faces=[enc_alex,enc_badguy,enc_farah,enc_laswell,enc_captain]


face_points=[]
face_enc=[]
count=0 #frame count

while True:
    check,frame=video.read() #getting frame from video
    count=count+1           #incrementing frame count

    if not check:
        break
    c_frame=frame[:,:, ::-1]
    #getting location of the face
    face_points=face_recognition.face_locations(c_frame,model="cnn")
    face_enc=face_recognition.face_encodings(c_frame,face_points)

    facial_names=[]
    for enc in face_enc:
        #comparing faces with our known encoded faces
        match_face=face_recognition.compare_faces(enc_faces,enc,tolerance=0.60)

        name=""
        if match_face[0]:
            name="Alex"
        if match_face[1]:
            name="Bad Guy"
        if match_face[2]:
            name="Farah"
        if match_face[3]:
            name="Laswell"
        if match_face[4]:
            name="Captain Price"

        facial_names.append(name)

    for (top,right,bottom,left),name in zip(face_points,facial_names):
        #draw rectangle around the face
        cv2.rectangle(frame,(left,top),(right,bottom),(255,0,0),2) #draw rectangle around the face
        #drawing a filled rectangle to use as a background for text
        cv2.rectangle(frame,(left,bottom-25),(right,bottom),(255,0,0),cv2.FILLED)
        #selecting the font
        font=cv2.FONT_HERSHEY_SIMPLEX
        #writing the names
        cv2.putText(frame,name,(left+8,bottom-4),font,1,(0,0,0),2)
    
    cc=int(video.get(cv2.CAP_PROP_FOURCC))
    fps=int(video.get(cv2.CAP_PROP_FPS))
    frame_width=int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height=int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    #writing the frame after face recognition using abovee details
    output=cv2.VideoWriter("out_{}.mp4".format(count),cc,fps,(frame_width,frame_height))
    print("writing {}/{}".format(count,length))
    output.write(frame)

video.release()
output.release()
cv2.destroyAllWindows()

'''
now you have the frames,merge them by any software or
use videomerger.py to merge the frames
I have also attached the output frames in output_frames
'''
