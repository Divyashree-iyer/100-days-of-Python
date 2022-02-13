# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 13:14:51 2022

@author: divyashree
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime

#connect to spotify

def conn_2_spotify():
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth
    
    spotify_client_id = YOUR_CLIENT_ID
    spotify_client_secret = YOUR_CLIENT_SECRET
    
    oauth = SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=spotify_client_id, 
        client_secret=spotify_client_secret, 
        redirect_uri='http://example.com',
        show_dialog=True,
        cache_path="token.txt")
    
    sp = spotipy.Spotify(auth_manager=oauth)
    
    user_id = sp.current_user()["id"]
    song_uris=[]
    # find album by name
    for album in album_names:
        
        results = sp.search(q = "album:" + album, type = "album")
        try:
            # get the first album uri
            album_id = results['albums']['items'][0]['uri']
            
            # get album tracks
            tracks = sp.album_tracks(album_id, limit=5)
            
            for track in tracks['items']:
                song_uris.append(track['uri'])
        except :
            print(f"{album} doesn't exist in Spotify. Skipped.")    
    #create a spotify playlist
    playlist = sp.user_playlist_create(user=user_id, name=f"{year} Top songs", public=False)
    print(playlist)
    
    #Adding songs found into the new playlist
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
        
        


now = datetime.now()
cur_year= now.year

print(f'Year range - 1931 to {cur_year}')
year = int(input("Which year to you want to travel to? Enter in YYYY format: "))

#web scraping foe music
if year >=1931 and year < cur_year:
    res = requests.get('http://myswar.co/album/year/'+str(year))
    contents = res.text
    soup = BeautifulSoup(contents, 'html.parser')
    album_names = [album_tables.find(name = 'a').get('title') for album_tables in soup.select('.song_detail_display_table')]
    conn_2_spotify()
else:
    print("I am sorry but the time machine can't go back further. Try another year")












