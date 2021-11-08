#dumb script for ffmpeg concat

#ffmpeg call:
#   ffmpeg -f concat -i imageInput.txt -vsync vfr -pix_fmt yuv420p output.mp4

N_CHEESE = 4#number of cheese
INTRO_TIME = 2
FRAME_TIME = 1
OUTFILE_NAME = "imageInput.txt"


outstring = ""

outstring += "file 'title.jpg'\nduration {}\n".format(INTRO_TIME)

for i in range(N_CHEESE):
    outstring += "file 'text{}.jpg'\nduration{}\n".format(i + 1, FRAME_TIME)
    outstring += "file 'cheese{}.jpg'\nduration{}\n".format(i + 1, FRAME_TIME)

f = open(OUTFILE_NAME, "w")
f.write(outstring)
f.close()