import sys, os

# 转换成mp3
for fname in sys.argv[1:]:
        fname = fname.replace("(","\(").replace(")","\)")
        os.system("ffmpeg -i " + fname + " -acodec mp3 " + fname[:-3] + "mp3")

# 缝合所有mp3为一
os.system('mp3wrap total.mp3 data/*.mp3')