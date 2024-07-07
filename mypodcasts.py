#! /usr/bin/env python3

import getpodcast

opt = getpodcast.options(
    date_from='2024-01-01',
    root_dir='./podcast')

podcasts = {
        # "Ross_and_Carrie": "https://podcasts.apple.com/gb/podcast/oh-no-ross-and-carrie/id425328515",
    "SGU": "https://feed.theskepticsguide.org/feed/sgu"
}

getpodcast.getpodcast(podcasts, opt)
