#! /usr/bin/env python3

import getpodcast

# https://pypi.org/project/getpodcast/
opt = getpodcast.options(
    date_from='2024-05-01',
    root_dir='/moshpit/podcast')

# get podcast feed url here
# https://www.labnol.org/podcast/

podcasts = {
        # "Ross_and_Carrie": "https://podcasts.apple.com/gb/podcast/oh-no-ross-and-carrie/id425328515",
    "ONRAC": "https://feeds.simplecast.com/ftB6Gihc",
    "HDTGM": "https://feeds.simplecast.com/Ao0C24M8",
    "Problem_squared": "https://anchor.fm/s/eb804d78/podcast/rss",
    "RobWords": "https://audioboom.com/channels/5128892.rss",
    "Threedom": "https://www.omnycontent.com/d/playlist/796469f9-ea34-46a2-8776-ad0f015d6beb/977368a8-ac88-4f62-9ef7-b1100150df3e/69a2a921-5b42-4bdb-a5a5-b1100150df68/podcast.rss",
    "Unspooled": "https://feeds.simplecast.com/WEtQeHM9",
    "Smartless": "https://rss.art19.com/smartless",
    #"SGU": "https://feed.theskepticsguide.org/feed/sgu"
}

getpodcast.getpodcast(podcasts, opt)
