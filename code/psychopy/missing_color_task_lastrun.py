#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on June 08, 2026, at 13:48
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
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
psychopyVersion = '2023.1.0'
expName = 'MCT'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\paper\\OneDrive\\Desktop\\PsychoPy\\masters_imagery\\missing_color_task_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
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

# --- Initialize components for Routine "CC_instr" ---
instr_text = visual.TextStim(win=win, name='instr_text',
    text='Вам будет показаны 2 последовательности цветных квадратов, сделанных по аналогии друг другу. Они будут появляться друг за другом, сначала полная, потом — с одним пропущенным, черным, квадратом.\n \nВам нужно представить недостающий цвет согласно последовательности и выбрать тот квадрат из представленных двух вариантов, который соответствует представленному цвету.\nВыбор нужного квадрата производится клавишами "←" и "→".\n\nСначала будет тренировочный этап с обратной связью, чтобы вы научились. Будет дано 8 задач.\n\nЧтобы начать тренировку, нажмите ПРОБЕЛ.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instr_resp = keyboard.Keyboard()

# --- Initialize components for Routine "blank" ---
fix = visual.ShapeStim(
    win=win, name='fix', vertices='cross',
    size=(0.08, 0.08),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "CC_trial" ---
clr1examp = visual.Rect(
    win=win, name='clr1examp',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.3375, 0.075), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
clr2examp = visual.Rect(
    win=win, name='clr2examp',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.1125, 0.075), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
clr3examp = visual.Rect(
    win=win, name='clr3examp',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.1125, 0.075), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
clr4examp = visual.Rect(
    win=win, name='clr4examp',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.3375, 0.075), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
clr1trial = visual.Rect(
    win=win, name='clr1trial',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.3375, -0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
clr2trail = visual.Rect(
    win=win, name='clr2trail',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.1125, -0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
clr3trail = visual.Rect(
    win=win, name='clr3trail',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.1125, -0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
clr4trail = visual.Rect(
    win=win, name='clr4trail',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.3375, -0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
key_skip = keyboard.Keyboard()
MASKclr1tr = visual.Rect(
    win=win, name='MASKclr1tr',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.3375, -0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
MASKclr2tr = visual.Rect(
    win=win, name='MASKclr2tr',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.1125, -0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-10.0, interpolate=True)
MASKclr3tr = visual.Rect(
    win=win, name='MASKclr3tr',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.1125, -0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-11.0, interpolate=True)
MASKclr4tr = visual.Rect(
    win=win, name='MASKclr4tr',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.3375, -0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-12.0, interpolate=True)

# --- Initialize components for Routine "blank" ---
fix = visual.ShapeStim(
    win=win, name='fix', vertices='cross',
    size=(0.08, 0.08),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "CC_trainAnsw" ---
l_point_2 = visual.Rect(
    win=win, name='l_point_2',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.2, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
r_point_2 = visual.Rect(
    win=win, name='r_point_2',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.2, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
CC_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "FB" ---
# Run 'Begin Experiment' code from loop_stop
msg='empty!'#if this comes up we forgot to update the msg!
FB_txt = visual.TextStim(win=win, name='FB_txt',
    text='',
    font='Open Sans',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
FB_clr = visual.Rect(
    win=win, name='FB_clr',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)

# --- Initialize components for Routine "CC_instr2" ---
instr2_text = visual.TextStim(win=win, name='instr2_text',
    text='Отлично! Теперь все по-настоящему, без обратной связи. Пожалуйста, не отвлекайтесь, сосредоточьтесь на задачах.\n\nЕсли вы готовы начать основной этап, нажмите ПРОБЕЛ.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instr2_resp = keyboard.Keyboard()

# --- Initialize components for Routine "CC_trial" ---
clr1examp = visual.Rect(
    win=win, name='clr1examp',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.3375, 0.075), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
clr2examp = visual.Rect(
    win=win, name='clr2examp',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.1125, 0.075), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
clr3examp = visual.Rect(
    win=win, name='clr3examp',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.1125, 0.075), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
clr4examp = visual.Rect(
    win=win, name='clr4examp',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.3375, 0.075), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
clr1trial = visual.Rect(
    win=win, name='clr1trial',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.3375, -0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
clr2trail = visual.Rect(
    win=win, name='clr2trail',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.1125, -0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
clr3trail = visual.Rect(
    win=win, name='clr3trail',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.1125, -0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
clr4trail = visual.Rect(
    win=win, name='clr4trail',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.3375, -0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
key_skip = keyboard.Keyboard()
MASKclr1tr = visual.Rect(
    win=win, name='MASKclr1tr',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.3375, -0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-9.0, interpolate=True)
MASKclr2tr = visual.Rect(
    win=win, name='MASKclr2tr',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.1125, -0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-10.0, interpolate=True)
MASKclr3tr = visual.Rect(
    win=win, name='MASKclr3tr',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.1125, -0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-11.0, interpolate=True)
MASKclr4tr = visual.Rect(
    win=win, name='MASKclr4tr',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.3375, -0.1), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-12.0, interpolate=True)

# --- Initialize components for Routine "blank" ---
fix = visual.ShapeStim(
    win=win, name='fix', vertices='cross',
    size=(0.08, 0.08),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "CC_answer" ---
l_point = visual.Rect(
    win=win, name='l_point',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(-0.2, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
r_point = visual.Rect(
    win=win, name='r_point',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=0.0, pos=(0.2, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
CC_resp = keyboard.Keyboard()

# --- Initialize components for Routine "blank" ---
fix = visual.ShapeStim(
    win=win, name='fix', vertices='cross',
    size=(0.08, 0.08),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "finish" ---
finish_txt = visual.TextStim(win=win, name='finish_txt',
    text='Это мучение закончилось!\nПодождите, когда эксперимент закроется.\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "CC_instr" ---
continueRoutine = True
# update component parameters for each repeat
instr_resp.keys = []
instr_resp.rt = []
_instr_resp_allKeys = []
# keep track of which components have finished
CC_instrComponents = [instr_text, instr_resp]
for thisComponent in CC_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "CC_instr" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_text* updates
    
    # if instr_text is starting this frame...
    if instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_text.frameNStart = frameN  # exact frame index
        instr_text.tStart = t  # local t and not account for scr refresh
        instr_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_text, 'tStartRefresh')  # time at next scr refresh
        # update status
        instr_text.status = STARTED
        instr_text.setAutoDraw(True)
    
    # if instr_text is active this frame...
    if instr_text.status == STARTED:
        # update params
        pass
    
    # *instr_resp* updates
    waitOnFlip = False
    
    # if instr_resp is starting this frame...
    if instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_resp.frameNStart = frameN  # exact frame index
        instr_resp.tStart = t  # local t and not account for scr refresh
        instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
        # update status
        instr_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_resp.status == STARTED and not waitOnFlip:
        theseKeys = instr_resp.getKeys(keyList=['space'], waitRelease=False)
        _instr_resp_allKeys.extend(theseKeys)
        if len(_instr_resp_allKeys):
            instr_resp.keys = _instr_resp_allKeys[-1].name  # just the last key pressed
            instr_resp.rt = _instr_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CC_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "CC_instr" ---
for thisComponent in CC_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "CC_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
training = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('CC_easylowhard_generalcond.xlsx'),
    seed=None, name='training')
thisExp.addLoop(training)  # add the loop to the experiment
thisTraining = training.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
if thisTraining != None:
    for paramName in thisTraining:
        exec('{} = thisTraining[paramName]'.format(paramName))

for thisTraining in training:
    currentLoop = training
    # abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
    if thisTraining != None:
        for paramName in thisTraining:
            exec('{} = thisTraining[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "blank" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [fix]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.8:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        
        # if fix is starting this frame...
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            # update status
            fix.status = STARTED
            fix.setAutoDraw(True)
        
        # if fix is active this frame...
        if fix.status == STARTED:
            # update params
            pass
        
        # if fix is stopping this frame...
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                # update status
                fix.status = FINISHED
                fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank" ---
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.800000)
    
    # --- Prepare to start Routine "CC_trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    clr1examp.setFillColor(clr1p1)
    clr2examp.setFillColor(clr2p1)
    clr3examp.setFillColor(clr3p1)
    clr4examp.setFillColor(clr4p1)
    clr1trial.setFillColor(clr1p2)
    clr2trail.setFillColor(clr2p2)
    clr3trail.setFillColor(clr3p2)
    clr4trail.setFillColor(clr4p2)
    key_skip.keys = []
    key_skip.rt = []
    _key_skip_allKeys = []
    MASKclr1tr.setFillColor('black')
    MASKclr2tr.setFillColor('black')
    MASKclr3tr.setFillColor('black')
    MASKclr4tr.setFillColor('black')
    # keep track of which components have finished
    CC_trialComponents = [clr1examp, clr2examp, clr3examp, clr4examp, clr1trial, clr2trail, clr3trail, clr4trail, key_skip, MASKclr1tr, MASKclr2tr, MASKclr3tr, MASKclr4tr]
    for thisComponent in CC_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "CC_trial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *clr1examp* updates
        
        # if clr1examp is starting this frame...
        if clr1examp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clr1examp.frameNStart = frameN  # exact frame index
            clr1examp.tStart = t  # local t and not account for scr refresh
            clr1examp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clr1examp, 'tStartRefresh')  # time at next scr refresh
            # update status
            clr1examp.status = STARTED
            clr1examp.setAutoDraw(True)
        
        # if clr1examp is active this frame...
        if clr1examp.status == STARTED:
            # update params
            pass
        
        # if clr1examp is stopping this frame...
        if clr1examp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clr1examp.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                clr1examp.tStop = t  # not accounting for scr refresh
                clr1examp.frameNStop = frameN  # exact frame index
                # update status
                clr1examp.status = FINISHED
                clr1examp.setAutoDraw(False)
        
        # *clr2examp* updates
        
        # if clr2examp is starting this frame...
        if clr2examp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clr2examp.frameNStart = frameN  # exact frame index
            clr2examp.tStart = t  # local t and not account for scr refresh
            clr2examp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clr2examp, 'tStartRefresh')  # time at next scr refresh
            # update status
            clr2examp.status = STARTED
            clr2examp.setAutoDraw(True)
        
        # if clr2examp is active this frame...
        if clr2examp.status == STARTED:
            # update params
            pass
        
        # if clr2examp is stopping this frame...
        if clr2examp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clr2examp.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                clr2examp.tStop = t  # not accounting for scr refresh
                clr2examp.frameNStop = frameN  # exact frame index
                # update status
                clr2examp.status = FINISHED
                clr2examp.setAutoDraw(False)
        
        # *clr3examp* updates
        
        # if clr3examp is starting this frame...
        if clr3examp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clr3examp.frameNStart = frameN  # exact frame index
            clr3examp.tStart = t  # local t and not account for scr refresh
            clr3examp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clr3examp, 'tStartRefresh')  # time at next scr refresh
            # update status
            clr3examp.status = STARTED
            clr3examp.setAutoDraw(True)
        
        # if clr3examp is active this frame...
        if clr3examp.status == STARTED:
            # update params
            pass
        
        # if clr3examp is stopping this frame...
        if clr3examp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clr3examp.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                clr3examp.tStop = t  # not accounting for scr refresh
                clr3examp.frameNStop = frameN  # exact frame index
                # update status
                clr3examp.status = FINISHED
                clr3examp.setAutoDraw(False)
        
        # *clr4examp* updates
        
        # if clr4examp is starting this frame...
        if clr4examp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clr4examp.frameNStart = frameN  # exact frame index
            clr4examp.tStart = t  # local t and not account for scr refresh
            clr4examp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clr4examp, 'tStartRefresh')  # time at next scr refresh
            # update status
            clr4examp.status = STARTED
            clr4examp.setAutoDraw(True)
        
        # if clr4examp is active this frame...
        if clr4examp.status == STARTED:
            # update params
            pass
        
        # if clr4examp is stopping this frame...
        if clr4examp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clr4examp.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                clr4examp.tStop = t  # not accounting for scr refresh
                clr4examp.frameNStop = frameN  # exact frame index
                # update status
                clr4examp.status = FINISHED
                clr4examp.setAutoDraw(False)
        
        # *clr1trial* updates
        
        # if clr1trial is starting this frame...
        if clr1trial.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            clr1trial.frameNStart = frameN  # exact frame index
            clr1trial.tStart = t  # local t and not account for scr refresh
            clr1trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clr1trial, 'tStartRefresh')  # time at next scr refresh
            # update status
            clr1trial.status = STARTED
            clr1trial.setAutoDraw(True)
        
        # if clr1trial is active this frame...
        if clr1trial.status == STARTED:
            # update params
            pass
        
        # if clr1trial is stopping this frame...
        if clr1trial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clr1trial.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                clr1trial.tStop = t  # not accounting for scr refresh
                clr1trial.frameNStop = frameN  # exact frame index
                # update status
                clr1trial.status = FINISHED
                clr1trial.setAutoDraw(False)
        
        # *clr2trail* updates
        
        # if clr2trail is starting this frame...
        if clr2trail.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            clr2trail.frameNStart = frameN  # exact frame index
            clr2trail.tStart = t  # local t and not account for scr refresh
            clr2trail.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clr2trail, 'tStartRefresh')  # time at next scr refresh
            # update status
            clr2trail.status = STARTED
            clr2trail.setAutoDraw(True)
        
        # if clr2trail is active this frame...
        if clr2trail.status == STARTED:
            # update params
            pass
        
        # if clr2trail is stopping this frame...
        if clr2trail.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clr2trail.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                clr2trail.tStop = t  # not accounting for scr refresh
                clr2trail.frameNStop = frameN  # exact frame index
                # update status
                clr2trail.status = FINISHED
                clr2trail.setAutoDraw(False)
        
        # *clr3trail* updates
        
        # if clr3trail is starting this frame...
        if clr3trail.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            clr3trail.frameNStart = frameN  # exact frame index
            clr3trail.tStart = t  # local t and not account for scr refresh
            clr3trail.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clr3trail, 'tStartRefresh')  # time at next scr refresh
            # update status
            clr3trail.status = STARTED
            clr3trail.setAutoDraw(True)
        
        # if clr3trail is active this frame...
        if clr3trail.status == STARTED:
            # update params
            pass
        
        # if clr3trail is stopping this frame...
        if clr3trail.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clr3trail.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                clr3trail.tStop = t  # not accounting for scr refresh
                clr3trail.frameNStop = frameN  # exact frame index
                # update status
                clr3trail.status = FINISHED
                clr3trail.setAutoDraw(False)
        
        # *clr4trail* updates
        
        # if clr4trail is starting this frame...
        if clr4trail.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            clr4trail.frameNStart = frameN  # exact frame index
            clr4trail.tStart = t  # local t and not account for scr refresh
            clr4trail.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clr4trail, 'tStartRefresh')  # time at next scr refresh
            # update status
            clr4trail.status = STARTED
            clr4trail.setAutoDraw(True)
        
        # if clr4trail is active this frame...
        if clr4trail.status == STARTED:
            # update params
            pass
        
        # if clr4trail is stopping this frame...
        if clr4trail.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clr4trail.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                clr4trail.tStop = t  # not accounting for scr refresh
                clr4trail.frameNStop = frameN  # exact frame index
                # update status
                clr4trail.status = FINISHED
                clr4trail.setAutoDraw(False)
        
        # *key_skip* updates
        waitOnFlip = False
        
        # if key_skip is starting this frame...
        if key_skip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_skip.frameNStart = frameN  # exact frame index
            key_skip.tStart = t  # local t and not account for scr refresh
            key_skip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_skip, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_skip.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_skip.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_skip.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_skip is stopping this frame...
        if key_skip.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_skip.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                key_skip.tStop = t  # not accounting for scr refresh
                key_skip.frameNStop = frameN  # exact frame index
                # update status
                key_skip.status = FINISHED
                key_skip.status = FINISHED
        if key_skip.status == STARTED and not waitOnFlip:
            theseKeys = key_skip.getKeys(keyList=['space'], waitRelease=False)
            _key_skip_allKeys.extend(theseKeys)
            if len(_key_skip_allKeys):
                key_skip.keys = _key_skip_allKeys[-1].name  # just the last key pressed
                key_skip.rt = _key_skip_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *MASKclr1tr* updates
        
        # if MASKclr1tr is starting this frame...
        if MASKclr1tr.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            MASKclr1tr.frameNStart = frameN  # exact frame index
            MASKclr1tr.tStart = t  # local t and not account for scr refresh
            MASKclr1tr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MASKclr1tr, 'tStartRefresh')  # time at next scr refresh
            # update status
            MASKclr1tr.status = STARTED
            MASKclr1tr.setAutoDraw(True)
        
        # if MASKclr1tr is active this frame...
        if MASKclr1tr.status == STARTED:
            # update params
            pass
        
        # if MASKclr1tr is stopping this frame...
        if MASKclr1tr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MASKclr1tr.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                MASKclr1tr.tStop = t  # not accounting for scr refresh
                MASKclr1tr.frameNStop = frameN  # exact frame index
                # update status
                MASKclr1tr.status = FINISHED
                MASKclr1tr.setAutoDraw(False)
        
        # *MASKclr2tr* updates
        
        # if MASKclr2tr is starting this frame...
        if MASKclr2tr.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            MASKclr2tr.frameNStart = frameN  # exact frame index
            MASKclr2tr.tStart = t  # local t and not account for scr refresh
            MASKclr2tr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MASKclr2tr, 'tStartRefresh')  # time at next scr refresh
            # update status
            MASKclr2tr.status = STARTED
            MASKclr2tr.setAutoDraw(True)
        
        # if MASKclr2tr is active this frame...
        if MASKclr2tr.status == STARTED:
            # update params
            pass
        
        # if MASKclr2tr is stopping this frame...
        if MASKclr2tr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MASKclr2tr.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                MASKclr2tr.tStop = t  # not accounting for scr refresh
                MASKclr2tr.frameNStop = frameN  # exact frame index
                # update status
                MASKclr2tr.status = FINISHED
                MASKclr2tr.setAutoDraw(False)
        
        # *MASKclr3tr* updates
        
        # if MASKclr3tr is starting this frame...
        if MASKclr3tr.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            MASKclr3tr.frameNStart = frameN  # exact frame index
            MASKclr3tr.tStart = t  # local t and not account for scr refresh
            MASKclr3tr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MASKclr3tr, 'tStartRefresh')  # time at next scr refresh
            # update status
            MASKclr3tr.status = STARTED
            MASKclr3tr.setAutoDraw(True)
        
        # if MASKclr3tr is active this frame...
        if MASKclr3tr.status == STARTED:
            # update params
            pass
        
        # if MASKclr3tr is stopping this frame...
        if MASKclr3tr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MASKclr3tr.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                MASKclr3tr.tStop = t  # not accounting for scr refresh
                MASKclr3tr.frameNStop = frameN  # exact frame index
                # update status
                MASKclr3tr.status = FINISHED
                MASKclr3tr.setAutoDraw(False)
        
        # *MASKclr4tr* updates
        
        # if MASKclr4tr is starting this frame...
        if MASKclr4tr.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            MASKclr4tr.frameNStart = frameN  # exact frame index
            MASKclr4tr.tStart = t  # local t and not account for scr refresh
            MASKclr4tr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MASKclr4tr, 'tStartRefresh')  # time at next scr refresh
            # update status
            MASKclr4tr.status = STARTED
            MASKclr4tr.setAutoDraw(True)
        
        # if MASKclr4tr is active this frame...
        if MASKclr4tr.status == STARTED:
            # update params
            pass
        
        # if MASKclr4tr is stopping this frame...
        if MASKclr4tr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MASKclr4tr.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                MASKclr4tr.tStop = t  # not accounting for scr refresh
                MASKclr4tr.frameNStop = frameN  # exact frame index
                # update status
                MASKclr4tr.status = FINISHED
                MASKclr4tr.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CC_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CC_trial" ---
    for thisComponent in CC_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    
    # --- Prepare to start Routine "blank" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [fix]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.8:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        
        # if fix is starting this frame...
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            # update status
            fix.status = STARTED
            fix.setAutoDraw(True)
        
        # if fix is active this frame...
        if fix.status == STARTED:
            # update params
            pass
        
        # if fix is stopping this frame...
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                # update status
                fix.status = FINISHED
                fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank" ---
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.800000)
    
    # --- Prepare to start Routine "CC_trainAnsw" ---
    continueRoutine = True
    # update component parameters for each repeat
    l_point_2.setFillColor(l_test)
    r_point_2.setFillColor(r_test)
    CC_resp_2.keys = []
    CC_resp_2.rt = []
    _CC_resp_2_allKeys = []
    # keep track of which components have finished
    CC_trainAnswComponents = [l_point_2, r_point_2, CC_resp_2]
    for thisComponent in CC_trainAnswComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "CC_trainAnsw" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *l_point_2* updates
        
        # if l_point_2 is starting this frame...
        if l_point_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            l_point_2.frameNStart = frameN  # exact frame index
            l_point_2.tStart = t  # local t and not account for scr refresh
            l_point_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l_point_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            l_point_2.status = STARTED
            l_point_2.setAutoDraw(True)
        
        # if l_point_2 is active this frame...
        if l_point_2.status == STARTED:
            # update params
            pass
        
        # if l_point_2 is stopping this frame...
        if l_point_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l_point_2.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                l_point_2.tStop = t  # not accounting for scr refresh
                l_point_2.frameNStop = frameN  # exact frame index
                # update status
                l_point_2.status = FINISHED
                l_point_2.setAutoDraw(False)
        
        # *r_point_2* updates
        
        # if r_point_2 is starting this frame...
        if r_point_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            r_point_2.frameNStart = frameN  # exact frame index
            r_point_2.tStart = t  # local t and not account for scr refresh
            r_point_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(r_point_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            r_point_2.status = STARTED
            r_point_2.setAutoDraw(True)
        
        # if r_point_2 is active this frame...
        if r_point_2.status == STARTED:
            # update params
            pass
        
        # if r_point_2 is stopping this frame...
        if r_point_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > r_point_2.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                r_point_2.tStop = t  # not accounting for scr refresh
                r_point_2.frameNStop = frameN  # exact frame index
                # update status
                r_point_2.status = FINISHED
                r_point_2.setAutoDraw(False)
        
        # *CC_resp_2* updates
        waitOnFlip = False
        
        # if CC_resp_2 is starting this frame...
        if CC_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CC_resp_2.frameNStart = frameN  # exact frame index
            CC_resp_2.tStart = t  # local t and not account for scr refresh
            CC_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CC_resp_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            CC_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(CC_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(CC_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if CC_resp_2 is stopping this frame...
        if CC_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CC_resp_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                CC_resp_2.tStop = t  # not accounting for scr refresh
                CC_resp_2.frameNStop = frameN  # exact frame index
                # update status
                CC_resp_2.status = FINISHED
                CC_resp_2.status = FINISHED
        if CC_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = CC_resp_2.getKeys(keyList=['left','right', 'space'], waitRelease=False)
            _CC_resp_2_allKeys.extend(theseKeys)
            if len(_CC_resp_2_allKeys):
                CC_resp_2.keys = _CC_resp_2_allKeys[-1].name  # just the last key pressed
                CC_resp_2.rt = _CC_resp_2_allKeys[-1].rt
                # was this correct?
                if (CC_resp_2.keys == str(answ)) or (CC_resp_2.keys == answ):
                    CC_resp_2.corr = 1
                else:
                    CC_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CC_trainAnswComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CC_trainAnsw" ---
    for thisComponent in CC_trainAnswComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if CC_resp_2.keys in ['', [], None]:  # No response was made
        CC_resp_2.keys = None
        # was no response the correct answer?!
        if str(answ).lower() == 'none':
           CC_resp_2.corr = 1;  # correct non-response
        else:
           CC_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for training (TrialHandler)
    training.addData('CC_resp_2.keys',CC_resp_2.keys)
    training.addData('CC_resp_2.corr', CC_resp_2.corr)
    if CC_resp_2.keys != None:  # we had a response
        training.addData('CC_resp_2.rt', CC_resp_2.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "FB" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from loop_stop
    if not CC_resp_2.keys :
        msg="Нет ответа"
    elif CC_resp_2.corr:#stored on last run routine
        msg="Да! Правильный цвет:"
    else:
        msg="Нет! Вот правильный:"
    
    FB_txt.setText(msg)
    FB_clr.setFillColor(realclr)
    # keep track of which components have finished
    FBComponents = [FB_txt, FB_clr]
    for thisComponent in FBComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "FB" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FB_txt* updates
        
        # if FB_txt is starting this frame...
        if FB_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FB_txt.frameNStart = frameN  # exact frame index
            FB_txt.tStart = t  # local t and not account for scr refresh
            FB_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FB_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            FB_txt.status = STARTED
            FB_txt.setAutoDraw(True)
        
        # if FB_txt is active this frame...
        if FB_txt.status == STARTED:
            # update params
            pass
        
        # if FB_txt is stopping this frame...
        if FB_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FB_txt.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                FB_txt.tStop = t  # not accounting for scr refresh
                FB_txt.frameNStop = frameN  # exact frame index
                # update status
                FB_txt.status = FINISHED
                FB_txt.setAutoDraw(False)
        
        # *FB_clr* updates
        
        # if FB_clr is starting this frame...
        if FB_clr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FB_clr.frameNStart = frameN  # exact frame index
            FB_clr.tStart = t  # local t and not account for scr refresh
            FB_clr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FB_clr, 'tStartRefresh')  # time at next scr refresh
            # update status
            FB_clr.status = STARTED
            FB_clr.setAutoDraw(True)
        
        # if FB_clr is active this frame...
        if FB_clr.status == STARTED:
            # update params
            pass
        
        # if FB_clr is stopping this frame...
        if FB_clr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FB_clr.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                FB_clr.tStop = t  # not accounting for scr refresh
                FB_clr.frameNStop = frameN  # exact frame index
                # update status
                FB_clr.status = FINISHED
                FB_clr.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FBComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "FB" ---
    for thisComponent in FBComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from loop_stop
    if training.thisN == 3:
        currentLoop.finished = True
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'training'


# --- Prepare to start Routine "CC_instr2" ---
continueRoutine = True
# update component parameters for each repeat
instr2_resp.keys = []
instr2_resp.rt = []
_instr2_resp_allKeys = []
# keep track of which components have finished
CC_instr2Components = [instr2_text, instr2_resp]
for thisComponent in CC_instr2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "CC_instr2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr2_text* updates
    
    # if instr2_text is starting this frame...
    if instr2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr2_text.frameNStart = frameN  # exact frame index
        instr2_text.tStart = t  # local t and not account for scr refresh
        instr2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr2_text, 'tStartRefresh')  # time at next scr refresh
        # update status
        instr2_text.status = STARTED
        instr2_text.setAutoDraw(True)
    
    # if instr2_text is active this frame...
    if instr2_text.status == STARTED:
        # update params
        pass
    
    # *instr2_resp* updates
    waitOnFlip = False
    
    # if instr2_resp is starting this frame...
    if instr2_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr2_resp.frameNStart = frameN  # exact frame index
        instr2_resp.tStart = t  # local t and not account for scr refresh
        instr2_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr2_resp, 'tStartRefresh')  # time at next scr refresh
        # update status
        instr2_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr2_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr2_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr2_resp.status == STARTED and not waitOnFlip:
        theseKeys = instr2_resp.getKeys(keyList=['space'], waitRelease=False)
        _instr2_resp_allKeys.extend(theseKeys)
        if len(_instr2_resp_allKeys):
            instr2_resp.keys = _instr2_resp_allKeys[-1].name  # just the last key pressed
            instr2_resp.rt = _instr2_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in CC_instr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "CC_instr2" ---
for thisComponent in CC_instr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "CC_instr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('CC_easylowhard_generalcond.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "CC_trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    clr1examp.setFillColor(clr1p1)
    clr2examp.setFillColor(clr2p1)
    clr3examp.setFillColor(clr3p1)
    clr4examp.setFillColor(clr4p1)
    clr1trial.setFillColor(clr1p2)
    clr2trail.setFillColor(clr2p2)
    clr3trail.setFillColor(clr3p2)
    clr4trail.setFillColor(clr4p2)
    key_skip.keys = []
    key_skip.rt = []
    _key_skip_allKeys = []
    MASKclr1tr.setFillColor('black')
    MASKclr2tr.setFillColor('black')
    MASKclr3tr.setFillColor('black')
    MASKclr4tr.setFillColor('black')
    # keep track of which components have finished
    CC_trialComponents = [clr1examp, clr2examp, clr3examp, clr4examp, clr1trial, clr2trail, clr3trail, clr4trail, key_skip, MASKclr1tr, MASKclr2tr, MASKclr3tr, MASKclr4tr]
    for thisComponent in CC_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "CC_trial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 6.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *clr1examp* updates
        
        # if clr1examp is starting this frame...
        if clr1examp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clr1examp.frameNStart = frameN  # exact frame index
            clr1examp.tStart = t  # local t and not account for scr refresh
            clr1examp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clr1examp, 'tStartRefresh')  # time at next scr refresh
            # update status
            clr1examp.status = STARTED
            clr1examp.setAutoDraw(True)
        
        # if clr1examp is active this frame...
        if clr1examp.status == STARTED:
            # update params
            pass
        
        # if clr1examp is stopping this frame...
        if clr1examp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clr1examp.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                clr1examp.tStop = t  # not accounting for scr refresh
                clr1examp.frameNStop = frameN  # exact frame index
                # update status
                clr1examp.status = FINISHED
                clr1examp.setAutoDraw(False)
        
        # *clr2examp* updates
        
        # if clr2examp is starting this frame...
        if clr2examp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clr2examp.frameNStart = frameN  # exact frame index
            clr2examp.tStart = t  # local t and not account for scr refresh
            clr2examp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clr2examp, 'tStartRefresh')  # time at next scr refresh
            # update status
            clr2examp.status = STARTED
            clr2examp.setAutoDraw(True)
        
        # if clr2examp is active this frame...
        if clr2examp.status == STARTED:
            # update params
            pass
        
        # if clr2examp is stopping this frame...
        if clr2examp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clr2examp.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                clr2examp.tStop = t  # not accounting for scr refresh
                clr2examp.frameNStop = frameN  # exact frame index
                # update status
                clr2examp.status = FINISHED
                clr2examp.setAutoDraw(False)
        
        # *clr3examp* updates
        
        # if clr3examp is starting this frame...
        if clr3examp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clr3examp.frameNStart = frameN  # exact frame index
            clr3examp.tStart = t  # local t and not account for scr refresh
            clr3examp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clr3examp, 'tStartRefresh')  # time at next scr refresh
            # update status
            clr3examp.status = STARTED
            clr3examp.setAutoDraw(True)
        
        # if clr3examp is active this frame...
        if clr3examp.status == STARTED:
            # update params
            pass
        
        # if clr3examp is stopping this frame...
        if clr3examp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clr3examp.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                clr3examp.tStop = t  # not accounting for scr refresh
                clr3examp.frameNStop = frameN  # exact frame index
                # update status
                clr3examp.status = FINISHED
                clr3examp.setAutoDraw(False)
        
        # *clr4examp* updates
        
        # if clr4examp is starting this frame...
        if clr4examp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            clr4examp.frameNStart = frameN  # exact frame index
            clr4examp.tStart = t  # local t and not account for scr refresh
            clr4examp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clr4examp, 'tStartRefresh')  # time at next scr refresh
            # update status
            clr4examp.status = STARTED
            clr4examp.setAutoDraw(True)
        
        # if clr4examp is active this frame...
        if clr4examp.status == STARTED:
            # update params
            pass
        
        # if clr4examp is stopping this frame...
        if clr4examp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clr4examp.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                clr4examp.tStop = t  # not accounting for scr refresh
                clr4examp.frameNStop = frameN  # exact frame index
                # update status
                clr4examp.status = FINISHED
                clr4examp.setAutoDraw(False)
        
        # *clr1trial* updates
        
        # if clr1trial is starting this frame...
        if clr1trial.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            clr1trial.frameNStart = frameN  # exact frame index
            clr1trial.tStart = t  # local t and not account for scr refresh
            clr1trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clr1trial, 'tStartRefresh')  # time at next scr refresh
            # update status
            clr1trial.status = STARTED
            clr1trial.setAutoDraw(True)
        
        # if clr1trial is active this frame...
        if clr1trial.status == STARTED:
            # update params
            pass
        
        # if clr1trial is stopping this frame...
        if clr1trial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clr1trial.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                clr1trial.tStop = t  # not accounting for scr refresh
                clr1trial.frameNStop = frameN  # exact frame index
                # update status
                clr1trial.status = FINISHED
                clr1trial.setAutoDraw(False)
        
        # *clr2trail* updates
        
        # if clr2trail is starting this frame...
        if clr2trail.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            clr2trail.frameNStart = frameN  # exact frame index
            clr2trail.tStart = t  # local t and not account for scr refresh
            clr2trail.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clr2trail, 'tStartRefresh')  # time at next scr refresh
            # update status
            clr2trail.status = STARTED
            clr2trail.setAutoDraw(True)
        
        # if clr2trail is active this frame...
        if clr2trail.status == STARTED:
            # update params
            pass
        
        # if clr2trail is stopping this frame...
        if clr2trail.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clr2trail.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                clr2trail.tStop = t  # not accounting for scr refresh
                clr2trail.frameNStop = frameN  # exact frame index
                # update status
                clr2trail.status = FINISHED
                clr2trail.setAutoDraw(False)
        
        # *clr3trail* updates
        
        # if clr3trail is starting this frame...
        if clr3trail.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            clr3trail.frameNStart = frameN  # exact frame index
            clr3trail.tStart = t  # local t and not account for scr refresh
            clr3trail.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clr3trail, 'tStartRefresh')  # time at next scr refresh
            # update status
            clr3trail.status = STARTED
            clr3trail.setAutoDraw(True)
        
        # if clr3trail is active this frame...
        if clr3trail.status == STARTED:
            # update params
            pass
        
        # if clr3trail is stopping this frame...
        if clr3trail.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clr3trail.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                clr3trail.tStop = t  # not accounting for scr refresh
                clr3trail.frameNStop = frameN  # exact frame index
                # update status
                clr3trail.status = FINISHED
                clr3trail.setAutoDraw(False)
        
        # *clr4trail* updates
        
        # if clr4trail is starting this frame...
        if clr4trail.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
            # keep track of start time/frame for later
            clr4trail.frameNStart = frameN  # exact frame index
            clr4trail.tStart = t  # local t and not account for scr refresh
            clr4trail.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(clr4trail, 'tStartRefresh')  # time at next scr refresh
            # update status
            clr4trail.status = STARTED
            clr4trail.setAutoDraw(True)
        
        # if clr4trail is active this frame...
        if clr4trail.status == STARTED:
            # update params
            pass
        
        # if clr4trail is stopping this frame...
        if clr4trail.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > clr4trail.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                clr4trail.tStop = t  # not accounting for scr refresh
                clr4trail.frameNStop = frameN  # exact frame index
                # update status
                clr4trail.status = FINISHED
                clr4trail.setAutoDraw(False)
        
        # *key_skip* updates
        waitOnFlip = False
        
        # if key_skip is starting this frame...
        if key_skip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_skip.frameNStart = frameN  # exact frame index
            key_skip.tStart = t  # local t and not account for scr refresh
            key_skip.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_skip, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_skip.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_skip.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_skip.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_skip is stopping this frame...
        if key_skip.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_skip.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                key_skip.tStop = t  # not accounting for scr refresh
                key_skip.frameNStop = frameN  # exact frame index
                # update status
                key_skip.status = FINISHED
                key_skip.status = FINISHED
        if key_skip.status == STARTED and not waitOnFlip:
            theseKeys = key_skip.getKeys(keyList=['space'], waitRelease=False)
            _key_skip_allKeys.extend(theseKeys)
            if len(_key_skip_allKeys):
                key_skip.keys = _key_skip_allKeys[-1].name  # just the last key pressed
                key_skip.rt = _key_skip_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *MASKclr1tr* updates
        
        # if MASKclr1tr is starting this frame...
        if MASKclr1tr.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            MASKclr1tr.frameNStart = frameN  # exact frame index
            MASKclr1tr.tStart = t  # local t and not account for scr refresh
            MASKclr1tr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MASKclr1tr, 'tStartRefresh')  # time at next scr refresh
            # update status
            MASKclr1tr.status = STARTED
            MASKclr1tr.setAutoDraw(True)
        
        # if MASKclr1tr is active this frame...
        if MASKclr1tr.status == STARTED:
            # update params
            pass
        
        # if MASKclr1tr is stopping this frame...
        if MASKclr1tr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MASKclr1tr.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                MASKclr1tr.tStop = t  # not accounting for scr refresh
                MASKclr1tr.frameNStop = frameN  # exact frame index
                # update status
                MASKclr1tr.status = FINISHED
                MASKclr1tr.setAutoDraw(False)
        
        # *MASKclr2tr* updates
        
        # if MASKclr2tr is starting this frame...
        if MASKclr2tr.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            MASKclr2tr.frameNStart = frameN  # exact frame index
            MASKclr2tr.tStart = t  # local t and not account for scr refresh
            MASKclr2tr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MASKclr2tr, 'tStartRefresh')  # time at next scr refresh
            # update status
            MASKclr2tr.status = STARTED
            MASKclr2tr.setAutoDraw(True)
        
        # if MASKclr2tr is active this frame...
        if MASKclr2tr.status == STARTED:
            # update params
            pass
        
        # if MASKclr2tr is stopping this frame...
        if MASKclr2tr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MASKclr2tr.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                MASKclr2tr.tStop = t  # not accounting for scr refresh
                MASKclr2tr.frameNStop = frameN  # exact frame index
                # update status
                MASKclr2tr.status = FINISHED
                MASKclr2tr.setAutoDraw(False)
        
        # *MASKclr3tr* updates
        
        # if MASKclr3tr is starting this frame...
        if MASKclr3tr.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            MASKclr3tr.frameNStart = frameN  # exact frame index
            MASKclr3tr.tStart = t  # local t and not account for scr refresh
            MASKclr3tr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MASKclr3tr, 'tStartRefresh')  # time at next scr refresh
            # update status
            MASKclr3tr.status = STARTED
            MASKclr3tr.setAutoDraw(True)
        
        # if MASKclr3tr is active this frame...
        if MASKclr3tr.status == STARTED:
            # update params
            pass
        
        # if MASKclr3tr is stopping this frame...
        if MASKclr3tr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MASKclr3tr.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                MASKclr3tr.tStop = t  # not accounting for scr refresh
                MASKclr3tr.frameNStop = frameN  # exact frame index
                # update status
                MASKclr3tr.status = FINISHED
                MASKclr3tr.setAutoDraw(False)
        
        # *MASKclr4tr* updates
        
        # if MASKclr4tr is starting this frame...
        if MASKclr4tr.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            MASKclr4tr.frameNStart = frameN  # exact frame index
            MASKclr4tr.tStart = t  # local t and not account for scr refresh
            MASKclr4tr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MASKclr4tr, 'tStartRefresh')  # time at next scr refresh
            # update status
            MASKclr4tr.status = STARTED
            MASKclr4tr.setAutoDraw(True)
        
        # if MASKclr4tr is active this frame...
        if MASKclr4tr.status == STARTED:
            # update params
            pass
        
        # if MASKclr4tr is stopping this frame...
        if MASKclr4tr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > MASKclr4tr.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                MASKclr4tr.tStop = t  # not accounting for scr refresh
                MASKclr4tr.frameNStop = frameN  # exact frame index
                # update status
                MASKclr4tr.status = FINISHED
                MASKclr4tr.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CC_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CC_trial" ---
    for thisComponent in CC_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-6.000000)
    
    # --- Prepare to start Routine "blank" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [fix]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.8:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        
        # if fix is starting this frame...
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            # update status
            fix.status = STARTED
            fix.setAutoDraw(True)
        
        # if fix is active this frame...
        if fix.status == STARTED:
            # update params
            pass
        
        # if fix is stopping this frame...
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                # update status
                fix.status = FINISHED
                fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank" ---
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.800000)
    
    # --- Prepare to start Routine "CC_answer" ---
    continueRoutine = True
    # update component parameters for each repeat
    l_point.setFillColor(l_test)
    r_point.setFillColor(r_test)
    CC_resp.keys = []
    CC_resp.rt = []
    _CC_resp_allKeys = []
    # keep track of which components have finished
    CC_answerComponents = [l_point, r_point, CC_resp]
    for thisComponent in CC_answerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "CC_answer" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *l_point* updates
        
        # if l_point is starting this frame...
        if l_point.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            l_point.frameNStart = frameN  # exact frame index
            l_point.tStart = t  # local t and not account for scr refresh
            l_point.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(l_point, 'tStartRefresh')  # time at next scr refresh
            # update status
            l_point.status = STARTED
            l_point.setAutoDraw(True)
        
        # if l_point is active this frame...
        if l_point.status == STARTED:
            # update params
            pass
        
        # if l_point is stopping this frame...
        if l_point.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > l_point.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                l_point.tStop = t  # not accounting for scr refresh
                l_point.frameNStop = frameN  # exact frame index
                # update status
                l_point.status = FINISHED
                l_point.setAutoDraw(False)
        
        # *r_point* updates
        
        # if r_point is starting this frame...
        if r_point.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            r_point.frameNStart = frameN  # exact frame index
            r_point.tStart = t  # local t and not account for scr refresh
            r_point.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(r_point, 'tStartRefresh')  # time at next scr refresh
            # update status
            r_point.status = STARTED
            r_point.setAutoDraw(True)
        
        # if r_point is active this frame...
        if r_point.status == STARTED:
            # update params
            pass
        
        # if r_point is stopping this frame...
        if r_point.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > r_point.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                r_point.tStop = t  # not accounting for scr refresh
                r_point.frameNStop = frameN  # exact frame index
                # update status
                r_point.status = FINISHED
                r_point.setAutoDraw(False)
        
        # *CC_resp* updates
        waitOnFlip = False
        
        # if CC_resp is starting this frame...
        if CC_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CC_resp.frameNStart = frameN  # exact frame index
            CC_resp.tStart = t  # local t and not account for scr refresh
            CC_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CC_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            CC_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(CC_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(CC_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if CC_resp is stopping this frame...
        if CC_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CC_resp.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                CC_resp.tStop = t  # not accounting for scr refresh
                CC_resp.frameNStop = frameN  # exact frame index
                # update status
                CC_resp.status = FINISHED
                CC_resp.status = FINISHED
        if CC_resp.status == STARTED and not waitOnFlip:
            theseKeys = CC_resp.getKeys(keyList=['left','right'], waitRelease=False)
            _CC_resp_allKeys.extend(theseKeys)
            if len(_CC_resp_allKeys):
                CC_resp.keys = _CC_resp_allKeys[-1].name  # just the last key pressed
                CC_resp.rt = _CC_resp_allKeys[-1].rt
                # was this correct?
                if (CC_resp.keys == str(answ)) or (CC_resp.keys == answ):
                    CC_resp.corr = 1
                else:
                    CC_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CC_answerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CC_answer" ---
    for thisComponent in CC_answerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if CC_resp.keys in ['', [], None]:  # No response was made
        CC_resp.keys = None
        # was no response the correct answer?!
        if str(answ).lower() == 'none':
           CC_resp.corr = 1;  # correct non-response
        else:
           CC_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('CC_resp.keys',CC_resp.keys)
    trials.addData('CC_resp.corr', CC_resp.corr)
    if CC_resp.keys != None:  # we had a response
        trials.addData('CC_resp.rt', CC_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "blank" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [fix]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "blank" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.8:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix* updates
        
        # if fix is starting this frame...
        if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix.frameNStart = frameN  # exact frame index
            fix.tStart = t  # local t and not account for scr refresh
            fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
            # update status
            fix.status = STARTED
            fix.setAutoDraw(True)
        
        # if fix is active this frame...
        if fix.status == STARTED:
            # update params
            pass
        
        # if fix is stopping this frame...
        if fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                fix.tStop = t  # not accounting for scr refresh
                fix.frameNStop = frameN  # exact frame index
                # update status
                fix.status = FINISHED
                fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "blank" ---
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.800000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "finish" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
finishComponents = [finish_txt]
for thisComponent in finishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "finish" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finish_txt* updates
    
    # if finish_txt is starting this frame...
    if finish_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finish_txt.frameNStart = frameN  # exact frame index
        finish_txt.tStart = t  # local t and not account for scr refresh
        finish_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finish_txt, 'tStartRefresh')  # time at next scr refresh
        # update status
        finish_txt.status = STARTED
        finish_txt.setAutoDraw(True)
    
    # if finish_txt is active this frame...
    if finish_txt.status == STARTED:
        # update params
        pass
    
    # if finish_txt is stopping this frame...
    if finish_txt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finish_txt.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            finish_txt.tStop = t  # not accounting for scr refresh
            finish_txt.frameNStop = frameN  # exact frame index
            # update status
            finish_txt.status = FINISHED
            finish_txt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "finish" ---
for thisComponent in finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
