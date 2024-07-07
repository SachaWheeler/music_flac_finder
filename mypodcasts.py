#! /usr/bin/env python3

import getpodcast

opt = getpodcast.options(
    date_from='2024-01-01',
    root_dir='/moshpit/podcast')

# get podcast feed url here
# https://www.labnol.org/podcast/

podcasts = {
        # "Ross_and_Carrie": "https://podcasts.apple.com/gb/podcast/oh-no-ross-and-carrie/id425328515",
    "ONRAC": "https://feeds.simplecast.com/ftB6Gihc",
    "HDTGM": "https://feeds.simplecast.com/Ao0C24M8",
    "Problem_squared": "https://anchor.fm/s/eb804d78/podcast/rss",
    "RobWords": "https://audioboom.com/channels/5128892.rss",
    #"SGU": "https://feed.theskepticsguide.org/feed/sgu"
}

getpodcast.getpodcast(podcasts, opt)
