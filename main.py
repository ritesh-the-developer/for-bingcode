import yt_dlp

def downloadYtVideo(link):
    yt = yt_dlp.YoutubeDL()
    prog_VideoList_res_with_link = []
    prog_videoList = yt.extract_info(link, download=False)['formats']
    prog_videoList = sorted(prog_videoList, key=lambda x: x.get('filesize', 0) if x.get('filesize', 0) is not None else 0, reverse=True)
    for video in prog_videoList:
        if video['acodec'] != 'none' and video['vcodec'] != 'none':
            current_res = video['resolution']
            vid_size = str(video.get('filesize', 'N/A')/1000000) + ' Mb' if video.get('filesize', 0) is not None else 'N/A'
            vidUrl = video['url']
            vid_format = video['ext']
            prog_VideoList_res_with_link.append((current_res, vidUrl, vid_size, vid_format))
    if len(prog_VideoList_res_with_link) == 0:
        prog_VideoList_res_with_link.append(('N/A', 'N/A', 'N/A', 'N/A'))
    return prog_VideoList_res_with_link

def downloadYtOnlyVideo(link):
    yt = yt_dlp.YoutubeDL()
    nonProg_VideoList_res_with_link  = []
    nonProg_videoList = yt.extract_info(link, download=False)['formats']
    nonProg_videoList = sorted(nonProg_videoList, key=lambda x: x.get('filesize', 0) if x.get('filesize', 0) is not None else 0, reverse=True)
    for video in nonProg_videoList:
        if video['acodec'] == 'none' and video['vcodec'] != 'none':
            current_res = video['resolution']
            vid_size = str(video.get('filesize', 'N/A')/1000000) + ' Mb' if video.get('filesize', 0) is not None else 'N/A'
            vidUrl = video['url']
            vid_format = video['ext']
            nonProg_VideoList_res_with_link.append((current_res, vidUrl, vid_size, vid_format))
    if len(nonProg_VideoList_res_with_link) == 0:
        nonProg_VideoList_res_with_link.append(('N/A', 'N/A', 'N/A', 'N/A'))
    return nonProg_VideoList_res_with_link

def downloadYtAudio(link):
    yt = yt_dlp.YoutubeDL()
    audio_VideoList_res_with_link  = []
    audio_videoList = yt.extract_info(link, download=False)['formats']
    audio_videoList = sorted(audio_videoList, key=lambda x: x.get('filesize', 0) if x.get('filesize', 0) is not None else 0, reverse=True)
    for video in audio_videoList:
        if video['acodec'] != 'none' and video['vcodec'] == 'none':
            current_res = video['abr'] + ' kbps'
            vid_size = str(video.get('filesize', 'N/A')/1000000) + ' Mb' if video.get('filesize', 0) is not None else 'N/A'
            vidUrl = video['url']
            vid_format = video['ext']
            audio_VideoList_res_with_link.append((current_res, vidUrl, vid_size, vid_format))
    if len(audio_VideoList_res_with_link) == 0:
        audio_VideoList_res_with_link.append(('N/A', 'N/A', 'N/A', 'N/A'))
    return audio_VideoList_res_with_link
