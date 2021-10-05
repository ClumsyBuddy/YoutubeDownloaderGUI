import youtube_dl as yt
import PySimpleGUI as sg


global AudioSwitch
AudioSwitch = False

sg.theme('DarkAmber')    # Keep things interesting for your users

def Download(Link):
    if AudioSwitch:
        ydl = yt.YoutubeDL({'format':'bestaudio', 'audio-format': 'm4a'})
        print("Audio Only")
    else:
        ydl = yt.YoutubeDL({})
        print("Audio and Video")
    with ydl:
        try:
            result = ydl.extract_info(
                Link,
                download=True # We just want to extract the info
            )
        except:
            print("Video does not exist")

layout = [[sg.Checkbox("Audio", key="Audio", enable_events=True), sg.Button("Download", key="DL"), sg.Input("", key="Input")]]      

window = sg.Window('Youtube Downloader', layout)      

while True:                             # The Event Loop
    event, values = window.read() 
    #print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Exit':
        break      
    if event == "DL":
        Download(values["Input"])
    if event == "Audio":
        AudioSwitch = values["Audio"]
window.close()






