print('****************WELCOME TO r3dstrings Youtube Downloader**********************\n')
def main():
    from pytube import YouTube
    try:
        get_url = input('Enter the URL of the video : \n')
        youtube_url = YouTube(get_url)
        print('The video that you are trying to download is | ', (youtube_url.title) ,'| \n \n ')
        print('specify whether you want to download the video v or audio a \n')
        response_url = input('enter a or v : \n')
        if response_url == 'v':
            print('you are downloading a video of length ',
                (youtube_url.length), 'seconds. please wait \n')
            youtube_stream = youtube_url.streams.get_highest_resolution()
            youtube_stream.download()
            print('\n download complete \n')
            exit

        if response_url == 'a':
            print('you are downloading an audio of length \n ',
                (youtube_url.length), 'seconds. please wait. \n')
            youtube_stream = youtube_url.streams.get_audio_only()
            youtube_stream.download()
            print('download complete \n ')
            exit
        else:
            print('\n please either enter a or v \n')
            main()
    except:
        print("\n either the url provided is wrong or we couldn't find the file requested.try again \n")
        main()
main()

