import os
import datetime
#Joan Bosco Olives Florit NIA: 217056
path = 'big_buck_bunny_1080p_stereo.ogg'

def cut_video(path):
    n = input("Please enter nº of seconds to want cut this video ")
    n=int(n)#cast to int
    end_v = str(datetime.timedelta(seconds=n))#seconds to HH:MM:SS
    #-ss indicates de initial time for cut video, -t indicate the final
    os.system('ffmpeg -i ' + path + ' -ss 00:00:00 -t ' + end_v + ' -c:v copy -c:a copy output_cutted.ogg')

def histogram_yuv(path):
    os.system('ffmpeg -i '+path+' -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay" output_histogram.ogg'.format(path))
    #if don't work, please comment before line and descomment the next one (depend of S.O.)
    #os.system('ffplay -i '+path+' -vf split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay')


def resize_video(path):
    n = input("Choose resize format: \n 1.- 720p\n 2.- 480p\n 3.- 360x240\n 4.- 160x120\n 5.- Return to Menu\n")
    n = int(n)
    match n:
        case 1:
            print("Choosed 720p format")
            #-1 indicate to keep scale
            os.system('ffmpeg -i '+path+' -filter:v scale=720:-1 -c:a copy 720p.ogg')

        case 2:
            print("Choosed 480p format")
            os.system('ffmpeg -i '+path+' -filter:v scale=480:-1 -c:a copy 480p.ogg')

        case 3:
            print("Choosed 360x240 format")
            os.system('ffmpeg -i '+path+' -s 360x240 -c:a copy 360x240p.ogg')
            
        case 4:
            print("Choosed 160x120 format")
            os.system('ffmpeg -i '+path+' -s 160x120 -c:a copy 160x120.ogg')
        case 5:
            print("...Returning to Menu")
            return
        case _:
            print("You are introduced different input, please read")
            #if introduced different int input, re-call the function
            resize_video(path)

#for 2 next functions: -ac # indicates the number of channels
def stereo2mono(path):
    os.system('ffmpeg -i '+path+'  -c:v copy -ac 1 output_mono.ogg')

def mono2stereo(path):
    os.system('ffmpeg -i '+path+'  -c:v copy -ac 2 output_stereo.ogg')


def main():
    while True:
        print('---Start cutting video, and after you can use the rest of the functionalities.---\n'
            '---(This is because the video operations its better to used with small video...)---\n')
        n = input("1.- Cut video\n2.- Histogram\n3.- Resize Video\n4.- Stereo to Mono\n5.- Mono to Stereo\n6.- Exit\n")
        n = int(n)
        #menu with case's
        match n: #match function only works in python 3.10 or superior
            case 1:
                print("Cut Video Choosed")
                cut_video(path)

            case 2:
                print("Histogram Choosed")
                histogram_yuv(path = 'output_cutted.ogg')

            case 3:
                print("Resize Video Choosed")
                resize_video(path = 'output_cutted.ogg')
                
            case 4:
                print("Stereo to Mono Choosed")
                stereo2mono(path = 'output_cutted.ogg')
            case 5:
                print("Mono to Stereo Choosed")
                mono2stereo(path = 'output_cutted.ogg')
            case 6:
                print("Exit")
                return
            case _:
                print("You are introduced an invalid input, choose [1, 2, 3, 4, 5 or 6]")
                main()


if __name__ == "__main__":
    main()

