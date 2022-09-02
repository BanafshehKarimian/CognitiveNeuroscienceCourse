#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.1),
    on March 07, 2022, at 23:00
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.1'
expName = 'HW1'  # from the Builder filename that created this script
expInfo = {'sbj': '810199252', 'hndns': 'r', 'eye': 'r', 'sex': 'female', 'age': '19', 'edu': '3'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['sbj'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='V:\\cognitive\\HW1\\HW1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='hsv',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "trial"
trialClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='سلام',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=0.0);

# Initialize components for Routine "Intro"
IntroClock = core.Clock()
IntroText = visual.TextStim(win=win, name='IntroText',
    text='در هر مرحله با توجه با کلید های گفته شده در توضیحات\nجنسیت تصویر نشان داده شده را از دید خودتان\nمشخص کنید\nدقت کنید که سرعت پاسخ دهی نیز در نتایج مهم خواهد بود\nبرای رد کردن هر بخش توضیحات کلید space را بزنید',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=0.0);
IntroKeyboard = keyboard.Keyboard()

# Initialize components for Routine "InsR"
InsRClock = core.Clock()
rightInst = visual.ImageStim(
    win=win,
    name='rightInst', 
    image='Supplementary Material/KbRight.jpg', mask=None, anchor='top-center',
    ori=90.0, pos=(0, 0), size=( 1 ,0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
rightInstKeyboard = keyboard.Keyboard()
rightInstText = visual.TextStim(win=win, name='rightInstText',
    text='دست راست خود را مانند شکل قرار دهید.\nO: خانم\nP: آقا',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);

# Initialize components for Routine "fixPoint"
fixPointClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon',
    size=(0.05, 0.05), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0902, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "right"
rightClock = core.Clock()
stimuliRight = visual.ImageStim(
    win=win,
    name='stimuliRight', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
rightK = keyboard.Keyboard()

# Initialize components for Routine "InsL"
InsLClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='Supplementary Material/KbLeft.jpg', mask=None, anchor='top-center',
    ori=90.0, pos=(0, 0), size=(1, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
leftInstKeyboard = keyboard.Keyboard()
leftInstText = visual.TextStim(win=win, name='leftInstText',
    text='دست چپ خود را مانند شکل قرار دهید.\nQ: خانم\nW: آقا',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);

# Initialize components for Routine "fixPoint"
fixPointClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon',
    size=(0.05, 0.05), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0902, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "left"
leftClock = core.Clock()
stimuliLeft = visual.ImageStim(
    win=win,
    name='stimuliLeft', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "InsR"
InsRClock = core.Clock()
rightInst = visual.ImageStim(
    win=win,
    name='rightInst', 
    image='Supplementary Material/KbRight.jpg', mask=None, anchor='top-center',
    ori=90.0, pos=(0, 0), size=( 1 ,0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
rightInstKeyboard = keyboard.Keyboard()
rightInstText = visual.TextStim(win=win, name='rightInstText',
    text='دست راست خود را مانند شکل قرار دهید.\nO: خانم\nP: آقا',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);

# Initialize components for Routine "fixPoint"
fixPointClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon',
    size=(0.05, 0.05), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0902, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "right"
rightClock = core.Clock()
stimuliRight = visual.ImageStim(
    win=win,
    name='stimuliRight', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
rightK = keyboard.Keyboard()

# Initialize components for Routine "InsR"
InsRClock = core.Clock()
rightInst = visual.ImageStim(
    win=win,
    name='rightInst', 
    image='Supplementary Material/KbRight.jpg', mask=None, anchor='top-center',
    ori=90.0, pos=(0, 0), size=( 1 ,0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
rightInstKeyboard = keyboard.Keyboard()
rightInstText = visual.TextStim(win=win, name='rightInstText',
    text='دست راست خود را مانند شکل قرار دهید.\nO: خانم\nP: آقا',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);

# Initialize components for Routine "fixPoint"
fixPointClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon',
    size=(0.05, 0.05), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0902, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "right"
rightClock = core.Clock()
stimuliRight = visual.ImageStim(
    win=win,
    name='stimuliRight', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
rightK = keyboard.Keyboard()

# Initialize components for Routine "InsL"
InsLClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='Supplementary Material/KbLeft.jpg', mask=None, anchor='top-center',
    ori=90.0, pos=(0, 0), size=(1, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
leftInstKeyboard = keyboard.Keyboard()
leftInstText = visual.TextStim(win=win, name='leftInstText',
    text='دست چپ خود را مانند شکل قرار دهید.\nQ: خانم\nW: آقا',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);

# Initialize components for Routine "fixPoint"
fixPointClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon',
    size=(0.05, 0.05), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0902, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "left"
leftClock = core.Clock()
stimuliLeft = visual.ImageStim(
    win=win,
    name='stimuliLeft', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "InsR"
InsRClock = core.Clock()
rightInst = visual.ImageStim(
    win=win,
    name='rightInst', 
    image='Supplementary Material/KbRight.jpg', mask=None, anchor='top-center',
    ori=90.0, pos=(0, 0), size=( 1 ,0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
rightInstKeyboard = keyboard.Keyboard()
rightInstText = visual.TextStim(win=win, name='rightInstText',
    text='دست راست خود را مانند شکل قرار دهید.\nO: خانم\nP: آقا',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);

# Initialize components for Routine "fixPoint"
fixPointClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon',
    size=(0.05, 0.05), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0902, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "right"
rightClock = core.Clock()
stimuliRight = visual.ImageStim(
    win=win,
    name='stimuliRight', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
rightK = keyboard.Keyboard()

# Initialize components for Routine "InsL"
InsLClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='Supplementary Material/KbLeft.jpg', mask=None, anchor='top-center',
    ori=90.0, pos=(0, 0), size=(1, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
leftInstKeyboard = keyboard.Keyboard()
leftInstText = visual.TextStim(win=win, name='leftInstText',
    text='دست چپ خود را مانند شکل قرار دهید.\nQ: خانم\nW: آقا',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);

# Initialize components for Routine "fixPoint"
fixPointClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon',
    size=(0.05, 0.05), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0902, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "left"
leftClock = core.Clock()
stimuliLeft = visual.ImageStim(
    win=win,
    name='stimuliLeft', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "InsL"
InsLClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='Supplementary Material/KbLeft.jpg', mask=None, anchor='top-center',
    ori=90.0, pos=(0, 0), size=(1, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
leftInstKeyboard = keyboard.Keyboard()
leftInstText = visual.TextStim(win=win, name='leftInstText',
    text='دست چپ خود را مانند شکل قرار دهید.\nQ: خانم\nW: آقا',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='Arabic',
    depth=-2.0);

# Initialize components for Routine "fixPoint"
fixPointClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon',
    size=(0.05, 0.05), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.0902, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "left"
leftClock = core.Clock()
stimuliLeft = visual.ImageStim(
    win=win,
    name='stimuliLeft', units='cm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [text]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# ------Prepare to start Routine "Intro"-------
continueRoutine = True
# update component parameters for each repeat
IntroKeyboard.keys = []
IntroKeyboard.rt = []
_IntroKeyboard_allKeys = []
# keep track of which components have finished
IntroComponents = [IntroText, IntroKeyboard]
for thisComponent in IntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Intro"-------
while continueRoutine:
    # get current time
    t = IntroClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *IntroText* updates
    if IntroText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IntroText.frameNStart = frameN  # exact frame index
        IntroText.tStart = t  # local t and not account for scr refresh
        IntroText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IntroText, 'tStartRefresh')  # time at next scr refresh
        IntroText.setAutoDraw(True)
    
    # *IntroKeyboard* updates
    waitOnFlip = False
    if IntroKeyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        IntroKeyboard.frameNStart = frameN  # exact frame index
        IntroKeyboard.tStart = t  # local t and not account for scr refresh
        IntroKeyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(IntroKeyboard, 'tStartRefresh')  # time at next scr refresh
        IntroKeyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(IntroKeyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(IntroKeyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if IntroKeyboard.status == STARTED and not waitOnFlip:
        theseKeys = IntroKeyboard.getKeys(keyList=['space'], waitRelease=False)
        _IntroKeyboard_allKeys.extend(theseKeys)
        if len(_IntroKeyboard_allKeys):
            IntroKeyboard.keys = _IntroKeyboard_allKeys[-1].name  # just the last key pressed
            IntroKeyboard.rt = _IntroKeyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro"-------
for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('IntroText.started', IntroText.tStartRefresh)
thisExp.addData('IntroText.stopped', IntroText.tStopRefresh)
# check responses
if IntroKeyboard.keys in ['', [], None]:  # No response was made
    IntroKeyboard.keys = None
thisExp.addData('IntroKeyboard.keys',IntroKeyboard.keys)
if IntroKeyboard.keys != None:  # we had a response
    thisExp.addData('IntroKeyboard.rt', IntroKeyboard.rt)
thisExp.addData('IntroKeyboard.started', IntroKeyboard.tStartRefresh)
thisExp.addData('IntroKeyboard.stopped', IntroKeyboard.tStopRefresh)
thisExp.nextEntry()
# the Routine "Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "InsR"-------
continueRoutine = True
# update component parameters for each repeat
rightInstKeyboard.keys = []
rightInstKeyboard.rt = []
_rightInstKeyboard_allKeys = []
# keep track of which components have finished
InsRComponents = [rightInst, rightInstKeyboard, rightInstText]
for thisComponent in InsRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InsRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InsR"-------
while continueRoutine:
    # get current time
    t = InsRClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InsRClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rightInst* updates
    if rightInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rightInst.frameNStart = frameN  # exact frame index
        rightInst.tStart = t  # local t and not account for scr refresh
        rightInst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rightInst, 'tStartRefresh')  # time at next scr refresh
        rightInst.setAutoDraw(True)
    
    # *rightInstKeyboard* updates
    waitOnFlip = False
    if rightInstKeyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rightInstKeyboard.frameNStart = frameN  # exact frame index
        rightInstKeyboard.tStart = t  # local t and not account for scr refresh
        rightInstKeyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rightInstKeyboard, 'tStartRefresh')  # time at next scr refresh
        rightInstKeyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(rightInstKeyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(rightInstKeyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if rightInstKeyboard.status == STARTED and not waitOnFlip:
        theseKeys = rightInstKeyboard.getKeys(keyList=['space'], waitRelease=False)
        _rightInstKeyboard_allKeys.extend(theseKeys)
        if len(_rightInstKeyboard_allKeys):
            rightInstKeyboard.keys = _rightInstKeyboard_allKeys[-1].name  # just the last key pressed
            rightInstKeyboard.rt = _rightInstKeyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *rightInstText* updates
    if rightInstText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rightInstText.frameNStart = frameN  # exact frame index
        rightInstText.tStart = t  # local t and not account for scr refresh
        rightInstText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rightInstText, 'tStartRefresh')  # time at next scr refresh
        rightInstText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InsRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InsR"-------
for thisComponent in InsRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rightInst.started', rightInst.tStartRefresh)
thisExp.addData('rightInst.stopped', rightInst.tStopRefresh)
# check responses
if rightInstKeyboard.keys in ['', [], None]:  # No response was made
    rightInstKeyboard.keys = None
thisExp.addData('rightInstKeyboard.keys',rightInstKeyboard.keys)
if rightInstKeyboard.keys != None:  # we had a response
    thisExp.addData('rightInstKeyboard.rt', rightInstKeyboard.rt)
thisExp.addData('rightInstKeyboard.started', rightInstKeyboard.tStartRefresh)
thisExp.addData('rightInstKeyboard.stopped', rightInstKeyboard.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('rightInstText.started', rightInstText.tStartRefresh)
thisExp.addData('rightInstText.stopped', rightInstText.tStopRefresh)
# the Routine "InsR" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loopright0 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('bmps.xlsx'),
    seed=None, name='loopright0')
thisExp.addLoop(loopright0)  # add the loop to the experiment
thisLoopright0 = loopright0.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoopright0.rgb)
if thisLoopright0 != None:
    for paramName in thisLoopright0:
        exec('{} = thisLoopright0[paramName]'.format(paramName))

for thisLoopright0 in loopright0:
    currentLoop = loopright0
    # abbreviate parameter names if possible (e.g. rgb = thisLoopright0.rgb)
    if thisLoopright0 != None:
        for paramName in thisLoopright0:
            exec('{} = thisLoopright0[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixPoint"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixPointComponents = [polygon]
    for thisComponent in fixPointComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixPointClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixPoint"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixPointClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixPointClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixPointComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixPoint"-------
    for thisComponent in fixPointComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loopright0.addData('polygon.started', polygon.tStartRefresh)
    loopright0.addData('polygon.stopped', polygon.tStopRefresh)
    
    # ------Prepare to start Routine "right"-------
    continueRoutine = True
    # update component parameters for each repeat
    stimuliRight.setPos(pos)
    stimuliRight.setSize(size)
    stimuliRight.setImage(stim)
    rightK.keys = []
    rightK.rt = []
    _rightK_allKeys = []
    # keep track of which components have finished
    rightComponents = [stimuliRight, rightK]
    for thisComponent in rightComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rightClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "right"-------
    while continueRoutine:
        # get current time
        t = rightClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rightClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuliRight* updates
        if stimuliRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimuliRight.frameNStart = frameN  # exact frame index
            stimuliRight.tStart = t  # local t and not account for scr refresh
            stimuliRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuliRight, 'tStartRefresh')  # time at next scr refresh
            stimuliRight.setAutoDraw(True)
        if stimuliRight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuliRight.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                stimuliRight.tStop = t  # not accounting for scr refresh
                stimuliRight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuliRight, 'tStopRefresh')  # time at next scr refresh
                stimuliRight.setAutoDraw(False)
        
        # *rightK* updates
        waitOnFlip = False
        if rightK.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightK.frameNStart = frameN  # exact frame index
            rightK.tStart = t  # local t and not account for scr refresh
            rightK.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightK, 'tStartRefresh')  # time at next scr refresh
            rightK.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rightK.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rightK.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rightK.status == STARTED and not waitOnFlip:
            theseKeys = rightK.getKeys(keyList=['p','o'], waitRelease=False)
            _rightK_allKeys.extend(theseKeys)
            if len(_rightK_allKeys):
                rightK.keys = _rightK_allKeys[-1].name  # just the last key pressed
                rightK.rt = _rightK_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rightComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "right"-------
    for thisComponent in rightComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loopright0.addData('stimuliRight.started', stimuliRight.tStartRefresh)
    loopright0.addData('stimuliRight.stopped', stimuliRight.tStopRefresh)
    # check responses
    if rightK.keys in ['', [], None]:  # No response was made
        rightK.keys = None
    loopright0.addData('rightK.keys',rightK.keys)
    if rightK.keys != None:  # we had a response
        loopright0.addData('rightK.rt', rightK.rt)
    loopright0.addData('rightK.started', rightK.tStartRefresh)
    loopright0.addData('rightK.stopped', rightK.tStopRefresh)
    # the Routine "right" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'loopright0'


# ------Prepare to start Routine "InsL"-------
continueRoutine = True
# update component parameters for each repeat
leftInstKeyboard.keys = []
leftInstKeyboard.rt = []
_leftInstKeyboard_allKeys = []
# keep track of which components have finished
InsLComponents = [image, leftInstKeyboard, leftInstText]
for thisComponent in InsLComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InsLClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InsL"-------
while continueRoutine:
    # get current time
    t = InsLClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InsLClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *leftInstKeyboard* updates
    waitOnFlip = False
    if leftInstKeyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        leftInstKeyboard.frameNStart = frameN  # exact frame index
        leftInstKeyboard.tStart = t  # local t and not account for scr refresh
        leftInstKeyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(leftInstKeyboard, 'tStartRefresh')  # time at next scr refresh
        leftInstKeyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(leftInstKeyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(leftInstKeyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if leftInstKeyboard.status == STARTED and not waitOnFlip:
        theseKeys = leftInstKeyboard.getKeys(keyList=['space'], waitRelease=False)
        _leftInstKeyboard_allKeys.extend(theseKeys)
        if len(_leftInstKeyboard_allKeys):
            leftInstKeyboard.keys = _leftInstKeyboard_allKeys[-1].name  # just the last key pressed
            leftInstKeyboard.rt = _leftInstKeyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *leftInstText* updates
    if leftInstText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        leftInstText.frameNStart = frameN  # exact frame index
        leftInstText.tStart = t  # local t and not account for scr refresh
        leftInstText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(leftInstText, 'tStartRefresh')  # time at next scr refresh
        leftInstText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InsLComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InsL"-------
for thisComponent in InsLComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# check responses
if leftInstKeyboard.keys in ['', [], None]:  # No response was made
    leftInstKeyboard.keys = None
thisExp.addData('leftInstKeyboard.keys',leftInstKeyboard.keys)
if leftInstKeyboard.keys != None:  # we had a response
    thisExp.addData('leftInstKeyboard.rt', leftInstKeyboard.rt)
thisExp.addData('leftInstKeyboard.started', leftInstKeyboard.tStartRefresh)
thisExp.addData('leftInstKeyboard.stopped', leftInstKeyboard.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('leftInstText.started', leftInstText.tStartRefresh)
thisExp.addData('leftInstText.stopped', leftInstText.tStopRefresh)
# the Routine "InsL" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loopleft0 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('bmps.xlsx'),
    seed=None, name='loopleft0')
thisExp.addLoop(loopleft0)  # add the loop to the experiment
thisLoopleft0 = loopleft0.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoopleft0.rgb)
if thisLoopleft0 != None:
    for paramName in thisLoopleft0:
        exec('{} = thisLoopleft0[paramName]'.format(paramName))

for thisLoopleft0 in loopleft0:
    currentLoop = loopleft0
    # abbreviate parameter names if possible (e.g. rgb = thisLoopleft0.rgb)
    if thisLoopleft0 != None:
        for paramName in thisLoopleft0:
            exec('{} = thisLoopleft0[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixPoint"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixPointComponents = [polygon]
    for thisComponent in fixPointComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixPointClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixPoint"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixPointClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixPointClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixPointComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixPoint"-------
    for thisComponent in fixPointComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loopleft0.addData('polygon.started', polygon.tStartRefresh)
    loopleft0.addData('polygon.stopped', polygon.tStopRefresh)
    
    # ------Prepare to start Routine "left"-------
    continueRoutine = True
    # update component parameters for each repeat
    stimuliLeft.setPos(pos)
    stimuliLeft.setSize(size)
    stimuliLeft.setImage(stim)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    leftComponents = [stimuliLeft, key_resp]
    for thisComponent in leftComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    leftClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "left"-------
    while continueRoutine:
        # get current time
        t = leftClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=leftClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuliLeft* updates
        if stimuliLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimuliLeft.frameNStart = frameN  # exact frame index
            stimuliLeft.tStart = t  # local t and not account for scr refresh
            stimuliLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuliLeft, 'tStartRefresh')  # time at next scr refresh
            stimuliLeft.setAutoDraw(True)
        if stimuliLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuliLeft.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                stimuliLeft.tStop = t  # not accounting for scr refresh
                stimuliLeft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuliLeft, 'tStopRefresh')  # time at next scr refresh
                stimuliLeft.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['q','w'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in leftComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "left"-------
    for thisComponent in leftComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loopleft0.addData('stimuliLeft.started', stimuliLeft.tStartRefresh)
    loopleft0.addData('stimuliLeft.stopped', stimuliLeft.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    loopleft0.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        loopleft0.addData('key_resp.rt', key_resp.rt)
    loopleft0.addData('key_resp.started', key_resp.tStartRefresh)
    loopleft0.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "left" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'loopleft0'


# ------Prepare to start Routine "InsR"-------
continueRoutine = True
# update component parameters for each repeat
rightInstKeyboard.keys = []
rightInstKeyboard.rt = []
_rightInstKeyboard_allKeys = []
# keep track of which components have finished
InsRComponents = [rightInst, rightInstKeyboard, rightInstText]
for thisComponent in InsRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InsRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InsR"-------
while continueRoutine:
    # get current time
    t = InsRClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InsRClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rightInst* updates
    if rightInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rightInst.frameNStart = frameN  # exact frame index
        rightInst.tStart = t  # local t and not account for scr refresh
        rightInst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rightInst, 'tStartRefresh')  # time at next scr refresh
        rightInst.setAutoDraw(True)
    
    # *rightInstKeyboard* updates
    waitOnFlip = False
    if rightInstKeyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rightInstKeyboard.frameNStart = frameN  # exact frame index
        rightInstKeyboard.tStart = t  # local t and not account for scr refresh
        rightInstKeyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rightInstKeyboard, 'tStartRefresh')  # time at next scr refresh
        rightInstKeyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(rightInstKeyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(rightInstKeyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if rightInstKeyboard.status == STARTED and not waitOnFlip:
        theseKeys = rightInstKeyboard.getKeys(keyList=['space'], waitRelease=False)
        _rightInstKeyboard_allKeys.extend(theseKeys)
        if len(_rightInstKeyboard_allKeys):
            rightInstKeyboard.keys = _rightInstKeyboard_allKeys[-1].name  # just the last key pressed
            rightInstKeyboard.rt = _rightInstKeyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *rightInstText* updates
    if rightInstText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rightInstText.frameNStart = frameN  # exact frame index
        rightInstText.tStart = t  # local t and not account for scr refresh
        rightInstText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rightInstText, 'tStartRefresh')  # time at next scr refresh
        rightInstText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InsRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InsR"-------
for thisComponent in InsRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rightInst.started', rightInst.tStartRefresh)
thisExp.addData('rightInst.stopped', rightInst.tStopRefresh)
# check responses
if rightInstKeyboard.keys in ['', [], None]:  # No response was made
    rightInstKeyboard.keys = None
thisExp.addData('rightInstKeyboard.keys',rightInstKeyboard.keys)
if rightInstKeyboard.keys != None:  # we had a response
    thisExp.addData('rightInstKeyboard.rt', rightInstKeyboard.rt)
thisExp.addData('rightInstKeyboard.started', rightInstKeyboard.tStartRefresh)
thisExp.addData('rightInstKeyboard.stopped', rightInstKeyboard.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('rightInstText.started', rightInstText.tStartRefresh)
thisExp.addData('rightInstText.stopped', rightInstText.tStopRefresh)
# the Routine "InsR" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loopRight = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('bmps.xlsx'),
    seed=None, name='loopRight')
thisExp.addLoop(loopRight)  # add the loop to the experiment
thisLoopRight = loopRight.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoopRight.rgb)
if thisLoopRight != None:
    for paramName in thisLoopRight:
        exec('{} = thisLoopRight[paramName]'.format(paramName))

for thisLoopRight in loopRight:
    currentLoop = loopRight
    # abbreviate parameter names if possible (e.g. rgb = thisLoopRight.rgb)
    if thisLoopRight != None:
        for paramName in thisLoopRight:
            exec('{} = thisLoopRight[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixPoint"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixPointComponents = [polygon]
    for thisComponent in fixPointComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixPointClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixPoint"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixPointClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixPointClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixPointComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixPoint"-------
    for thisComponent in fixPointComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loopRight.addData('polygon.started', polygon.tStartRefresh)
    loopRight.addData('polygon.stopped', polygon.tStopRefresh)
    
    # ------Prepare to start Routine "right"-------
    continueRoutine = True
    # update component parameters for each repeat
    stimuliRight.setPos(pos)
    stimuliRight.setSize(size)
    stimuliRight.setImage(stim)
    rightK.keys = []
    rightK.rt = []
    _rightK_allKeys = []
    # keep track of which components have finished
    rightComponents = [stimuliRight, rightK]
    for thisComponent in rightComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rightClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "right"-------
    while continueRoutine:
        # get current time
        t = rightClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rightClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuliRight* updates
        if stimuliRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimuliRight.frameNStart = frameN  # exact frame index
            stimuliRight.tStart = t  # local t and not account for scr refresh
            stimuliRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuliRight, 'tStartRefresh')  # time at next scr refresh
            stimuliRight.setAutoDraw(True)
        if stimuliRight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuliRight.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                stimuliRight.tStop = t  # not accounting for scr refresh
                stimuliRight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuliRight, 'tStopRefresh')  # time at next scr refresh
                stimuliRight.setAutoDraw(False)
        
        # *rightK* updates
        waitOnFlip = False
        if rightK.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightK.frameNStart = frameN  # exact frame index
            rightK.tStart = t  # local t and not account for scr refresh
            rightK.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightK, 'tStartRefresh')  # time at next scr refresh
            rightK.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rightK.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rightK.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rightK.status == STARTED and not waitOnFlip:
            theseKeys = rightK.getKeys(keyList=['p','o'], waitRelease=False)
            _rightK_allKeys.extend(theseKeys)
            if len(_rightK_allKeys):
                rightK.keys = _rightK_allKeys[-1].name  # just the last key pressed
                rightK.rt = _rightK_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rightComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "right"-------
    for thisComponent in rightComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loopRight.addData('stimuliRight.started', stimuliRight.tStartRefresh)
    loopRight.addData('stimuliRight.stopped', stimuliRight.tStopRefresh)
    # check responses
    if rightK.keys in ['', [], None]:  # No response was made
        rightK.keys = None
    loopRight.addData('rightK.keys',rightK.keys)
    if rightK.keys != None:  # we had a response
        loopRight.addData('rightK.rt', rightK.rt)
    loopRight.addData('rightK.started', rightK.tStartRefresh)
    loopRight.addData('rightK.stopped', rightK.tStopRefresh)
    # the Routine "right" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'loopRight'


# ------Prepare to start Routine "InsR"-------
continueRoutine = True
# update component parameters for each repeat
rightInstKeyboard.keys = []
rightInstKeyboard.rt = []
_rightInstKeyboard_allKeys = []
# keep track of which components have finished
InsRComponents = [rightInst, rightInstKeyboard, rightInstText]
for thisComponent in InsRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InsRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InsR"-------
while continueRoutine:
    # get current time
    t = InsRClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InsRClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rightInst* updates
    if rightInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rightInst.frameNStart = frameN  # exact frame index
        rightInst.tStart = t  # local t and not account for scr refresh
        rightInst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rightInst, 'tStartRefresh')  # time at next scr refresh
        rightInst.setAutoDraw(True)
    
    # *rightInstKeyboard* updates
    waitOnFlip = False
    if rightInstKeyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rightInstKeyboard.frameNStart = frameN  # exact frame index
        rightInstKeyboard.tStart = t  # local t and not account for scr refresh
        rightInstKeyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rightInstKeyboard, 'tStartRefresh')  # time at next scr refresh
        rightInstKeyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(rightInstKeyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(rightInstKeyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if rightInstKeyboard.status == STARTED and not waitOnFlip:
        theseKeys = rightInstKeyboard.getKeys(keyList=['space'], waitRelease=False)
        _rightInstKeyboard_allKeys.extend(theseKeys)
        if len(_rightInstKeyboard_allKeys):
            rightInstKeyboard.keys = _rightInstKeyboard_allKeys[-1].name  # just the last key pressed
            rightInstKeyboard.rt = _rightInstKeyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *rightInstText* updates
    if rightInstText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rightInstText.frameNStart = frameN  # exact frame index
        rightInstText.tStart = t  # local t and not account for scr refresh
        rightInstText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rightInstText, 'tStartRefresh')  # time at next scr refresh
        rightInstText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InsRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InsR"-------
for thisComponent in InsRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rightInst.started', rightInst.tStartRefresh)
thisExp.addData('rightInst.stopped', rightInst.tStopRefresh)
# check responses
if rightInstKeyboard.keys in ['', [], None]:  # No response was made
    rightInstKeyboard.keys = None
thisExp.addData('rightInstKeyboard.keys',rightInstKeyboard.keys)
if rightInstKeyboard.keys != None:  # we had a response
    thisExp.addData('rightInstKeyboard.rt', rightInstKeyboard.rt)
thisExp.addData('rightInstKeyboard.started', rightInstKeyboard.tStartRefresh)
thisExp.addData('rightInstKeyboard.stopped', rightInstKeyboard.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('rightInstText.started', rightInstText.tStartRefresh)
thisExp.addData('rightInstText.stopped', rightInstText.tStopRefresh)
# the Routine "InsR" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loopRight2 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('bmps.xlsx'),
    seed=None, name='loopRight2')
thisExp.addLoop(loopRight2)  # add the loop to the experiment
thisLoopRight2 = loopRight2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoopRight2.rgb)
if thisLoopRight2 != None:
    for paramName in thisLoopRight2:
        exec('{} = thisLoopRight2[paramName]'.format(paramName))

for thisLoopRight2 in loopRight2:
    currentLoop = loopRight2
    # abbreviate parameter names if possible (e.g. rgb = thisLoopRight2.rgb)
    if thisLoopRight2 != None:
        for paramName in thisLoopRight2:
            exec('{} = thisLoopRight2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixPoint"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixPointComponents = [polygon]
    for thisComponent in fixPointComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixPointClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixPoint"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixPointClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixPointClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixPointComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixPoint"-------
    for thisComponent in fixPointComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loopRight2.addData('polygon.started', polygon.tStartRefresh)
    loopRight2.addData('polygon.stopped', polygon.tStopRefresh)
    
    # ------Prepare to start Routine "right"-------
    continueRoutine = True
    # update component parameters for each repeat
    stimuliRight.setPos(pos)
    stimuliRight.setSize(size)
    stimuliRight.setImage(stim)
    rightK.keys = []
    rightK.rt = []
    _rightK_allKeys = []
    # keep track of which components have finished
    rightComponents = [stimuliRight, rightK]
    for thisComponent in rightComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rightClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "right"-------
    while continueRoutine:
        # get current time
        t = rightClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rightClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuliRight* updates
        if stimuliRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimuliRight.frameNStart = frameN  # exact frame index
            stimuliRight.tStart = t  # local t and not account for scr refresh
            stimuliRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuliRight, 'tStartRefresh')  # time at next scr refresh
            stimuliRight.setAutoDraw(True)
        if stimuliRight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuliRight.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                stimuliRight.tStop = t  # not accounting for scr refresh
                stimuliRight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuliRight, 'tStopRefresh')  # time at next scr refresh
                stimuliRight.setAutoDraw(False)
        
        # *rightK* updates
        waitOnFlip = False
        if rightK.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightK.frameNStart = frameN  # exact frame index
            rightK.tStart = t  # local t and not account for scr refresh
            rightK.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightK, 'tStartRefresh')  # time at next scr refresh
            rightK.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rightK.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rightK.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rightK.status == STARTED and not waitOnFlip:
            theseKeys = rightK.getKeys(keyList=['p','o'], waitRelease=False)
            _rightK_allKeys.extend(theseKeys)
            if len(_rightK_allKeys):
                rightK.keys = _rightK_allKeys[-1].name  # just the last key pressed
                rightK.rt = _rightK_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rightComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "right"-------
    for thisComponent in rightComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loopRight2.addData('stimuliRight.started', stimuliRight.tStartRefresh)
    loopRight2.addData('stimuliRight.stopped', stimuliRight.tStopRefresh)
    # check responses
    if rightK.keys in ['', [], None]:  # No response was made
        rightK.keys = None
    loopRight2.addData('rightK.keys',rightK.keys)
    if rightK.keys != None:  # we had a response
        loopRight2.addData('rightK.rt', rightK.rt)
    loopRight2.addData('rightK.started', rightK.tStartRefresh)
    loopRight2.addData('rightK.stopped', rightK.tStopRefresh)
    # the Routine "right" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'loopRight2'


# ------Prepare to start Routine "InsL"-------
continueRoutine = True
# update component parameters for each repeat
leftInstKeyboard.keys = []
leftInstKeyboard.rt = []
_leftInstKeyboard_allKeys = []
# keep track of which components have finished
InsLComponents = [image, leftInstKeyboard, leftInstText]
for thisComponent in InsLComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InsLClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InsL"-------
while continueRoutine:
    # get current time
    t = InsLClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InsLClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *leftInstKeyboard* updates
    waitOnFlip = False
    if leftInstKeyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        leftInstKeyboard.frameNStart = frameN  # exact frame index
        leftInstKeyboard.tStart = t  # local t and not account for scr refresh
        leftInstKeyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(leftInstKeyboard, 'tStartRefresh')  # time at next scr refresh
        leftInstKeyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(leftInstKeyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(leftInstKeyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if leftInstKeyboard.status == STARTED and not waitOnFlip:
        theseKeys = leftInstKeyboard.getKeys(keyList=['space'], waitRelease=False)
        _leftInstKeyboard_allKeys.extend(theseKeys)
        if len(_leftInstKeyboard_allKeys):
            leftInstKeyboard.keys = _leftInstKeyboard_allKeys[-1].name  # just the last key pressed
            leftInstKeyboard.rt = _leftInstKeyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *leftInstText* updates
    if leftInstText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        leftInstText.frameNStart = frameN  # exact frame index
        leftInstText.tStart = t  # local t and not account for scr refresh
        leftInstText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(leftInstText, 'tStartRefresh')  # time at next scr refresh
        leftInstText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InsLComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InsL"-------
for thisComponent in InsLComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# check responses
if leftInstKeyboard.keys in ['', [], None]:  # No response was made
    leftInstKeyboard.keys = None
thisExp.addData('leftInstKeyboard.keys',leftInstKeyboard.keys)
if leftInstKeyboard.keys != None:  # we had a response
    thisExp.addData('leftInstKeyboard.rt', leftInstKeyboard.rt)
thisExp.addData('leftInstKeyboard.started', leftInstKeyboard.tStartRefresh)
thisExp.addData('leftInstKeyboard.stopped', leftInstKeyboard.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('leftInstText.started', leftInstText.tStartRefresh)
thisExp.addData('leftInstText.stopped', leftInstText.tStopRefresh)
# the Routine "InsL" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loopLeft = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('bmps.xlsx'),
    seed=None, name='loopLeft')
thisExp.addLoop(loopLeft)  # add the loop to the experiment
thisLoopLeft = loopLeft.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoopLeft.rgb)
if thisLoopLeft != None:
    for paramName in thisLoopLeft:
        exec('{} = thisLoopLeft[paramName]'.format(paramName))

for thisLoopLeft in loopLeft:
    currentLoop = loopLeft
    # abbreviate parameter names if possible (e.g. rgb = thisLoopLeft.rgb)
    if thisLoopLeft != None:
        for paramName in thisLoopLeft:
            exec('{} = thisLoopLeft[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixPoint"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixPointComponents = [polygon]
    for thisComponent in fixPointComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixPointClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixPoint"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixPointClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixPointClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixPointComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixPoint"-------
    for thisComponent in fixPointComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loopLeft.addData('polygon.started', polygon.tStartRefresh)
    loopLeft.addData('polygon.stopped', polygon.tStopRefresh)
    
    # ------Prepare to start Routine "left"-------
    continueRoutine = True
    # update component parameters for each repeat
    stimuliLeft.setPos(pos)
    stimuliLeft.setSize(size)
    stimuliLeft.setImage(stim)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    leftComponents = [stimuliLeft, key_resp]
    for thisComponent in leftComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    leftClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "left"-------
    while continueRoutine:
        # get current time
        t = leftClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=leftClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuliLeft* updates
        if stimuliLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimuliLeft.frameNStart = frameN  # exact frame index
            stimuliLeft.tStart = t  # local t and not account for scr refresh
            stimuliLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuliLeft, 'tStartRefresh')  # time at next scr refresh
            stimuliLeft.setAutoDraw(True)
        if stimuliLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuliLeft.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                stimuliLeft.tStop = t  # not accounting for scr refresh
                stimuliLeft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuliLeft, 'tStopRefresh')  # time at next scr refresh
                stimuliLeft.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['q','w'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in leftComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "left"-------
    for thisComponent in leftComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loopLeft.addData('stimuliLeft.started', stimuliLeft.tStartRefresh)
    loopLeft.addData('stimuliLeft.stopped', stimuliLeft.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    loopLeft.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        loopLeft.addData('key_resp.rt', key_resp.rt)
    loopLeft.addData('key_resp.started', key_resp.tStartRefresh)
    loopLeft.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "left" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'loopLeft'


# ------Prepare to start Routine "InsR"-------
continueRoutine = True
# update component parameters for each repeat
rightInstKeyboard.keys = []
rightInstKeyboard.rt = []
_rightInstKeyboard_allKeys = []
# keep track of which components have finished
InsRComponents = [rightInst, rightInstKeyboard, rightInstText]
for thisComponent in InsRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InsRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InsR"-------
while continueRoutine:
    # get current time
    t = InsRClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InsRClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rightInst* updates
    if rightInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rightInst.frameNStart = frameN  # exact frame index
        rightInst.tStart = t  # local t and not account for scr refresh
        rightInst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rightInst, 'tStartRefresh')  # time at next scr refresh
        rightInst.setAutoDraw(True)
    
    # *rightInstKeyboard* updates
    waitOnFlip = False
    if rightInstKeyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rightInstKeyboard.frameNStart = frameN  # exact frame index
        rightInstKeyboard.tStart = t  # local t and not account for scr refresh
        rightInstKeyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rightInstKeyboard, 'tStartRefresh')  # time at next scr refresh
        rightInstKeyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(rightInstKeyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(rightInstKeyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if rightInstKeyboard.status == STARTED and not waitOnFlip:
        theseKeys = rightInstKeyboard.getKeys(keyList=['space'], waitRelease=False)
        _rightInstKeyboard_allKeys.extend(theseKeys)
        if len(_rightInstKeyboard_allKeys):
            rightInstKeyboard.keys = _rightInstKeyboard_allKeys[-1].name  # just the last key pressed
            rightInstKeyboard.rt = _rightInstKeyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *rightInstText* updates
    if rightInstText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rightInstText.frameNStart = frameN  # exact frame index
        rightInstText.tStart = t  # local t and not account for scr refresh
        rightInstText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rightInstText, 'tStartRefresh')  # time at next scr refresh
        rightInstText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InsRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InsR"-------
for thisComponent in InsRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rightInst.started', rightInst.tStartRefresh)
thisExp.addData('rightInst.stopped', rightInst.tStopRefresh)
# check responses
if rightInstKeyboard.keys in ['', [], None]:  # No response was made
    rightInstKeyboard.keys = None
thisExp.addData('rightInstKeyboard.keys',rightInstKeyboard.keys)
if rightInstKeyboard.keys != None:  # we had a response
    thisExp.addData('rightInstKeyboard.rt', rightInstKeyboard.rt)
thisExp.addData('rightInstKeyboard.started', rightInstKeyboard.tStartRefresh)
thisExp.addData('rightInstKeyboard.stopped', rightInstKeyboard.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('rightInstText.started', rightInstText.tStartRefresh)
thisExp.addData('rightInstText.stopped', rightInstText.tStopRefresh)
# the Routine "InsR" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loopRight3 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('bmps.xlsx'),
    seed=None, name='loopRight3')
thisExp.addLoop(loopRight3)  # add the loop to the experiment
thisLoopRight3 = loopRight3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoopRight3.rgb)
if thisLoopRight3 != None:
    for paramName in thisLoopRight3:
        exec('{} = thisLoopRight3[paramName]'.format(paramName))

for thisLoopRight3 in loopRight3:
    currentLoop = loopRight3
    # abbreviate parameter names if possible (e.g. rgb = thisLoopRight3.rgb)
    if thisLoopRight3 != None:
        for paramName in thisLoopRight3:
            exec('{} = thisLoopRight3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixPoint"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixPointComponents = [polygon]
    for thisComponent in fixPointComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixPointClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixPoint"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixPointClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixPointClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixPointComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixPoint"-------
    for thisComponent in fixPointComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loopRight3.addData('polygon.started', polygon.tStartRefresh)
    loopRight3.addData('polygon.stopped', polygon.tStopRefresh)
    
    # ------Prepare to start Routine "right"-------
    continueRoutine = True
    # update component parameters for each repeat
    stimuliRight.setPos(pos)
    stimuliRight.setSize(size)
    stimuliRight.setImage(stim)
    rightK.keys = []
    rightK.rt = []
    _rightK_allKeys = []
    # keep track of which components have finished
    rightComponents = [stimuliRight, rightK]
    for thisComponent in rightComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rightClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "right"-------
    while continueRoutine:
        # get current time
        t = rightClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rightClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuliRight* updates
        if stimuliRight.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimuliRight.frameNStart = frameN  # exact frame index
            stimuliRight.tStart = t  # local t and not account for scr refresh
            stimuliRight.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuliRight, 'tStartRefresh')  # time at next scr refresh
            stimuliRight.setAutoDraw(True)
        if stimuliRight.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuliRight.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                stimuliRight.tStop = t  # not accounting for scr refresh
                stimuliRight.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuliRight, 'tStopRefresh')  # time at next scr refresh
                stimuliRight.setAutoDraw(False)
        
        # *rightK* updates
        waitOnFlip = False
        if rightK.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rightK.frameNStart = frameN  # exact frame index
            rightK.tStart = t  # local t and not account for scr refresh
            rightK.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rightK, 'tStartRefresh')  # time at next scr refresh
            rightK.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rightK.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rightK.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rightK.status == STARTED and not waitOnFlip:
            theseKeys = rightK.getKeys(keyList=['p','o'], waitRelease=False)
            _rightK_allKeys.extend(theseKeys)
            if len(_rightK_allKeys):
                rightK.keys = _rightK_allKeys[-1].name  # just the last key pressed
                rightK.rt = _rightK_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rightComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "right"-------
    for thisComponent in rightComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loopRight3.addData('stimuliRight.started', stimuliRight.tStartRefresh)
    loopRight3.addData('stimuliRight.stopped', stimuliRight.tStopRefresh)
    # check responses
    if rightK.keys in ['', [], None]:  # No response was made
        rightK.keys = None
    loopRight3.addData('rightK.keys',rightK.keys)
    if rightK.keys != None:  # we had a response
        loopRight3.addData('rightK.rt', rightK.rt)
    loopRight3.addData('rightK.started', rightK.tStartRefresh)
    loopRight3.addData('rightK.stopped', rightK.tStopRefresh)
    # the Routine "right" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'loopRight3'


# ------Prepare to start Routine "InsL"-------
continueRoutine = True
# update component parameters for each repeat
leftInstKeyboard.keys = []
leftInstKeyboard.rt = []
_leftInstKeyboard_allKeys = []
# keep track of which components have finished
InsLComponents = [image, leftInstKeyboard, leftInstText]
for thisComponent in InsLComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InsLClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InsL"-------
while continueRoutine:
    # get current time
    t = InsLClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InsLClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *leftInstKeyboard* updates
    waitOnFlip = False
    if leftInstKeyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        leftInstKeyboard.frameNStart = frameN  # exact frame index
        leftInstKeyboard.tStart = t  # local t and not account for scr refresh
        leftInstKeyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(leftInstKeyboard, 'tStartRefresh')  # time at next scr refresh
        leftInstKeyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(leftInstKeyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(leftInstKeyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if leftInstKeyboard.status == STARTED and not waitOnFlip:
        theseKeys = leftInstKeyboard.getKeys(keyList=['space'], waitRelease=False)
        _leftInstKeyboard_allKeys.extend(theseKeys)
        if len(_leftInstKeyboard_allKeys):
            leftInstKeyboard.keys = _leftInstKeyboard_allKeys[-1].name  # just the last key pressed
            leftInstKeyboard.rt = _leftInstKeyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *leftInstText* updates
    if leftInstText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        leftInstText.frameNStart = frameN  # exact frame index
        leftInstText.tStart = t  # local t and not account for scr refresh
        leftInstText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(leftInstText, 'tStartRefresh')  # time at next scr refresh
        leftInstText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InsLComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InsL"-------
for thisComponent in InsLComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# check responses
if leftInstKeyboard.keys in ['', [], None]:  # No response was made
    leftInstKeyboard.keys = None
thisExp.addData('leftInstKeyboard.keys',leftInstKeyboard.keys)
if leftInstKeyboard.keys != None:  # we had a response
    thisExp.addData('leftInstKeyboard.rt', leftInstKeyboard.rt)
thisExp.addData('leftInstKeyboard.started', leftInstKeyboard.tStartRefresh)
thisExp.addData('leftInstKeyboard.stopped', leftInstKeyboard.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('leftInstText.started', leftInstText.tStartRefresh)
thisExp.addData('leftInstText.stopped', leftInstText.tStopRefresh)
# the Routine "InsL" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loopLeft2 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('bmps.xlsx'),
    seed=None, name='loopLeft2')
thisExp.addLoop(loopLeft2)  # add the loop to the experiment
thisLoopLeft2 = loopLeft2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoopLeft2.rgb)
if thisLoopLeft2 != None:
    for paramName in thisLoopLeft2:
        exec('{} = thisLoopLeft2[paramName]'.format(paramName))

for thisLoopLeft2 in loopLeft2:
    currentLoop = loopLeft2
    # abbreviate parameter names if possible (e.g. rgb = thisLoopLeft2.rgb)
    if thisLoopLeft2 != None:
        for paramName in thisLoopLeft2:
            exec('{} = thisLoopLeft2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixPoint"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixPointComponents = [polygon]
    for thisComponent in fixPointComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixPointClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixPoint"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixPointClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixPointClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixPointComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixPoint"-------
    for thisComponent in fixPointComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loopLeft2.addData('polygon.started', polygon.tStartRefresh)
    loopLeft2.addData('polygon.stopped', polygon.tStopRefresh)
    
    # ------Prepare to start Routine "left"-------
    continueRoutine = True
    # update component parameters for each repeat
    stimuliLeft.setPos(pos)
    stimuliLeft.setSize(size)
    stimuliLeft.setImage(stim)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    leftComponents = [stimuliLeft, key_resp]
    for thisComponent in leftComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    leftClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "left"-------
    while continueRoutine:
        # get current time
        t = leftClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=leftClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuliLeft* updates
        if stimuliLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimuliLeft.frameNStart = frameN  # exact frame index
            stimuliLeft.tStart = t  # local t and not account for scr refresh
            stimuliLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuliLeft, 'tStartRefresh')  # time at next scr refresh
            stimuliLeft.setAutoDraw(True)
        if stimuliLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuliLeft.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                stimuliLeft.tStop = t  # not accounting for scr refresh
                stimuliLeft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuliLeft, 'tStopRefresh')  # time at next scr refresh
                stimuliLeft.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['q','w'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in leftComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "left"-------
    for thisComponent in leftComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loopLeft2.addData('stimuliLeft.started', stimuliLeft.tStartRefresh)
    loopLeft2.addData('stimuliLeft.stopped', stimuliLeft.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    loopLeft2.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        loopLeft2.addData('key_resp.rt', key_resp.rt)
    loopLeft2.addData('key_resp.started', key_resp.tStartRefresh)
    loopLeft2.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "left" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'loopLeft2'


# ------Prepare to start Routine "InsL"-------
continueRoutine = True
# update component parameters for each repeat
leftInstKeyboard.keys = []
leftInstKeyboard.rt = []
_leftInstKeyboard_allKeys = []
# keep track of which components have finished
InsLComponents = [image, leftInstKeyboard, leftInstText]
for thisComponent in InsLComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InsLClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "InsL"-------
while continueRoutine:
    # get current time
    t = InsLClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InsLClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *leftInstKeyboard* updates
    waitOnFlip = False
    if leftInstKeyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        leftInstKeyboard.frameNStart = frameN  # exact frame index
        leftInstKeyboard.tStart = t  # local t and not account for scr refresh
        leftInstKeyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(leftInstKeyboard, 'tStartRefresh')  # time at next scr refresh
        leftInstKeyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(leftInstKeyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(leftInstKeyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if leftInstKeyboard.status == STARTED and not waitOnFlip:
        theseKeys = leftInstKeyboard.getKeys(keyList=['space'], waitRelease=False)
        _leftInstKeyboard_allKeys.extend(theseKeys)
        if len(_leftInstKeyboard_allKeys):
            leftInstKeyboard.keys = _leftInstKeyboard_allKeys[-1].name  # just the last key pressed
            leftInstKeyboard.rt = _leftInstKeyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *leftInstText* updates
    if leftInstText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        leftInstText.frameNStart = frameN  # exact frame index
        leftInstText.tStart = t  # local t and not account for scr refresh
        leftInstText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(leftInstText, 'tStartRefresh')  # time at next scr refresh
        leftInstText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InsLComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "InsL"-------
for thisComponent in InsLComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# check responses
if leftInstKeyboard.keys in ['', [], None]:  # No response was made
    leftInstKeyboard.keys = None
thisExp.addData('leftInstKeyboard.keys',leftInstKeyboard.keys)
if leftInstKeyboard.keys != None:  # we had a response
    thisExp.addData('leftInstKeyboard.rt', leftInstKeyboard.rt)
thisExp.addData('leftInstKeyboard.started', leftInstKeyboard.tStartRefresh)
thisExp.addData('leftInstKeyboard.stopped', leftInstKeyboard.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('leftInstText.started', leftInstText.tStartRefresh)
thisExp.addData('leftInstText.stopped', leftInstText.tStopRefresh)
# the Routine "InsL" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loopLeft3 = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('bmps.xlsx'),
    seed=None, name='loopLeft3')
thisExp.addLoop(loopLeft3)  # add the loop to the experiment
thisLoopLeft3 = loopLeft3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoopLeft3.rgb)
if thisLoopLeft3 != None:
    for paramName in thisLoopLeft3:
        exec('{} = thisLoopLeft3[paramName]'.format(paramName))

for thisLoopLeft3 in loopLeft3:
    currentLoop = loopLeft3
    # abbreviate parameter names if possible (e.g. rgb = thisLoopLeft3.rgb)
    if thisLoopLeft3 != None:
        for paramName in thisLoopLeft3:
            exec('{} = thisLoopLeft3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixPoint"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixPointComponents = [polygon]
    for thisComponent in fixPointComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixPointClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixPoint"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixPointClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixPointClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixPointComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixPoint"-------
    for thisComponent in fixPointComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loopLeft3.addData('polygon.started', polygon.tStartRefresh)
    loopLeft3.addData('polygon.stopped', polygon.tStopRefresh)
    
    # ------Prepare to start Routine "left"-------
    continueRoutine = True
    # update component parameters for each repeat
    stimuliLeft.setPos(pos)
    stimuliLeft.setSize(size)
    stimuliLeft.setImage(stim)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    leftComponents = [stimuliLeft, key_resp]
    for thisComponent in leftComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    leftClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "left"-------
    while continueRoutine:
        # get current time
        t = leftClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=leftClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuliLeft* updates
        if stimuliLeft.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stimuliLeft.frameNStart = frameN  # exact frame index
            stimuliLeft.tStart = t  # local t and not account for scr refresh
            stimuliLeft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuliLeft, 'tStartRefresh')  # time at next scr refresh
            stimuliLeft.setAutoDraw(True)
        if stimuliLeft.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stimuliLeft.tStartRefresh + 0.05-frameTolerance:
                # keep track of stop time/frame for later
                stimuliLeft.tStop = t  # not accounting for scr refresh
                stimuliLeft.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stimuliLeft, 'tStopRefresh')  # time at next scr refresh
                stimuliLeft.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['q','w'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in leftComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "left"-------
    for thisComponent in leftComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loopLeft3.addData('stimuliLeft.started', stimuliLeft.tStartRefresh)
    loopLeft3.addData('stimuliLeft.stopped', stimuliLeft.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    loopLeft3.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        loopLeft3.addData('key_resp.rt', key_resp.rt)
    loopLeft3.addData('key_resp.started', key_resp.tStartRefresh)
    loopLeft3.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "left" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'loopLeft3'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
