#-*- coding: UTF-8 -*-
import time
from lib.utils import *
from lib.culrcscrapers.azlyrics import lyricsScraper as lyricsScraper_azlyrics
from lib.culrcscrapers.darklyrics import lyricsScraper as lyricsScraper_darklyrics
from lib.culrcscrapers.genius import lyricsScraper as lyricsScraper_genius
from lib.culrcscrapers.gomaudio import lyricsScraper as lyricsScraper_gomaudio
from lib.culrcscrapers.lyricscom import lyricsScraper as lyricsScraper_lyricscom
from lib.culrcscrapers.lyricsify import lyricsScraper as lyricsScraper_lyricsify
from lib.culrcscrapers.lyricsmode import lyricsScraper as lyricsScraper_lyricsmode
from lib.culrcscrapers.minilyrics import lyricsScraper as lyricsScraper_minilyrics
from lib.culrcscrapers.music163 import lyricsScraper as lyricsScraper_music163
from lib.culrcscrapers.musixmatch import lyricsScraper as lyricsScraper_musixmatch

FAILED = []

def test_scrapers():
    lyricssettings = {}
    lyricssettings['debug'] = ADDON.getSettingBool('log_enabled')
    lyricssettings['save_filename_format'] = ADDON.getSettingInt('save_filename_format')
    lyricssettings['save_lyrics_path'] = ADDON.getSettingString('save_lyrics_path')
    lyricssettings['save_subfolder'] = ADDON.getSettingBool('save_subfolder')
    lyricssettings['save_subfolder_path'] = ADDON.getSettingString('save_subfolder_path')

    dialog = xbmcgui.DialogProgress()
    TIMINGS = []

    # test alsong
    dialog.create(ADDONNAME, LANGUAGE(32163) % 'azlyrics')
    log('==================== azlyrics ====================', debug=True)
    song = Song(opt=lyricssettings)
    song.artist = 'La Dispute'
    song.title = 'Such Small Hands'
    st = time.time()
    lyrics = lyricsScraper_azlyrics.LyricsFetcher(settings=lyricssettings, debug=True).get_lyrics(song)
    ft = time.time()
    tt = ft - st
    TIMINGS.append(['azlyrics',tt])
    if lyrics:
        log(lyrics.lyrics, debug=True)
    else:
        FAILED.append('azlyrics')
        log('FAILED: azlyrics', debug=True)
    if dialog.iscanceled():
        return

    # test darklyrics
    dialog.update(11, LANGUAGE(32163) % 'darklyrics')
    log('==================== darklyrics ====================', debug=True)
    song = Song(opt=lyricssettings)
    song.artist = 'Neurosis'
    song.title = 'Lost'
    st = time.time()
    lyrics = lyricsScraper_darklyrics.LyricsFetcher(settings=lyricssettings, debug=True).get_lyrics(song)
    ft = time.time()
    tt = ft - st
    TIMINGS.append(['darklyrics',tt])
    if lyrics:
        log(lyrics.lyrics, debug=True)
    else:
        FAILED.append('darklyrics')
        log('FAILED: darklyrics', debug=True)
    if dialog.iscanceled():
        return

    # test genius
    dialog.update(22, LANGUAGE(32163) % 'genius')
    log('==================== genius ====================', debug=True)
    song = Song(opt=lyricssettings)
    song.artist = 'Maren Morris'
    song.title = 'My Church'
    st = time.time()
    lyrics = lyricsScraper_genius.LyricsFetcher(settings=lyricssettings, debug=True).get_lyrics(song)
    ft = time.time()
    tt = ft - st
    TIMINGS.append(['genius',tt])
    if lyrics:
        log(lyrics.lyrics, debug=True)
    else:
        FAILED.append('genius')
        log('FAILED: genius', debug=True)
    if dialog.iscanceled():
        return

    # test gomaudio
    dialog.update(33, LANGUAGE(32163) % 'gomaudio')
    log('==================== gomaudio ====================', debug=True)
    song = Song(opt=lyricssettings)
    song.artist = 'Lady Gaga'
    song.title = 'Just Dance'
    st = time.time()
    lyrics = lyricsScraper_gomaudio.LyricsFetcher(settings=lyricssettings, debug=True).get_lyrics(song, 'd106534632cb43306423acb351f8e6e9', '.mp3')
    ft = time.time()
    tt = ft - st
    TIMINGS.append(['gomaudio',tt])
    if lyrics:
        log(lyrics.lyrics, debug=True)
    else:
        FAILED.append('gomaudio')
        log('FAILED: gomaudio', debug=True)
    if dialog.iscanceled():
        return

    # test lyricscom
    dialog.update(44, LANGUAGE(32163) % 'lyricscom')
    log('==================== lyricscom ====================', debug=True)
    song = Song(opt=lyricssettings)
    song.artist = 'Blur'
    song.title = 'You\'re So Great'
    st = time.time()
    lyrics = lyricsScraper_lyricscom.LyricsFetcher(settings=lyricssettings, debug=True).get_lyrics(song)
    ft = time.time()
    tt = ft - st
    TIMINGS.append(['lyricscom',tt])
    if lyrics:
        log(lyrics.lyrics, debug=True)
    else:
        FAILED.append('lyricscom')
        log('FAILED: lyricscom', debug=True)
    if dialog.iscanceled():
        return

    # test lyricsify
    dialog.update(55, LANGUAGE(32163) % 'lyricsify')
    log('==================== lyricsify ====================', debug=True)
    song = Song(opt=lyricssettings)
    song.artist = 'Madonna'
    song.title = 'Crazy For You'
    st = time.time()
    lyrics = lyricsScraper_lyricsify.LyricsFetcher(settings=lyricssettings, debug=True).get_lyrics(song)
    ft = time.time()
    tt = ft - st
    TIMINGS.append(['lyricsify',tt])
    if lyrics:
        log(lyrics.lyrics, debug=True)
    else:
        FAILED.append('lyricsify')
        log('FAILED: lyricsify', debug=True)
    if dialog.iscanceled():
        return

    # test lyricsmode
    dialog.update(66, LANGUAGE(32163) % 'lyricsmode')
    log('==================== lyricsmode ====================', debug=True)
    song = Song(opt=lyricssettings)
    song.artist = 'Maren Morris'
    song.title = 'My Church'
    st = time.time()
    lyrics = lyricsScraper_lyricsmode.LyricsFetcher(settings=lyricssettings, debug=True).get_lyrics(song)
    ft = time.time()
    tt = ft - st
    TIMINGS.append(['lyricsmode',tt])
    if lyrics:
        log(lyrics.lyrics, debug=True)
    else:
        FAILED.append('lyricsmode')
        log('FAILED: lyricsmode', debug=True)
    if dialog.iscanceled():
        return


    # test minilyrics
    dialog.update(77, LANGUAGE(32163) % 'minilyrics')
    log('==================== minilyrics ====================', debug=True)
    song = Song(opt=lyricssettings)
    song.artist = 'Chicago'
    song.title = 'Stay The Night'
    st = time.time()
    lyrics = lyricsScraper_minilyrics.LyricsFetcher(settings=lyricssettings, debug=True).get_lyrics(song)
    ft = time.time()
    tt = ft - st
    TIMINGS.append(['minilyrics',tt])
    if lyrics:
        log(lyrics.lyrics, debug=True)
    else:
        FAILED.append('minilyrics')
        log('FAILED: minilyrics', debug=True)
    if dialog.iscanceled():
        return

    # test music163
    dialog.update(88, LANGUAGE(32163) % 'music163')
    log('==================== music163 ====================', debug=True)
    song = Song(opt=lyricssettings)
    song.artist = 'Chicago'
    song.title = 'Stay The Night'
    st = time.time()
    lyrics = lyricsScraper_music163.LyricsFetcher(settings=lyricssettings, debug=True).get_lyrics(song)
    ft = time.time()
    tt = ft - st
    TIMINGS.append(['music163',tt])
    if lyrics:
        log(lyrics.lyrics, debug=True)
    else:
        FAILED.append('music163')
        log('FAILED: music163', debug=True)
    if dialog.iscanceled():
        return

    # test musixmatch
    dialog.update(88, LANGUAGE(32163) % 'musixmatch')
    log('==================== musixmatch ====================', debug=True)
    song = Song(opt=lyricssettings)
    song.artist = 'Kate Bush'
    song.title = 'Wuthering Heights'
    st = time.time()
    lyrics = lyricsScraper_musixmatch.LyricsFetcher(settings=lyricssettings, debug=True).get_lyrics(song)
    ft = time.time()
    tt = ft - st
    TIMINGS.append(['musixmatch',tt])
    if lyrics:
        log(lyrics.lyrics, debug=True)
    else:
        FAILED.append('musixmatch')
        log('FAILED: musixmatch', debug=True)
    if dialog.iscanceled():
        return

    dialog.close()
    log('=======================================', debug=True)
    log('FAILED: %s' % str(FAILED), debug=True)
    log('=======================================', debug=True)
    for item in TIMINGS:
        log('%s - %i' % (item[0], item[1]), debug=True)
    log('=======================================', debug=True)
    if FAILED:
        dialog = xbmcgui.Dialog().ok(ADDONNAME, LANGUAGE(32165) % ' / '.join(FAILED))
    else:
        dialog = xbmcgui.Dialog().ok(ADDONNAME, LANGUAGE(32164))
