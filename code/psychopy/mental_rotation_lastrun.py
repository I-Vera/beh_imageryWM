#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on March 27, 2026, at 13:21
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
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
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
expName = 'MR'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\paper\\OneDrive\\Desktop\\PsychoPy\\masters_imagery\\mental_rotation_lastrun.py',
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
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
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

# --- Initialize components for Routine "mentalrot_instr" ---
mentalrot_announce = visual.TextStim(win=win, name='mentalrot_announce',
    text='Задача на ментальное вращение',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mentalrot_instr_txt = visual.TextStim(win=win, name='mentalrot_instr_txt',
    text='Вам будут показаны пары фигур: одна слева, другая справа от центра экрана. Ваша задача — как можно быстрее определить, одинаковые ли это фигуры (одна повёрнута относительно другой) или разные (одна является зеркальным отражением другой).\n\nЕсли фигуры одинаковые, нажмите кнопку "←".\nЕсли фигуры разные (зеркальные), нажмите кнопку "→".\n\nСтарайтесь не поворачивать голову — используйте только воображение. \n\nЧтобы начать тренировочный этап, нажмите любую кнопку.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
mentalrot_instr_key = keyboard.Keyboard()

# --- Initialize components for Routine "fix" ---
blank = visual.TextStim(win=win, name='blank',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "mentalrot_train" ---
mr_image_2 = visual.ImageStim(
    win=win,
    name='mr_image_2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mr_stim_2 = visual.ImageStim(
    win=win,
    name='mr_stim_2', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0.4, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mr_answ_2 = keyboard.Keyboard()
mr_hint_2 = visual.TextStim(win=win, name='mr_hint_2',
    text='← (ДА)           Та же фигура?           (НЕТ) →',
    font='Open Sans',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "mentalrot_instr_2" ---
mentalrot_instr_txt_2 = visual.TextStim(win=win, name='mentalrot_instr_txt_2',
    text='Тренировка окончена!\n\nЧтобы начать основной этап, нажмите любую кнопку.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mentalrot_instr_key_2 = keyboard.Keyboard()

# --- Initialize components for Routine "fix" ---
blank = visual.TextStim(win=win, name='blank',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "mentalrot_task" ---
mr_image = visual.ImageStim(
    win=win,
    name='mr_image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.4, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
mr_stim = visual.ImageStim(
    win=win,
    name='mr_stim', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0.4, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=True, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
mr_answ = keyboard.Keyboard()
mr_hint = visual.TextStim(win=win, name='mr_hint',
    text='← (ДА)           Та же фигура?           (НЕТ) →',
    font='Open Sans',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "finish_goodbye" ---
byebye_text = visual.TextStim(win=win, name='byebye_text',
    text='На этом эксперимент окончен.\n\nБольшое спасибо за участие! ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "mentalrot_instr" ---
continueRoutine = True
# update component parameters for each repeat
mentalrot_instr_key.keys = []
mentalrot_instr_key.rt = []
_mentalrot_instr_key_allKeys = []
# keep track of which components have finished
mentalrot_instrComponents = [mentalrot_announce, mentalrot_instr_txt, mentalrot_instr_key]
for thisComponent in mentalrot_instrComponents:
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

# --- Run Routine "mentalrot_instr" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *mentalrot_announce* updates
    
    # if mentalrot_announce is starting this frame...
    if mentalrot_announce.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mentalrot_announce.frameNStart = frameN  # exact frame index
        mentalrot_announce.tStart = t  # local t and not account for scr refresh
        mentalrot_announce.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mentalrot_announce, 'tStartRefresh')  # time at next scr refresh
        # update status
        mentalrot_announce.status = STARTED
        mentalrot_announce.setAutoDraw(True)
    
    # if mentalrot_announce is active this frame...
    if mentalrot_announce.status == STARTED:
        # update params
        pass
    
    # if mentalrot_announce is stopping this frame...
    if mentalrot_announce.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mentalrot_announce.tStartRefresh + 1.5-frameTolerance:
            # keep track of stop time/frame for later
            mentalrot_announce.tStop = t  # not accounting for scr refresh
            mentalrot_announce.frameNStop = frameN  # exact frame index
            # update status
            mentalrot_announce.status = FINISHED
            mentalrot_announce.setAutoDraw(False)
    
    # *mentalrot_instr_txt* updates
    
    # if mentalrot_instr_txt is starting this frame...
    if mentalrot_instr_txt.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        mentalrot_instr_txt.frameNStart = frameN  # exact frame index
        mentalrot_instr_txt.tStart = t  # local t and not account for scr refresh
        mentalrot_instr_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mentalrot_instr_txt, 'tStartRefresh')  # time at next scr refresh
        # update status
        mentalrot_instr_txt.status = STARTED
        mentalrot_instr_txt.setAutoDraw(True)
    
    # if mentalrot_instr_txt is active this frame...
    if mentalrot_instr_txt.status == STARTED:
        # update params
        pass
    
    # *mentalrot_instr_key* updates
    waitOnFlip = False
    
    # if mentalrot_instr_key is starting this frame...
    if mentalrot_instr_key.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        mentalrot_instr_key.frameNStart = frameN  # exact frame index
        mentalrot_instr_key.tStart = t  # local t and not account for scr refresh
        mentalrot_instr_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mentalrot_instr_key, 'tStartRefresh')  # time at next scr refresh
        # update status
        mentalrot_instr_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(mentalrot_instr_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(mentalrot_instr_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if mentalrot_instr_key.status == STARTED and not waitOnFlip:
        theseKeys = mentalrot_instr_key.getKeys(keyList=None, waitRelease=False)
        _mentalrot_instr_key_allKeys.extend(theseKeys)
        if len(_mentalrot_instr_key_allKeys):
            mentalrot_instr_key.keys = _mentalrot_instr_key_allKeys[-1].name  # just the last key pressed
            mentalrot_instr_key.rt = _mentalrot_instr_key_allKeys[-1].rt
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
    for thisComponent in mentalrot_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "mentalrot_instr" ---
for thisComponent in mentalrot_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "mentalrot_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
training = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('mr_condition.xlsx'),
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
    
    # --- Prepare to start Routine "fix" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [blank]
    for thisComponent in fixComponents:
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
    
    # --- Run Routine "fix" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        
        # if blank is starting this frame...
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank.started')
            # update status
            blank.status = STARTED
            blank.setAutoDraw(True)
        
        # if blank is active this frame...
        if blank.status == STARTED:
            # update params
            pass
        
        # if blank is stopping this frame...
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank.stopped')
                # update status
                blank.status = FINISHED
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fix" ---
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "mentalrot_train" ---
    continueRoutine = True
    # update component parameters for each repeat
    mr_image_2.setImage(imagefile)
    mr_stim_2.setImage(stimfile)
    mr_answ_2.keys = []
    mr_answ_2.rt = []
    _mr_answ_2_allKeys = []
    # keep track of which components have finished
    mentalrot_trainComponents = [mr_image_2, mr_stim_2, mr_answ_2, mr_hint_2]
    for thisComponent in mentalrot_trainComponents:
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
    
    # --- Run Routine "mentalrot_train" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mr_image_2* updates
        
        # if mr_image_2 is starting this frame...
        if mr_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mr_image_2.frameNStart = frameN  # exact frame index
            mr_image_2.tStart = t  # local t and not account for scr refresh
            mr_image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mr_image_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            mr_image_2.status = STARTED
            mr_image_2.setAutoDraw(True)
        
        # if mr_image_2 is active this frame...
        if mr_image_2.status == STARTED:
            # update params
            pass
        
        # if mr_image_2 is stopping this frame...
        if mr_image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mr_image_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mr_image_2.tStop = t  # not accounting for scr refresh
                mr_image_2.frameNStop = frameN  # exact frame index
                # update status
                mr_image_2.status = FINISHED
                mr_image_2.setAutoDraw(False)
        
        # *mr_stim_2* updates
        
        # if mr_stim_2 is starting this frame...
        if mr_stim_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mr_stim_2.frameNStart = frameN  # exact frame index
            mr_stim_2.tStart = t  # local t and not account for scr refresh
            mr_stim_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mr_stim_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            mr_stim_2.status = STARTED
            mr_stim_2.setAutoDraw(True)
        
        # if mr_stim_2 is active this frame...
        if mr_stim_2.status == STARTED:
            # update params
            pass
        
        # if mr_stim_2 is stopping this frame...
        if mr_stim_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mr_stim_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mr_stim_2.tStop = t  # not accounting for scr refresh
                mr_stim_2.frameNStop = frameN  # exact frame index
                # update status
                mr_stim_2.status = FINISHED
                mr_stim_2.setAutoDraw(False)
        
        # *mr_answ_2* updates
        waitOnFlip = False
        
        # if mr_answ_2 is starting this frame...
        if mr_answ_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mr_answ_2.frameNStart = frameN  # exact frame index
            mr_answ_2.tStart = t  # local t and not account for scr refresh
            mr_answ_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mr_answ_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'mr_answ_2.started')
            # update status
            mr_answ_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(mr_answ_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(mr_answ_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if mr_answ_2 is stopping this frame...
        if mr_answ_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mr_answ_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mr_answ_2.tStop = t  # not accounting for scr refresh
                mr_answ_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mr_answ_2.stopped')
                # update status
                mr_answ_2.status = FINISHED
                mr_answ_2.status = FINISHED
        if mr_answ_2.status == STARTED and not waitOnFlip:
            theseKeys = mr_answ_2.getKeys(keyList=['left','right'], waitRelease=False)
            _mr_answ_2_allKeys.extend(theseKeys)
            if len(_mr_answ_2_allKeys):
                mr_answ_2.keys = _mr_answ_2_allKeys[-1].name  # just the last key pressed
                mr_answ_2.rt = _mr_answ_2_allKeys[-1].rt
                # was this correct?
                if (mr_answ_2.keys == str(corrAns)) or (mr_answ_2.keys == corrAns):
                    mr_answ_2.corr = 1
                else:
                    mr_answ_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *mr_hint_2* updates
        
        # if mr_hint_2 is starting this frame...
        if mr_hint_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mr_hint_2.frameNStart = frameN  # exact frame index
            mr_hint_2.tStart = t  # local t and not account for scr refresh
            mr_hint_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mr_hint_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            mr_hint_2.status = STARTED
            mr_hint_2.setAutoDraw(True)
        
        # if mr_hint_2 is active this frame...
        if mr_hint_2.status == STARTED:
            # update params
            pass
        
        # if mr_hint_2 is stopping this frame...
        if mr_hint_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mr_hint_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mr_hint_2.tStop = t  # not accounting for scr refresh
                mr_hint_2.frameNStop = frameN  # exact frame index
                # update status
                mr_hint_2.status = FINISHED
                mr_hint_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mentalrot_trainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mentalrot_train" ---
    for thisComponent in mentalrot_trainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if mr_answ_2.keys in ['', [], None]:  # No response was made
        mr_answ_2.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           mr_answ_2.corr = 1;  # correct non-response
        else:
           mr_answ_2.corr = 0;  # failed to respond (incorrectly)
    # store data for training (TrialHandler)
    training.addData('mr_answ_2.keys',mr_answ_2.keys)
    training.addData('mr_answ_2.corr', mr_answ_2.corr)
    if mr_answ_2.keys != None:  # we had a response
        training.addData('mr_answ_2.rt', mr_answ_2.rt)
    # Run 'End Routine' code from code
    if training.thisN == 4:
        currentLoop.finished = True
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'training'


# --- Prepare to start Routine "mentalrot_instr_2" ---
continueRoutine = True
# update component parameters for each repeat
mentalrot_instr_key_2.keys = []
mentalrot_instr_key_2.rt = []
_mentalrot_instr_key_2_allKeys = []
# keep track of which components have finished
mentalrot_instr_2Components = [mentalrot_instr_txt_2, mentalrot_instr_key_2]
for thisComponent in mentalrot_instr_2Components:
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

# --- Run Routine "mentalrot_instr_2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *mentalrot_instr_txt_2* updates
    
    # if mentalrot_instr_txt_2 is starting this frame...
    if mentalrot_instr_txt_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        mentalrot_instr_txt_2.frameNStart = frameN  # exact frame index
        mentalrot_instr_txt_2.tStart = t  # local t and not account for scr refresh
        mentalrot_instr_txt_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mentalrot_instr_txt_2, 'tStartRefresh')  # time at next scr refresh
        # update status
        mentalrot_instr_txt_2.status = STARTED
        mentalrot_instr_txt_2.setAutoDraw(True)
    
    # if mentalrot_instr_txt_2 is active this frame...
    if mentalrot_instr_txt_2.status == STARTED:
        # update params
        pass
    
    # *mentalrot_instr_key_2* updates
    waitOnFlip = False
    
    # if mentalrot_instr_key_2 is starting this frame...
    if mentalrot_instr_key_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        mentalrot_instr_key_2.frameNStart = frameN  # exact frame index
        mentalrot_instr_key_2.tStart = t  # local t and not account for scr refresh
        mentalrot_instr_key_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mentalrot_instr_key_2, 'tStartRefresh')  # time at next scr refresh
        # update status
        mentalrot_instr_key_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(mentalrot_instr_key_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(mentalrot_instr_key_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if mentalrot_instr_key_2.status == STARTED and not waitOnFlip:
        theseKeys = mentalrot_instr_key_2.getKeys(keyList=None, waitRelease=False)
        _mentalrot_instr_key_2_allKeys.extend(theseKeys)
        if len(_mentalrot_instr_key_2_allKeys):
            mentalrot_instr_key_2.keys = _mentalrot_instr_key_2_allKeys[-1].name  # just the last key pressed
            mentalrot_instr_key_2.rt = _mentalrot_instr_key_2_allKeys[-1].rt
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
    for thisComponent in mentalrot_instr_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "mentalrot_instr_2" ---
for thisComponent in mentalrot_instr_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "mentalrot_instr_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
mentalrot_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('mr_condition.xlsx'),
    seed=None, name='mentalrot_trials')
thisExp.addLoop(mentalrot_trials)  # add the loop to the experiment
thisMentalrot_trial = mentalrot_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMentalrot_trial.rgb)
if thisMentalrot_trial != None:
    for paramName in thisMentalrot_trial:
        exec('{} = thisMentalrot_trial[paramName]'.format(paramName))

for thisMentalrot_trial in mentalrot_trials:
    currentLoop = mentalrot_trials
    # abbreviate parameter names if possible (e.g. rgb = thisMentalrot_trial.rgb)
    if thisMentalrot_trial != None:
        for paramName in thisMentalrot_trial:
            exec('{} = thisMentalrot_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "fix" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [blank]
    for thisComponent in fixComponents:
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
    
    # --- Run Routine "fix" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        
        # if blank is starting this frame...
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'blank.started')
            # update status
            blank.status = STARTED
            blank.setAutoDraw(True)
        
        # if blank is active this frame...
        if blank.status == STARTED:
            # update params
            pass
        
        # if blank is stopping this frame...
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank.stopped')
                # update status
                blank.status = FINISHED
                blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "fix" ---
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "mentalrot_task" ---
    continueRoutine = True
    # update component parameters for each repeat
    mr_image.setImage(imagefile)
    mr_stim.setImage(stimfile)
    mr_answ.keys = []
    mr_answ.rt = []
    _mr_answ_allKeys = []
    # keep track of which components have finished
    mentalrot_taskComponents = [mr_image, mr_stim, mr_answ, mr_hint]
    for thisComponent in mentalrot_taskComponents:
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
    
    # --- Run Routine "mentalrot_task" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *mr_image* updates
        
        # if mr_image is starting this frame...
        if mr_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mr_image.frameNStart = frameN  # exact frame index
            mr_image.tStart = t  # local t and not account for scr refresh
            mr_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mr_image, 'tStartRefresh')  # time at next scr refresh
            # update status
            mr_image.status = STARTED
            mr_image.setAutoDraw(True)
        
        # if mr_image is active this frame...
        if mr_image.status == STARTED:
            # update params
            pass
        
        # if mr_image is stopping this frame...
        if mr_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mr_image.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mr_image.tStop = t  # not accounting for scr refresh
                mr_image.frameNStop = frameN  # exact frame index
                # update status
                mr_image.status = FINISHED
                mr_image.setAutoDraw(False)
        
        # *mr_stim* updates
        
        # if mr_stim is starting this frame...
        if mr_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mr_stim.frameNStart = frameN  # exact frame index
            mr_stim.tStart = t  # local t and not account for scr refresh
            mr_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mr_stim, 'tStartRefresh')  # time at next scr refresh
            # update status
            mr_stim.status = STARTED
            mr_stim.setAutoDraw(True)
        
        # if mr_stim is active this frame...
        if mr_stim.status == STARTED:
            # update params
            pass
        
        # if mr_stim is stopping this frame...
        if mr_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mr_stim.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mr_stim.tStop = t  # not accounting for scr refresh
                mr_stim.frameNStop = frameN  # exact frame index
                # update status
                mr_stim.status = FINISHED
                mr_stim.setAutoDraw(False)
        
        # *mr_answ* updates
        waitOnFlip = False
        
        # if mr_answ is starting this frame...
        if mr_answ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mr_answ.frameNStart = frameN  # exact frame index
            mr_answ.tStart = t  # local t and not account for scr refresh
            mr_answ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mr_answ, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'mr_answ.started')
            # update status
            mr_answ.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(mr_answ.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(mr_answ.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if mr_answ is stopping this frame...
        if mr_answ.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mr_answ.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mr_answ.tStop = t  # not accounting for scr refresh
                mr_answ.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'mr_answ.stopped')
                # update status
                mr_answ.status = FINISHED
                mr_answ.status = FINISHED
        if mr_answ.status == STARTED and not waitOnFlip:
            theseKeys = mr_answ.getKeys(keyList=['left','right'], waitRelease=False)
            _mr_answ_allKeys.extend(theseKeys)
            if len(_mr_answ_allKeys):
                mr_answ.keys = _mr_answ_allKeys[-1].name  # just the last key pressed
                mr_answ.rt = _mr_answ_allKeys[-1].rt
                # was this correct?
                if (mr_answ.keys == str(corrAns)) or (mr_answ.keys == corrAns):
                    mr_answ.corr = 1
                else:
                    mr_answ.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *mr_hint* updates
        
        # if mr_hint is starting this frame...
        if mr_hint.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mr_hint.frameNStart = frameN  # exact frame index
            mr_hint.tStart = t  # local t and not account for scr refresh
            mr_hint.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mr_hint, 'tStartRefresh')  # time at next scr refresh
            # update status
            mr_hint.status = STARTED
            mr_hint.setAutoDraw(True)
        
        # if mr_hint is active this frame...
        if mr_hint.status == STARTED:
            # update params
            pass
        
        # if mr_hint is stopping this frame...
        if mr_hint.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mr_hint.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mr_hint.tStop = t  # not accounting for scr refresh
                mr_hint.frameNStop = frameN  # exact frame index
                # update status
                mr_hint.status = FINISHED
                mr_hint.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in mentalrot_taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "mentalrot_task" ---
    for thisComponent in mentalrot_taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if mr_answ.keys in ['', [], None]:  # No response was made
        mr_answ.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           mr_answ.corr = 1;  # correct non-response
        else:
           mr_answ.corr = 0;  # failed to respond (incorrectly)
    # store data for mentalrot_trials (TrialHandler)
    mentalrot_trials.addData('mr_answ.keys',mr_answ.keys)
    mentalrot_trials.addData('mr_answ.corr', mr_answ.corr)
    if mr_answ.keys != None:  # we had a response
        mentalrot_trials.addData('mr_answ.rt', mr_answ.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'mentalrot_trials'


# --- Prepare to start Routine "finish_goodbye" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
finish_goodbyeComponents = [byebye_text]
for thisComponent in finish_goodbyeComponents:
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

# --- Run Routine "finish_goodbye" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *byebye_text* updates
    
    # if byebye_text is starting this frame...
    if byebye_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        byebye_text.frameNStart = frameN  # exact frame index
        byebye_text.tStart = t  # local t and not account for scr refresh
        byebye_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(byebye_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'byebye_text.started')
        # update status
        byebye_text.status = STARTED
        byebye_text.setAutoDraw(True)
    
    # if byebye_text is active this frame...
    if byebye_text.status == STARTED:
        # update params
        pass
    
    # if byebye_text is stopping this frame...
    if byebye_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > byebye_text.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            byebye_text.tStop = t  # not accounting for scr refresh
            byebye_text.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'byebye_text.stopped')
            # update status
            byebye_text.status = FINISHED
            byebye_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finish_goodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "finish_goodbye" ---
for thisComponent in finish_goodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.000000)

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
