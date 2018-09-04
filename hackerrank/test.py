import pandas as pd
import math

# Empty dictionary where the videos are stored as the key value
# and are associated to a number which is the times the video
# was viewed

global watched
watched = {}

def videoViewed(videoid):
    # Set the video viewed in the watched dict.

    # set the video to lower case
    videoid = videoid.lower()

    # If the video is in the dictionary it adds plus 1 to the visits
    # else, the video is added to the dictionary
    # O(1)
    if videoid in watched.keys():
        watched[videoid] += 1
    else:
        watched[videoid] = 1


def getRanking(videoid):
    lng = len(watched)

    # Search if valid video
    if videoid in watched.keys():
        rank = watched[videoid]
    else:
        return 0

    if lng == 1:
        return 1

    # Sort the data
    # O(N)
    ranking = pd.DataFrame(list(watched.items()), columns=['video_id', 'rank'])
    ranking = ranking.sort_values(by=['rank'], ascending=False)

    ranked = list(ranking['rank'])

    int_p = 0
    end_p = lng+1

    # Search in the list for the position of the video,
    # There could be repeated numbers of views but it takes the any of them
    # I don't think is a problem due to that more videos have the same popularity
    # but they're just in upper or lower indexes around the real value.

    # O(log N)
    while int_p <= end_p:

        mid_p = math.ceil((int_p+end_p))/2

        if ranked[mid_p] < rank:
            int_p = mid_p + 1
        elif ranked[mid_p] > rank:
            end_p = mid_p - 1
        else:
            return mid_p


def getTopVideos():
    lng = len(watched)

    # Sort the data
    # O(N)
    ranking = pd.DataFrame(list(watched.items()), columns=['video_id', 'rank'])
    ranking = ranking.sort_values('rank', ascending=False)

    # If the list of video is not large enough the value of top viewed changes
    if lng >= 10:
        videos = list(ranking['video_id'].iloc[:10])
    else:
        try:
            videos = list(ranking['video_id'].iloc[:lng])
        except:
            videos = ['']
    result = ['']

    # Nice way or printing the list
    # O(N)
    try:
        for video in range(len(videos)):
            result.append(str(video+1)+". "+videos[video])
    except:
        result = ['']

    return result
