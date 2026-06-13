#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on June 08, 2026, at 13:07
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
expName = 'SS'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\paper\\OneDrive\\Desktop\\PsychoPy\\masters_imagery\\spatial_span_nback_lastrun.py',
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

# --- Initialize components for Routine "instruction_1" ---
instr_text = visual.TextStim(win=win, name='instr_text',
    text='В этом задании на экране будет появляться точка, которая каждый раз перемещается в одно из нескольких возможных мест. Ваша задача — следить за расположением точки и запоминать последовательность её позиций.\n\nЧерез некоторое время вам нужно будет решать, совпадает ли текущее положение точки с положением, которое было несколько шагов назад. \n\nНапример:\nВ варианте "2-back" следует определить, находится ли точка в том же месте, что и два шага назад (позапрошлое);\nВ варианте "3-back" — то же самое, но с позицией три шага назад (позапозапрошлое);\nВ варианте "4-back" — с позицией четыре шага назад.\n\nНачинайте отвечать, когда точка становится красной. Отвечайте каждый раз, когда точка меняет положение.\n\nЕсли текущее положение не совпадает с тем, которое было указанное количество шагов назад, нажмите клавишу "←".\nЕсли совпадает — нажмите "→".\n\nСтарайтесь отвечать как можно быстрее и точнее. После короткой тренировки начнётся основная часть эксперимента.\nЕсли вы готовы начать тренировку, нажмите «пробел».',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instr_resp = keyboard.Keyboard()

# --- Initialize components for Routine "fix" ---
fix1 = visual.ShapeStim(
    win=win, name='fix1', vertices='cross',
    size=(0.08, 0.08),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "buffering_0_2" ---
buffer02_txt = visual.TextStim(win=win, name='buffer02_txt',
    text='с этого момента задачи:\n\n«два шага назад»\n\n(«то же место, что и позапрошлое?»)',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "fix" ---
fix1 = visual.ShapeStim(
    win=win, name='fix1', vertices='cross',
    size=(0.08, 0.08),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "test_2n" ---
test_griddot_resp2 = keyboard.Keyboard()
hint_no2 = visual.TextStim(win=win, name='hint_no2',
    text='нет\n←',
    font='Open Sans',
    pos=(-0.6, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
hint_quest2 = visual.TextStim(win=win, name='hint_quest2',
    text='как позапрошлая?',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
hint_yes2 = visual.TextStim(win=win, name='hint_yes2',
    text='да\n→',
    font='Open Sans',
    pos=(0.6, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "fix" ---
fix1 = visual.ShapeStim(
    win=win, name='fix1', vertices='cross',
    size=(0.08, 0.08),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "buffering_2_3" ---
buffer23_txt = visual.TextStim(win=win, name='buffer23_txt',
    text='с этого момента задачи\n\n«три шага назад»\n(«то же, что и позапозапрошлое?»)',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "fix" ---
fix1 = visual.ShapeStim(
    win=win, name='fix1', vertices='cross',
    size=(0.08, 0.08),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "test_3n" ---
test_griddot_resp3 = keyboard.Keyboard()
hint_no3 = visual.TextStim(win=win, name='hint_no3',
    text='нет\n←',
    font='Open Sans',
    pos=(-0.6, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
hint_quest3 = visual.TextStim(win=win, name='hint_quest3',
    text='как позапозапрошлая?',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
hint_yes3 = visual.TextStim(win=win, name='hint_yes3',
    text='да\n→',
    font='Open Sans',
    pos=(0.6, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "fix" ---
fix1 = visual.ShapeStim(
    win=win, name='fix1', vertices='cross',
    size=(0.08, 0.08),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "buffering_3_4" ---
buffer34_txt = visual.TextStim(win=win, name='buffer34_txt',
    text='с этого момента задачи\n\n«четыре шага назад»',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "fix" ---
fix1 = visual.ShapeStim(
    win=win, name='fix1', vertices='cross',
    size=(0.08, 0.08),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "test_4n" ---
test_griddot_resp4 = keyboard.Keyboard()
hint_no4 = visual.TextStim(win=win, name='hint_no4',
    text='нет\n←',
    font='Open Sans',
    pos=(-0.6, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
hint_yes4 = visual.TextStim(win=win, name='hint_yes4',
    text='да\n→',
    font='Open Sans',
    pos=(0.6, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
hint_quest4 = visual.TextStim(win=win, name='hint_quest4',
    text='как 4 шага назад?',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "test_confirm" ---
confirm_txt = visual.TextStim(win=win, name='confirm_txt',
    text='Понятен ли вам принцип задания?\n\nЕсли да и вы готовы начать основную часть, нажмите "Y"\nЕсли нет и вы хотите еще раз повторить тренировку, нажмите "N"',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
confirm_resp = keyboard.Keyboard()

# --- Initialize components for Routine "instruction_2" ---
instr_text_2 = visual.TextStim(win=win, name='instr_text_2',
    text='Тренировка закончилась.\n\nНапоминаем, что в этом задании на экране будет появляться точка, позиции которой нужно будет запоминать. Вам нужно будет решать, совпадает ли текущее положение точки с положением, которое было несколько шагов назад. Например:\n\nВ варианте «2-back» следует определить, находится ли точка в том же месте, что и два шага назад; «3-back» — то же самое, но с позицией три шага назад; «4-back» — с позицией четыре шага назад. \n\nОтвечайте, когда точка станет красной. \nЕсли текущее положение не совпадает с тем, что было указанное количество шагов назад, нажмите клавишу "←".\nЕсли совпадает — нажмите "→".\n\nСтарайтесь отвечать как можно быстрее и точнее. После короткой тренировки начнётся основная часть эксперимента.\n\nЕсли вы все поняли и готовы начинать основную часть эксперимента, нажмите "пробел".',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instr_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "buffering_0_2" ---
buffer02_txt = visual.TextStim(win=win, name='buffer02_txt',
    text='с этого момента задачи:\n\n«два шага назад»\n\n(«то же место, что и позапрошлое?»)',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "fix" ---
fix1 = visual.ShapeStim(
    win=win, name='fix1', vertices='cross',
    size=(0.08, 0.08),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "trial_2n" ---
griddot_resp2 = keyboard.Keyboard()

# --- Initialize components for Routine "timebreak" ---
timeout_txt = visual.TextStim(win=win, name='timeout_txt',
    text='когда вы будете готовы продолжить\n\nнажмите ПРОБЕЛ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
timeout_resp = keyboard.Keyboard()

# --- Initialize components for Routine "buffering_2_3" ---
buffer23_txt = visual.TextStim(win=win, name='buffer23_txt',
    text='с этого момента задачи\n\n«три шага назад»\n(«то же, что и позапозапрошлое?»)',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "fix" ---
fix1 = visual.ShapeStim(
    win=win, name='fix1', vertices='cross',
    size=(0.08, 0.08),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "trial_3n" ---
griddot_resp3 = keyboard.Keyboard()

# --- Initialize components for Routine "timebreak" ---
timeout_txt = visual.TextStim(win=win, name='timeout_txt',
    text='когда вы будете готовы продолжить\n\nнажмите ПРОБЕЛ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
timeout_resp = keyboard.Keyboard()

# --- Initialize components for Routine "buffering_3_4" ---
buffer34_txt = visual.TextStim(win=win, name='buffer34_txt',
    text='с этого момента задачи\n\n«четыре шага назад»',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "fix" ---
fix1 = visual.ShapeStim(
    win=win, name='fix1', vertices='cross',
    size=(0.08, 0.08),
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# --- Initialize components for Routine "trial_4n" ---
griddot_resp4 = keyboard.Keyboard()

# --- Initialize components for Routine "timebreak" ---
timeout_txt = visual.TextStim(win=win, name='timeout_txt',
    text='когда вы будете готовы продолжить\n\nнажмите ПРОБЕЛ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
timeout_resp = keyboard.Keyboard()

# --- Initialize components for Routine "goodbye" ---
bye_txt = visual.TextStim(win=win, name='bye_txt',
    text='Спасибо за участие!',
    font='Arial',
    units='norm', pos=(0, 0), height=0.1, wrapWidth=1.8, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instruction_1" ---
continueRoutine = True
# update component parameters for each repeat
instr_resp.keys = []
instr_resp.rt = []
_instr_resp_allKeys = []
# Run 'Begin Routine' code from begin_setup
import psychopy.core as core
# Initialize global clock
globalClock = core.Clock() 
Nloop = 0
# keep track of which components have finished
instruction_1Components = [instr_text, instr_resp]
for thisComponent in instruction_1Components:
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

# --- Run Routine "instruction_1" ---
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
    for thisComponent in instruction_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction_1" ---
for thisComponent in instruction_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
training_session = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='training_session')
thisExp.addLoop(training_session)  # add the loop to the experiment
thisTraining_session = training_session.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining_session.rgb)
if thisTraining_session != None:
    for paramName in thisTraining_session:
        exec('{} = thisTraining_session[paramName]'.format(paramName))

for thisTraining_session in training_session:
    currentLoop = training_session
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_session.rgb)
    if thisTraining_session != None:
        for paramName in thisTraining_session:
            exec('{} = thisTraining_session[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "fix" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [fix1]
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
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix1* updates
        
        # if fix1 is starting this frame...
        if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix1.frameNStart = frameN  # exact frame index
            fix1.tStart = t  # local t and not account for scr refresh
            fix1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
            # update status
            fix1.status = STARTED
            fix1.setAutoDraw(True)
        
        # if fix1 is active this frame...
        if fix1.status == STARTED:
            # update params
            pass
        
        # if fix1 is stopping this frame...
        if fix1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix1.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                fix1.tStop = t  # not accounting for scr refresh
                fix1.frameNStop = frameN  # exact frame index
                # update status
                fix1.status = FINISHED
                fix1.setAutoDraw(False)
        
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
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "buffering_0_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from countreset_2
    Nloop = 0
    # keep track of which components have finished
    buffering_0_2Components = [buffer02_txt]
    for thisComponent in buffering_0_2Components:
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
    
    # --- Run Routine "buffering_0_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *buffer02_txt* updates
        
        # if buffer02_txt is starting this frame...
        if buffer02_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buffer02_txt.frameNStart = frameN  # exact frame index
            buffer02_txt.tStart = t  # local t and not account for scr refresh
            buffer02_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buffer02_txt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'buffer02_txt.started')
            # update status
            buffer02_txt.status = STARTED
            buffer02_txt.setAutoDraw(True)
        
        # if buffer02_txt is active this frame...
        if buffer02_txt.status == STARTED:
            # update params
            pass
        
        # if buffer02_txt is stopping this frame...
        if buffer02_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > buffer02_txt.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                buffer02_txt.tStop = t  # not accounting for scr refresh
                buffer02_txt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'buffer02_txt.stopped')
                # update status
                buffer02_txt.status = FINISHED
                buffer02_txt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in buffering_0_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "buffering_0_2" ---
    for thisComponent in buffering_0_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # set up handler to look after randomisation of conditions etc
    training_2n = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('filtered_seq_single_column_2n.csv'),
        seed=None, name='training_2n')
    thisExp.addLoop(training_2n)  # add the loop to the experiment
    thisTraining_2n = training_2n.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_2n.rgb)
    if thisTraining_2n != None:
        for paramName in thisTraining_2n:
            exec('{} = thisTraining_2n[paramName]'.format(paramName))
    
    for thisTraining_2n in training_2n:
        currentLoop = training_2n
        # abbreviate parameter names if possible (e.g. rgb = thisTraining_2n.rgb)
        if thisTraining_2n != None:
            for paramName in thisTraining_2n:
                exec('{} = thisTraining_2n[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "fix" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        fixComponents = [fix1]
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
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix1* updates
            
            # if fix1 is starting this frame...
            if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix1.frameNStart = frameN  # exact frame index
                fix1.tStart = t  # local t and not account for scr refresh
                fix1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
                # update status
                fix1.status = STARTED
                fix1.setAutoDraw(True)
            
            # if fix1 is active this frame...
            if fix1.status == STARTED:
                # update params
                pass
            
            # if fix1 is stopping this frame...
            if fix1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    fix1.tStop = t  # not accounting for scr refresh
                    fix1.frameNStop = frameN  # exact frame index
                    # update status
                    fix1.status = FINISHED
                    fix1.setAutoDraw(False)
            
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
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "test_2n" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from test_griddot2
        # Define grid parameters
        n_rows = 3
        n_cols = 3
        grid_size = 0.65  # size in normalized units (0 to 1)
        cell_size = grid_size / n_rows
        
        # Create grid lines using Rect
        grid_lines = []
        for i in range(n_rows + 1):
            # Horizontal lines
            y = -grid_size/2 + i*cell_size
            line = visual.Rect(win, width=grid_size, height=0.01, pos=(0, y), fillColor='white', lineColor='white')
            grid_lines.append(line)
        
        for j in range(n_cols + 1):
            # Vertical lines
            x = -grid_size/2 + j*cell_size
            line = visual.Rect(win, width=0.01, height=grid_size, pos=(x, 0), fillColor='white', lineColor='white')
            grid_lines.append(line)
        
        # Create the dot
        dot = visual.Circle(win, radius=0.04, fillColor='red', lineColor='red')
        
        step_duration = 2  # seconds per step
        step_index = 0
        step_clock = core.Clock()
        
        if Nloop == 2:
            currentLoop.finished = True
        Nloop = Nloop+1
        test_griddot_resp2.keys = []
        test_griddot_resp2.rt = []
        _test_griddot_resp2_allKeys = []
        # keep track of which components have finished
        test_2nComponents = [test_griddot_resp2, hint_no2, hint_quest2, hint_yes2]
        for thisComponent in test_2nComponents:
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
        
        # --- Run Routine "test_2n" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 16.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from test_griddot2
            if step_index < len(sequence):
                row_index, col_index = sequence[step_index]
                dot.pos = (-grid_size/2 + (col_index + 0.5) * cell_size,
                           -grid_size/2 + (row_index + 0.5) * cell_size)
            
                # Set color for first two dots, else default to red
                if step_index < 2:
                    dot.fillColor = 'orange'
                    dot.lineColor = 'orange'
                else:
                    dot.fillColor = 'red'
                    dot.lineColor = 'red'
            
                for line in grid_lines:
                    line.draw()
            
                current_time = step_clock.getTime()
            
                # Draw dot only if within first 1.8 seconds of the step
                if current_time < 1.8:
                    dot.draw()
            
                if current_time >= step_duration:  # step_duration should be 2.0 seconds
                    step_clock.reset()
                    step_index += 1
            else:
                continueRoutine = False
            
            
            # *test_griddot_resp2* updates
            waitOnFlip = False
            
            # if test_griddot_resp2 is starting this frame...
            if test_griddot_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                test_griddot_resp2.frameNStart = frameN  # exact frame index
                test_griddot_resp2.tStart = t  # local t and not account for scr refresh
                test_griddot_resp2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(test_griddot_resp2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'test_griddot_resp2.started')
                # update status
                test_griddot_resp2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(test_griddot_resp2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(test_griddot_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if test_griddot_resp2 is stopping this frame...
            if test_griddot_resp2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > test_griddot_resp2.tStartRefresh + 16-frameTolerance:
                    # keep track of stop time/frame for later
                    test_griddot_resp2.tStop = t  # not accounting for scr refresh
                    test_griddot_resp2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'test_griddot_resp2.stopped')
                    # update status
                    test_griddot_resp2.status = FINISHED
                    test_griddot_resp2.status = FINISHED
            if test_griddot_resp2.status == STARTED and not waitOnFlip:
                theseKeys = test_griddot_resp2.getKeys(keyList=['left','right'], waitRelease=False)
                _test_griddot_resp2_allKeys.extend(theseKeys)
                if len(_test_griddot_resp2_allKeys):
                    test_griddot_resp2.keys = [key.name for key in _test_griddot_resp2_allKeys]  # storing all keys
                    test_griddot_resp2.rt = [key.rt for key in _test_griddot_resp2_allKeys]
            
            # *hint_no2* updates
            
            # if hint_no2 is starting this frame...
            if hint_no2.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
                # keep track of start time/frame for later
                hint_no2.frameNStart = frameN  # exact frame index
                hint_no2.tStart = t  # local t and not account for scr refresh
                hint_no2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hint_no2, 'tStartRefresh')  # time at next scr refresh
                # update status
                hint_no2.status = STARTED
                hint_no2.setAutoDraw(True)
            
            # if hint_no2 is active this frame...
            if hint_no2.status == STARTED:
                # update params
                pass
            
            # if hint_no2 is stopping this frame...
            if hint_no2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hint_no2.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    hint_no2.tStop = t  # not accounting for scr refresh
                    hint_no2.frameNStop = frameN  # exact frame index
                    # update status
                    hint_no2.status = FINISHED
                    hint_no2.setAutoDraw(False)
            
            # *hint_quest2* updates
            
            # if hint_quest2 is starting this frame...
            if hint_quest2.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
                # keep track of start time/frame for later
                hint_quest2.frameNStart = frameN  # exact frame index
                hint_quest2.tStart = t  # local t and not account for scr refresh
                hint_quest2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hint_quest2, 'tStartRefresh')  # time at next scr refresh
                # update status
                hint_quest2.status = STARTED
                hint_quest2.setAutoDraw(True)
            
            # if hint_quest2 is active this frame...
            if hint_quest2.status == STARTED:
                # update params
                pass
            
            # if hint_quest2 is stopping this frame...
            if hint_quest2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hint_quest2.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    hint_quest2.tStop = t  # not accounting for scr refresh
                    hint_quest2.frameNStop = frameN  # exact frame index
                    # update status
                    hint_quest2.status = FINISHED
                    hint_quest2.setAutoDraw(False)
            
            # *hint_yes2* updates
            
            # if hint_yes2 is starting this frame...
            if hint_yes2.status == NOT_STARTED and tThisFlip >= 4.0-frameTolerance:
                # keep track of start time/frame for later
                hint_yes2.frameNStart = frameN  # exact frame index
                hint_yes2.tStart = t  # local t and not account for scr refresh
                hint_yes2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hint_yes2, 'tStartRefresh')  # time at next scr refresh
                # update status
                hint_yes2.status = STARTED
                hint_yes2.setAutoDraw(True)
            
            # if hint_yes2 is active this frame...
            if hint_yes2.status == STARTED:
                # update params
                pass
            
            # if hint_yes2 is stopping this frame...
            if hint_yes2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hint_yes2.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    hint_yes2.tStop = t  # not accounting for scr refresh
                    hint_yes2.frameNStop = frameN  # exact frame index
                    # update status
                    hint_yes2.status = FINISHED
                    hint_yes2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test_2nComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test_2n" ---
        for thisComponent in test_2nComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if test_griddot_resp2.keys in ['', [], None]:  # No response was made
            test_griddot_resp2.keys = None
        training_2n.addData('test_griddot_resp2.keys',test_griddot_resp2.keys)
        if test_griddot_resp2.keys != None:  # we had a response
            training_2n.addData('test_griddot_resp2.rt', test_griddot_resp2.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-16.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'training_2n'
    
    
    # --- Prepare to start Routine "fix" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [fix1]
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
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix1* updates
        
        # if fix1 is starting this frame...
        if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix1.frameNStart = frameN  # exact frame index
            fix1.tStart = t  # local t and not account for scr refresh
            fix1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
            # update status
            fix1.status = STARTED
            fix1.setAutoDraw(True)
        
        # if fix1 is active this frame...
        if fix1.status == STARTED:
            # update params
            pass
        
        # if fix1 is stopping this frame...
        if fix1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix1.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                fix1.tStop = t  # not accounting for scr refresh
                fix1.frameNStop = frameN  # exact frame index
                # update status
                fix1.status = FINISHED
                fix1.setAutoDraw(False)
        
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
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "buffering_2_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from countreset_3
    Nloop = 0
    # keep track of which components have finished
    buffering_2_3Components = [buffer23_txt]
    for thisComponent in buffering_2_3Components:
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
    
    # --- Run Routine "buffering_2_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *buffer23_txt* updates
        
        # if buffer23_txt is starting this frame...
        if buffer23_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buffer23_txt.frameNStart = frameN  # exact frame index
            buffer23_txt.tStart = t  # local t and not account for scr refresh
            buffer23_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buffer23_txt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'buffer23_txt.started')
            # update status
            buffer23_txt.status = STARTED
            buffer23_txt.setAutoDraw(True)
        
        # if buffer23_txt is active this frame...
        if buffer23_txt.status == STARTED:
            # update params
            pass
        
        # if buffer23_txt is stopping this frame...
        if buffer23_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > buffer23_txt.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                buffer23_txt.tStop = t  # not accounting for scr refresh
                buffer23_txt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'buffer23_txt.stopped')
                # update status
                buffer23_txt.status = FINISHED
                buffer23_txt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in buffering_2_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "buffering_2_3" ---
    for thisComponent in buffering_2_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # set up handler to look after randomisation of conditions etc
    training_3n = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('filtered_seq_single_column_3n.csv'),
        seed=None, name='training_3n')
    thisExp.addLoop(training_3n)  # add the loop to the experiment
    thisTraining_3n = training_3n.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_3n.rgb)
    if thisTraining_3n != None:
        for paramName in thisTraining_3n:
            exec('{} = thisTraining_3n[paramName]'.format(paramName))
    
    for thisTraining_3n in training_3n:
        currentLoop = training_3n
        # abbreviate parameter names if possible (e.g. rgb = thisTraining_3n.rgb)
        if thisTraining_3n != None:
            for paramName in thisTraining_3n:
                exec('{} = thisTraining_3n[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "fix" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        fixComponents = [fix1]
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
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix1* updates
            
            # if fix1 is starting this frame...
            if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix1.frameNStart = frameN  # exact frame index
                fix1.tStart = t  # local t and not account for scr refresh
                fix1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
                # update status
                fix1.status = STARTED
                fix1.setAutoDraw(True)
            
            # if fix1 is active this frame...
            if fix1.status == STARTED:
                # update params
                pass
            
            # if fix1 is stopping this frame...
            if fix1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    fix1.tStop = t  # not accounting for scr refresh
                    fix1.frameNStop = frameN  # exact frame index
                    # update status
                    fix1.status = FINISHED
                    fix1.setAutoDraw(False)
            
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
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "test_3n" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from test_griddot3
        # Define grid parameters
        n_rows = 3
        n_cols = 3
        grid_size = 0.65  # size in normalized units (0 to 1)
        cell_size = grid_size / n_rows
        
        # Create grid lines using Rect
        grid_lines = []
        for i in range(n_rows + 1):
            # Horizontal lines
            y = -grid_size/2 + i*cell_size
            line = visual.Rect(win, width=grid_size, height=0.01, pos=(0, y), fillColor='white', lineColor='white')
            grid_lines.append(line)
        
        for j in range(n_cols + 1):
            # Vertical lines
            x = -grid_size/2 + j*cell_size
            line = visual.Rect(win, width=0.01, height=grid_size, pos=(x, 0), fillColor='white', lineColor='white')
            grid_lines.append(line)
        
        # Create the dot
        dot = visual.Circle(win, radius=0.04, fillColor='red', lineColor='red')
        
        step_duration = 2  # seconds per step
        step_index = 0
        step_clock = core.Clock()
        
        if Nloop == 2:
            currentLoop.finished = True
        Nloop = Nloop+1
        test_griddot_resp3.keys = []
        test_griddot_resp3.rt = []
        _test_griddot_resp3_allKeys = []
        # keep track of which components have finished
        test_3nComponents = [test_griddot_resp3, hint_no3, hint_quest3, hint_yes3]
        for thisComponent in test_3nComponents:
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
        
        # --- Run Routine "test_3n" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 18.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from test_griddot3
            if step_index < len(sequence):
                row_index, col_index = sequence[step_index]
                dot.pos = (-grid_size/2 + (col_index + 0.5) * cell_size,
                           -grid_size/2 + (row_index + 0.5) * cell_size)
            
                # Set color for first two dots, else default to red
                if step_index < 3:
                    dot.fillColor = 'purple'
                    dot.lineColor = 'purple'
                else:
                    dot.fillColor = 'red'
                    dot.lineColor = 'red'
            
                for line in grid_lines:
                    line.draw()
            
                current_time = step_clock.getTime()
            
                # Draw dot only if within first 1.8 seconds of the step
                if current_time < 1.8:
                    dot.draw()
            
                if current_time >= step_duration:  # step_duration should be 2.0 seconds
                    step_clock.reset()
                    step_index += 1
            else:
                continueRoutine = False
            
            
            # *test_griddot_resp3* updates
            waitOnFlip = False
            
            # if test_griddot_resp3 is starting this frame...
            if test_griddot_resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                test_griddot_resp3.frameNStart = frameN  # exact frame index
                test_griddot_resp3.tStart = t  # local t and not account for scr refresh
                test_griddot_resp3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(test_griddot_resp3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'test_griddot_resp3.started')
                # update status
                test_griddot_resp3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(test_griddot_resp3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(test_griddot_resp3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if test_griddot_resp3 is stopping this frame...
            if test_griddot_resp3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > test_griddot_resp3.tStartRefresh + 18-frameTolerance:
                    # keep track of stop time/frame for later
                    test_griddot_resp3.tStop = t  # not accounting for scr refresh
                    test_griddot_resp3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'test_griddot_resp3.stopped')
                    # update status
                    test_griddot_resp3.status = FINISHED
                    test_griddot_resp3.status = FINISHED
            if test_griddot_resp3.status == STARTED and not waitOnFlip:
                theseKeys = test_griddot_resp3.getKeys(keyList=['left','right'], waitRelease=False)
                _test_griddot_resp3_allKeys.extend(theseKeys)
                if len(_test_griddot_resp3_allKeys):
                    test_griddot_resp3.keys = [key.name for key in _test_griddot_resp3_allKeys]  # storing all keys
                    test_griddot_resp3.rt = [key.rt for key in _test_griddot_resp3_allKeys]
            
            # *hint_no3* updates
            
            # if hint_no3 is starting this frame...
            if hint_no3.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
                # keep track of start time/frame for later
                hint_no3.frameNStart = frameN  # exact frame index
                hint_no3.tStart = t  # local t and not account for scr refresh
                hint_no3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hint_no3, 'tStartRefresh')  # time at next scr refresh
                # update status
                hint_no3.status = STARTED
                hint_no3.setAutoDraw(True)
            
            # if hint_no3 is active this frame...
            if hint_no3.status == STARTED:
                # update params
                pass
            
            # if hint_no3 is stopping this frame...
            if hint_no3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hint_no3.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    hint_no3.tStop = t  # not accounting for scr refresh
                    hint_no3.frameNStop = frameN  # exact frame index
                    # update status
                    hint_no3.status = FINISHED
                    hint_no3.setAutoDraw(False)
            
            # *hint_quest3* updates
            
            # if hint_quest3 is starting this frame...
            if hint_quest3.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
                # keep track of start time/frame for later
                hint_quest3.frameNStart = frameN  # exact frame index
                hint_quest3.tStart = t  # local t and not account for scr refresh
                hint_quest3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hint_quest3, 'tStartRefresh')  # time at next scr refresh
                # update status
                hint_quest3.status = STARTED
                hint_quest3.setAutoDraw(True)
            
            # if hint_quest3 is active this frame...
            if hint_quest3.status == STARTED:
                # update params
                pass
            
            # if hint_quest3 is stopping this frame...
            if hint_quest3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hint_quest3.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    hint_quest3.tStop = t  # not accounting for scr refresh
                    hint_quest3.frameNStop = frameN  # exact frame index
                    # update status
                    hint_quest3.status = FINISHED
                    hint_quest3.setAutoDraw(False)
            
            # *hint_yes3* updates
            
            # if hint_yes3 is starting this frame...
            if hint_yes3.status == NOT_STARTED and tThisFlip >= 6.0-frameTolerance:
                # keep track of start time/frame for later
                hint_yes3.frameNStart = frameN  # exact frame index
                hint_yes3.tStart = t  # local t and not account for scr refresh
                hint_yes3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hint_yes3, 'tStartRefresh')  # time at next scr refresh
                # update status
                hint_yes3.status = STARTED
                hint_yes3.setAutoDraw(True)
            
            # if hint_yes3 is active this frame...
            if hint_yes3.status == STARTED:
                # update params
                pass
            
            # if hint_yes3 is stopping this frame...
            if hint_yes3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hint_yes3.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    hint_yes3.tStop = t  # not accounting for scr refresh
                    hint_yes3.frameNStop = frameN  # exact frame index
                    # update status
                    hint_yes3.status = FINISHED
                    hint_yes3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test_3nComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test_3n" ---
        for thisComponent in test_3nComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if test_griddot_resp3.keys in ['', [], None]:  # No response was made
            test_griddot_resp3.keys = None
        training_3n.addData('test_griddot_resp3.keys',test_griddot_resp3.keys)
        if test_griddot_resp3.keys != None:  # we had a response
            training_3n.addData('test_griddot_resp3.rt', test_griddot_resp3.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-18.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'training_3n'
    
    
    # --- Prepare to start Routine "fix" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [fix1]
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
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fix1* updates
        
        # if fix1 is starting this frame...
        if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fix1.frameNStart = frameN  # exact frame index
            fix1.tStart = t  # local t and not account for scr refresh
            fix1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
            # update status
            fix1.status = STARTED
            fix1.setAutoDraw(True)
        
        # if fix1 is active this frame...
        if fix1.status == STARTED:
            # update params
            pass
        
        # if fix1 is stopping this frame...
        if fix1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fix1.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                fix1.tStop = t  # not accounting for scr refresh
                fix1.frameNStop = frameN  # exact frame index
                # update status
                fix1.status = FINISHED
                fix1.setAutoDraw(False)
        
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
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "buffering_3_4" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from countreset_4
    Nloop = 0
    # keep track of which components have finished
    buffering_3_4Components = [buffer34_txt]
    for thisComponent in buffering_3_4Components:
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
    
    # --- Run Routine "buffering_3_4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *buffer34_txt* updates
        
        # if buffer34_txt is starting this frame...
        if buffer34_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            buffer34_txt.frameNStart = frameN  # exact frame index
            buffer34_txt.tStart = t  # local t and not account for scr refresh
            buffer34_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(buffer34_txt, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'buffer34_txt.started')
            # update status
            buffer34_txt.status = STARTED
            buffer34_txt.setAutoDraw(True)
        
        # if buffer34_txt is active this frame...
        if buffer34_txt.status == STARTED:
            # update params
            pass
        
        # if buffer34_txt is stopping this frame...
        if buffer34_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > buffer34_txt.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                buffer34_txt.tStop = t  # not accounting for scr refresh
                buffer34_txt.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'buffer34_txt.stopped')
                # update status
                buffer34_txt.status = FINISHED
                buffer34_txt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in buffering_3_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "buffering_3_4" ---
    for thisComponent in buffering_3_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # set up handler to look after randomisation of conditions etc
    training_4n = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('filtered_seq_single_column_4n.csv'),
        seed=None, name='training_4n')
    thisExp.addLoop(training_4n)  # add the loop to the experiment
    thisTraining_4n = training_4n.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_4n.rgb)
    if thisTraining_4n != None:
        for paramName in thisTraining_4n:
            exec('{} = thisTraining_4n[paramName]'.format(paramName))
    
    for thisTraining_4n in training_4n:
        currentLoop = training_4n
        # abbreviate parameter names if possible (e.g. rgb = thisTraining_4n.rgb)
        if thisTraining_4n != None:
            for paramName in thisTraining_4n:
                exec('{} = thisTraining_4n[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "fix" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        fixComponents = [fix1]
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
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix1* updates
            
            # if fix1 is starting this frame...
            if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix1.frameNStart = frameN  # exact frame index
                fix1.tStart = t  # local t and not account for scr refresh
                fix1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
                # update status
                fix1.status = STARTED
                fix1.setAutoDraw(True)
            
            # if fix1 is active this frame...
            if fix1.status == STARTED:
                # update params
                pass
            
            # if fix1 is stopping this frame...
            if fix1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    fix1.tStop = t  # not accounting for scr refresh
                    fix1.frameNStop = frameN  # exact frame index
                    # update status
                    fix1.status = FINISHED
                    fix1.setAutoDraw(False)
            
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
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "test_4n" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from test_griddot4
        # Define grid parameters
        n_rows = 3
        n_cols = 3
        grid_size = 0.65  # size in normalized units (0 to 1)
        cell_size = grid_size / n_rows
        
        # Create grid lines using Rect
        grid_lines = []
        for i in range(n_rows + 1):
            # Horizontal lines
            y = -grid_size/2 + i*cell_size
            line = visual.Rect(win, width=grid_size, height=0.01, pos=(0, y), fillColor='white', lineColor='white')
            grid_lines.append(line)
        
        for j in range(n_cols + 1):
            # Vertical lines
            x = -grid_size/2 + j*cell_size
            line = visual.Rect(win, width=0.01, height=grid_size, pos=(x, 0), fillColor='white', lineColor='white')
            grid_lines.append(line)
        
        # Create the dot
        dot = visual.Circle(win, radius=0.04, fillColor='red', lineColor='red')
        
        step_duration = 2  # seconds per step
        step_index = 0
        step_clock = core.Clock()
        
        if Nloop == 2:
            currentLoop.finished = True
        Nloop = Nloop+1
        test_griddot_resp4.keys = []
        test_griddot_resp4.rt = []
        _test_griddot_resp4_allKeys = []
        # keep track of which components have finished
        test_4nComponents = [test_griddot_resp4, hint_no4, hint_yes4, hint_quest4]
        for thisComponent in test_4nComponents:
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
        
        # --- Run Routine "test_4n" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 20.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from test_griddot4
            if step_index < len(sequence):
                row_index, col_index = sequence[step_index]
                dot.pos = (-grid_size/2 + (col_index + 0.5) * cell_size,
                           -grid_size/2 + (row_index + 0.5) * cell_size)
            
                # Set color for first two dots, else default to red
                if step_index < 4:
                    dot.fillColor = 'yellow'
                    dot.lineColor = 'yellow'
                else:
                    dot.fillColor = 'red'
                    dot.lineColor = 'red'
            
                for line in grid_lines:
                    line.draw()
            
                current_time = step_clock.getTime()
            
                # Draw dot only if within first 1.8 seconds of the step
                if current_time < 1.8:
                    dot.draw()
            
                if current_time >= step_duration:  # step_duration should be 2.0 seconds
                    step_clock.reset()
                    step_index += 1
            else:
                continueRoutine = False
            
            
            # *test_griddot_resp4* updates
            waitOnFlip = False
            
            # if test_griddot_resp4 is starting this frame...
            if test_griddot_resp4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                test_griddot_resp4.frameNStart = frameN  # exact frame index
                test_griddot_resp4.tStart = t  # local t and not account for scr refresh
                test_griddot_resp4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(test_griddot_resp4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'test_griddot_resp4.started')
                # update status
                test_griddot_resp4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(test_griddot_resp4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(test_griddot_resp4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if test_griddot_resp4 is stopping this frame...
            if test_griddot_resp4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > test_griddot_resp4.tStartRefresh + 20-frameTolerance:
                    # keep track of stop time/frame for later
                    test_griddot_resp4.tStop = t  # not accounting for scr refresh
                    test_griddot_resp4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'test_griddot_resp4.stopped')
                    # update status
                    test_griddot_resp4.status = FINISHED
                    test_griddot_resp4.status = FINISHED
            if test_griddot_resp4.status == STARTED and not waitOnFlip:
                theseKeys = test_griddot_resp4.getKeys(keyList=['left','right'], waitRelease=False)
                _test_griddot_resp4_allKeys.extend(theseKeys)
                if len(_test_griddot_resp4_allKeys):
                    test_griddot_resp4.keys = [key.name for key in _test_griddot_resp4_allKeys]  # storing all keys
                    test_griddot_resp4.rt = [key.rt for key in _test_griddot_resp4_allKeys]
            
            # *hint_no4* updates
            
            # if hint_no4 is starting this frame...
            if hint_no4.status == NOT_STARTED and tThisFlip >= 8.0-frameTolerance:
                # keep track of start time/frame for later
                hint_no4.frameNStart = frameN  # exact frame index
                hint_no4.tStart = t  # local t and not account for scr refresh
                hint_no4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hint_no4, 'tStartRefresh')  # time at next scr refresh
                # update status
                hint_no4.status = STARTED
                hint_no4.setAutoDraw(True)
            
            # if hint_no4 is active this frame...
            if hint_no4.status == STARTED:
                # update params
                pass
            
            # if hint_no4 is stopping this frame...
            if hint_no4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hint_no4.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    hint_no4.tStop = t  # not accounting for scr refresh
                    hint_no4.frameNStop = frameN  # exact frame index
                    # update status
                    hint_no4.status = FINISHED
                    hint_no4.setAutoDraw(False)
            
            # *hint_yes4* updates
            
            # if hint_yes4 is starting this frame...
            if hint_yes4.status == NOT_STARTED and tThisFlip >= 8.0-frameTolerance:
                # keep track of start time/frame for later
                hint_yes4.frameNStart = frameN  # exact frame index
                hint_yes4.tStart = t  # local t and not account for scr refresh
                hint_yes4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hint_yes4, 'tStartRefresh')  # time at next scr refresh
                # update status
                hint_yes4.status = STARTED
                hint_yes4.setAutoDraw(True)
            
            # if hint_yes4 is active this frame...
            if hint_yes4.status == STARTED:
                # update params
                pass
            
            # if hint_yes4 is stopping this frame...
            if hint_yes4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hint_yes4.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    hint_yes4.tStop = t  # not accounting for scr refresh
                    hint_yes4.frameNStop = frameN  # exact frame index
                    # update status
                    hint_yes4.status = FINISHED
                    hint_yes4.setAutoDraw(False)
            
            # *hint_quest4* updates
            
            # if hint_quest4 is starting this frame...
            if hint_quest4.status == NOT_STARTED and tThisFlip >= 8.0-frameTolerance:
                # keep track of start time/frame for later
                hint_quest4.frameNStart = frameN  # exact frame index
                hint_quest4.tStart = t  # local t and not account for scr refresh
                hint_quest4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hint_quest4, 'tStartRefresh')  # time at next scr refresh
                # update status
                hint_quest4.status = STARTED
                hint_quest4.setAutoDraw(True)
            
            # if hint_quest4 is active this frame...
            if hint_quest4.status == STARTED:
                # update params
                pass
            
            # if hint_quest4 is stopping this frame...
            if hint_quest4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hint_quest4.tStartRefresh + 12-frameTolerance:
                    # keep track of stop time/frame for later
                    hint_quest4.tStop = t  # not accounting for scr refresh
                    hint_quest4.frameNStop = frameN  # exact frame index
                    # update status
                    hint_quest4.status = FINISHED
                    hint_quest4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in test_4nComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "test_4n" ---
        for thisComponent in test_4nComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if test_griddot_resp4.keys in ['', [], None]:  # No response was made
            test_griddot_resp4.keys = None
        training_4n.addData('test_griddot_resp4.keys',test_griddot_resp4.keys)
        if test_griddot_resp4.keys != None:  # we had a response
            training_4n.addData('test_griddot_resp4.rt', test_griddot_resp4.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-20.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'training_4n'
    
    
    # --- Prepare to start Routine "test_confirm" ---
    continueRoutine = True
    # update component parameters for each repeat
    confirm_resp.keys = []
    confirm_resp.rt = []
    _confirm_resp_allKeys = []
    # keep track of which components have finished
    test_confirmComponents = [confirm_txt, confirm_resp]
    for thisComponent in test_confirmComponents:
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
    
    # --- Run Routine "test_confirm" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *confirm_txt* updates
        
        # if confirm_txt is starting this frame...
        if confirm_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            confirm_txt.frameNStart = frameN  # exact frame index
            confirm_txt.tStart = t  # local t and not account for scr refresh
            confirm_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirm_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            confirm_txt.status = STARTED
            confirm_txt.setAutoDraw(True)
        
        # if confirm_txt is active this frame...
        if confirm_txt.status == STARTED:
            # update params
            pass
        
        # *confirm_resp* updates
        waitOnFlip = False
        
        # if confirm_resp is starting this frame...
        if confirm_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            confirm_resp.frameNStart = frameN  # exact frame index
            confirm_resp.tStart = t  # local t and not account for scr refresh
            confirm_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(confirm_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'confirm_resp.started')
            # update status
            confirm_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(confirm_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(confirm_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if confirm_resp.status == STARTED and not waitOnFlip:
            theseKeys = confirm_resp.getKeys(keyList=['y','n'], waitRelease=False)
            _confirm_resp_allKeys.extend(theseKeys)
            if len(_confirm_resp_allKeys):
                confirm_resp.keys = _confirm_resp_allKeys[-1].name  # just the last key pressed
                confirm_resp.rt = _confirm_resp_allKeys[-1].rt
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
        for thisComponent in test_confirmComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "test_confirm" ---
    for thisComponent in test_confirmComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if confirm_resp.keys in ['', [], None]:  # No response was made
        confirm_resp.keys = None
    training_session.addData('confirm_resp.keys',confirm_resp.keys)
    if confirm_resp.keys != None:  # we had a response
        training_session.addData('confirm_resp.rt', confirm_resp.rt)
    # Run 'End Routine' code from confirm_cond
    if 'y' in confirm_resp.keys:
        training_session.finished = True
    # the Routine "test_confirm" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'training_session'


# --- Prepare to start Routine "instruction_2" ---
continueRoutine = True
# update component parameters for each repeat
instr_resp_2.keys = []
instr_resp_2.rt = []
_instr_resp_2_allKeys = []
# Run 'Begin Routine' code from begin_setup_2
import psychopy.core as core

Nloop = 0
# keep track of which components have finished
instruction_2Components = [instr_text_2, instr_resp_2]
for thisComponent in instruction_2Components:
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

# --- Run Routine "instruction_2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_text_2* updates
    
    # if instr_text_2 is starting this frame...
    if instr_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_text_2.frameNStart = frameN  # exact frame index
        instr_text_2.tStart = t  # local t and not account for scr refresh
        instr_text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instr_text_2.started')
        # update status
        instr_text_2.status = STARTED
        instr_text_2.setAutoDraw(True)
    
    # if instr_text_2 is active this frame...
    if instr_text_2.status == STARTED:
        # update params
        pass
    
    # *instr_resp_2* updates
    waitOnFlip = False
    
    # if instr_resp_2 is starting this frame...
    if instr_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_resp_2.frameNStart = frameN  # exact frame index
        instr_resp_2.tStart = t  # local t and not account for scr refresh
        instr_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_resp_2, 'tStartRefresh')  # time at next scr refresh
        # update status
        instr_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instr_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instr_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instr_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = instr_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _instr_resp_2_allKeys.extend(theseKeys)
        if len(_instr_resp_2_allKeys):
            instr_resp_2.keys = _instr_resp_2_allKeys[-1].name  # just the last key pressed
            instr_resp_2.rt = _instr_resp_2_allKeys[-1].rt
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
    for thisComponent in instruction_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instruction_2" ---
for thisComponent in instruction_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruction_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "buffering_0_2" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from countreset_2
Nloop = 0
# keep track of which components have finished
buffering_0_2Components = [buffer02_txt]
for thisComponent in buffering_0_2Components:
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

# --- Run Routine "buffering_0_2" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *buffer02_txt* updates
    
    # if buffer02_txt is starting this frame...
    if buffer02_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buffer02_txt.frameNStart = frameN  # exact frame index
        buffer02_txt.tStart = t  # local t and not account for scr refresh
        buffer02_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buffer02_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'buffer02_txt.started')
        # update status
        buffer02_txt.status = STARTED
        buffer02_txt.setAutoDraw(True)
    
    # if buffer02_txt is active this frame...
    if buffer02_txt.status == STARTED:
        # update params
        pass
    
    # if buffer02_txt is stopping this frame...
    if buffer02_txt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > buffer02_txt.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            buffer02_txt.tStop = t  # not accounting for scr refresh
            buffer02_txt.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'buffer02_txt.stopped')
            # update status
            buffer02_txt.status = FINISHED
            buffer02_txt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in buffering_0_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "buffering_0_2" ---
for thisComponent in buffering_0_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# set up handler to look after randomisation of conditions etc
allrep_2nback = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='allrep_2nback')
thisExp.addLoop(allrep_2nback)  # add the loop to the experiment
thisAllrep_2nback = allrep_2nback.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAllrep_2nback.rgb)
if thisAllrep_2nback != None:
    for paramName in thisAllrep_2nback:
        exec('{} = thisAllrep_2nback[paramName]'.format(paramName))

for thisAllrep_2nback in allrep_2nback:
    currentLoop = allrep_2nback
    # abbreviate parameter names if possible (e.g. rgb = thisAllrep_2nback.rgb)
    if thisAllrep_2nback != None:
        for paramName in thisAllrep_2nback:
            exec('{} = thisAllrep_2nback[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_2nback = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('filtered_seq_single_column_2n.csv'),
        seed=None, name='trials_2nback')
    thisExp.addLoop(trials_2nback)  # add the loop to the experiment
    thisTrials_2nback = trials_2nback.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_2nback.rgb)
    if thisTrials_2nback != None:
        for paramName in thisTrials_2nback:
            exec('{} = thisTrials_2nback[paramName]'.format(paramName))
    
    for thisTrials_2nback in trials_2nback:
        currentLoop = trials_2nback
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_2nback.rgb)
        if thisTrials_2nback != None:
            for paramName in thisTrials_2nback:
                exec('{} = thisTrials_2nback[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "fix" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        fixComponents = [fix1]
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
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix1* updates
            
            # if fix1 is starting this frame...
            if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix1.frameNStart = frameN  # exact frame index
                fix1.tStart = t  # local t and not account for scr refresh
                fix1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
                # update status
                fix1.status = STARTED
                fix1.setAutoDraw(True)
            
            # if fix1 is active this frame...
            if fix1.status == STARTED:
                # update params
                pass
            
            # if fix1 is stopping this frame...
            if fix1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    fix1.tStop = t  # not accounting for scr refresh
                    fix1.frameNStop = frameN  # exact frame index
                    # update status
                    fix1.status = FINISHED
                    fix1.setAutoDraw(False)
            
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
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "trial_2n" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from griddot2
        # Define grid parameters
        n_rows = 3
        n_cols = 3
        grid_size = 0.65  # size in normalized units (0 to 1)
        cell_size = grid_size / n_rows
        
        # Create grid lines using Rect
        grid_lines = []
        for i in range(n_rows + 1):
            # Horizontal lines
            y = -grid_size/2 + i*cell_size
            line = visual.Rect(win, width=grid_size, height=0.01, pos=(0, y), fillColor='white', lineColor='white')
            grid_lines.append(line)
        
        for j in range(n_cols + 1):
            # Vertical lines
            x = -grid_size/2 + j*cell_size
            line = visual.Rect(win, width=0.01, height=grid_size, pos=(x, 0), fillColor='white', lineColor='white')
            grid_lines.append(line)
        
        # Create the dot
        dot = visual.Circle(win, radius=0.04, fillColor='red', lineColor='red')
        
        step_duration = 2  # seconds per step
        step_index = 0
        step_clock = core.Clock()
        
        if Nloop == 5:
            currentLoop.finished = True
        Nloop = Nloop+1
        griddot_resp2.keys = []
        griddot_resp2.rt = []
        _griddot_resp2_allKeys = []
        # keep track of which components have finished
        trial_2nComponents = [griddot_resp2]
        for thisComponent in trial_2nComponents:
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
        
        # --- Run Routine "trial_2n" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 16.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from griddot2
            if step_index < len(sequence):
                row_index, col_index = sequence[step_index]
                dot.pos = (-grid_size/2 + (col_index + 0.5) * cell_size,
                           -grid_size/2 + (row_index + 0.5) * cell_size)
            
                # Set color for first two dots, else default to red
                if step_index < 2:
                    dot.fillColor = 'orange'
                    dot.lineColor = 'orange'
                else:
                    dot.fillColor = 'red'
                    dot.lineColor = 'red'
            
                for line in grid_lines:
                    line.draw()
            
                current_time = step_clock.getTime()
            
                # Draw dot only if within first 1.8 seconds of the step
                if current_time < 1.8:
                    dot.draw()
            
                if current_time >= step_duration:  # step_duration should be 2.0 seconds
                    step_clock.reset()
                    step_index += 1
            else:
                continueRoutine = False
            
            
            # *griddot_resp2* updates
            waitOnFlip = False
            
            # if griddot_resp2 is starting this frame...
            if griddot_resp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                griddot_resp2.frameNStart = frameN  # exact frame index
                griddot_resp2.tStart = t  # local t and not account for scr refresh
                griddot_resp2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(griddot_resp2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'griddot_resp2.started')
                # update status
                griddot_resp2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(griddot_resp2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(griddot_resp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if griddot_resp2 is stopping this frame...
            if griddot_resp2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > griddot_resp2.tStartRefresh + 16-frameTolerance:
                    # keep track of stop time/frame for later
                    griddot_resp2.tStop = t  # not accounting for scr refresh
                    griddot_resp2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'griddot_resp2.stopped')
                    # update status
                    griddot_resp2.status = FINISHED
                    griddot_resp2.status = FINISHED
            if griddot_resp2.status == STARTED and not waitOnFlip:
                theseKeys = griddot_resp2.getKeys(keyList=['left','right'], waitRelease=False)
                _griddot_resp2_allKeys.extend(theseKeys)
                if len(_griddot_resp2_allKeys):
                    griddot_resp2.keys = [key.name for key in _griddot_resp2_allKeys]  # storing all keys
                    griddot_resp2.rt = [key.rt for key in _griddot_resp2_allKeys]
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_2nComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_2n" ---
        for thisComponent in trial_2nComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if griddot_resp2.keys in ['', [], None]:  # No response was made
            griddot_resp2.keys = None
        trials_2nback.addData('griddot_resp2.keys',griddot_resp2.keys)
        if griddot_resp2.keys != None:  # we had a response
            trials_2nback.addData('griddot_resp2.rt', griddot_resp2.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-16.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_2nback'
    
    
    # --- Prepare to start Routine "timebreak" ---
    continueRoutine = True
    # update component parameters for each repeat
    timeout_resp.keys = []
    timeout_resp.rt = []
    _timeout_resp_allKeys = []
    # Run 'Begin Routine' code from countreset
    Nloop = 0
    # keep track of which components have finished
    timebreakComponents = [timeout_txt, timeout_resp]
    for thisComponent in timebreakComponents:
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
    
    # --- Run Routine "timebreak" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *timeout_txt* updates
        
        # if timeout_txt is starting this frame...
        if timeout_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timeout_txt.frameNStart = frameN  # exact frame index
            timeout_txt.tStart = t  # local t and not account for scr refresh
            timeout_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timeout_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            timeout_txt.status = STARTED
            timeout_txt.setAutoDraw(True)
        
        # if timeout_txt is active this frame...
        if timeout_txt.status == STARTED:
            # update params
            pass
        
        # *timeout_resp* updates
        waitOnFlip = False
        
        # if timeout_resp is starting this frame...
        if timeout_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timeout_resp.frameNStart = frameN  # exact frame index
            timeout_resp.tStart = t  # local t and not account for scr refresh
            timeout_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timeout_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            timeout_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(timeout_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(timeout_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if timeout_resp.status == STARTED and not waitOnFlip:
            theseKeys = timeout_resp.getKeys(keyList=['space'], waitRelease=False)
            _timeout_resp_allKeys.extend(theseKeys)
            if len(_timeout_resp_allKeys):
                timeout_resp.keys = _timeout_resp_allKeys[-1].name  # just the last key pressed
                timeout_resp.rt = _timeout_resp_allKeys[-1].rt
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
        for thisComponent in timebreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "timebreak" ---
    for thisComponent in timebreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "timebreak" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'allrep_2nback'


# --- Prepare to start Routine "buffering_2_3" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from countreset_3
Nloop = 0
# keep track of which components have finished
buffering_2_3Components = [buffer23_txt]
for thisComponent in buffering_2_3Components:
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

# --- Run Routine "buffering_2_3" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *buffer23_txt* updates
    
    # if buffer23_txt is starting this frame...
    if buffer23_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buffer23_txt.frameNStart = frameN  # exact frame index
        buffer23_txt.tStart = t  # local t and not account for scr refresh
        buffer23_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buffer23_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'buffer23_txt.started')
        # update status
        buffer23_txt.status = STARTED
        buffer23_txt.setAutoDraw(True)
    
    # if buffer23_txt is active this frame...
    if buffer23_txt.status == STARTED:
        # update params
        pass
    
    # if buffer23_txt is stopping this frame...
    if buffer23_txt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > buffer23_txt.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            buffer23_txt.tStop = t  # not accounting for scr refresh
            buffer23_txt.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'buffer23_txt.stopped')
            # update status
            buffer23_txt.status = FINISHED
            buffer23_txt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in buffering_2_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "buffering_2_3" ---
for thisComponent in buffering_2_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# set up handler to look after randomisation of conditions etc
allrep_3nback = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='allrep_3nback')
thisExp.addLoop(allrep_3nback)  # add the loop to the experiment
thisAllrep_3nback = allrep_3nback.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAllrep_3nback.rgb)
if thisAllrep_3nback != None:
    for paramName in thisAllrep_3nback:
        exec('{} = thisAllrep_3nback[paramName]'.format(paramName))

for thisAllrep_3nback in allrep_3nback:
    currentLoop = allrep_3nback
    # abbreviate parameter names if possible (e.g. rgb = thisAllrep_3nback.rgb)
    if thisAllrep_3nback != None:
        for paramName in thisAllrep_3nback:
            exec('{} = thisAllrep_3nback[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_3nback = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('filtered_seq_single_column_3n.csv'),
        seed=None, name='trials_3nback')
    thisExp.addLoop(trials_3nback)  # add the loop to the experiment
    thisTrials_3nback = trials_3nback.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_3nback.rgb)
    if thisTrials_3nback != None:
        for paramName in thisTrials_3nback:
            exec('{} = thisTrials_3nback[paramName]'.format(paramName))
    
    for thisTrials_3nback in trials_3nback:
        currentLoop = trials_3nback
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_3nback.rgb)
        if thisTrials_3nback != None:
            for paramName in thisTrials_3nback:
                exec('{} = thisTrials_3nback[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "fix" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        fixComponents = [fix1]
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
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix1* updates
            
            # if fix1 is starting this frame...
            if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix1.frameNStart = frameN  # exact frame index
                fix1.tStart = t  # local t and not account for scr refresh
                fix1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
                # update status
                fix1.status = STARTED
                fix1.setAutoDraw(True)
            
            # if fix1 is active this frame...
            if fix1.status == STARTED:
                # update params
                pass
            
            # if fix1 is stopping this frame...
            if fix1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    fix1.tStop = t  # not accounting for scr refresh
                    fix1.frameNStop = frameN  # exact frame index
                    # update status
                    fix1.status = FINISHED
                    fix1.setAutoDraw(False)
            
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
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "trial_3n" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from griddot3
        # Define grid parameters
        n_rows = 3
        n_cols = 3
        grid_size = 0.65  # size in normalized units (0 to 1)
        cell_size = grid_size / n_rows
        
        # Create grid lines using Rect
        grid_lines = []
        for i in range(n_rows + 1):
            # Horizontal lines
            y = -grid_size/2 + i*cell_size
            line = visual.Rect(win, width=grid_size, height=0.01, pos=(0, y), fillColor='white', lineColor='white')
            grid_lines.append(line)
        
        for j in range(n_cols + 1):
            # Vertical lines
            x = -grid_size/2 + j*cell_size
            line = visual.Rect(win, width=0.01, height=grid_size, pos=(x, 0), fillColor='white', lineColor='white')
            grid_lines.append(line)
        
        # Create the dot
        dot = visual.Circle(win, radius=0.04, fillColor='red', lineColor='red')
        
        step_duration = 2  # seconds per step
        step_index = 0
        step_clock = core.Clock()
        
        if Nloop == 5:
            currentLoop.finished = True
        Nloop = Nloop+1
        griddot_resp3.keys = []
        griddot_resp3.rt = []
        _griddot_resp3_allKeys = []
        # keep track of which components have finished
        trial_3nComponents = [griddot_resp3]
        for thisComponent in trial_3nComponents:
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
        
        # --- Run Routine "trial_3n" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 18.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from griddot3
            if step_index < len(sequence):
                row_index, col_index = sequence[step_index]
                dot.pos = (-grid_size/2 + (col_index + 0.5) * cell_size,
                           -grid_size/2 + (row_index + 0.5) * cell_size)
            
                # Set color for first two dots, else default to red
                if step_index < 3:
                    dot.fillColor = 'purple'
                    dot.lineColor = 'purple'
                else:
                    dot.fillColor = 'red'
                    dot.lineColor = 'red'
            
                for line in grid_lines:
                    line.draw()
            
                current_time = step_clock.getTime()
            
                # Draw dot only if within first 1.8 seconds of the step
                if current_time < 1.8:
                    dot.draw()
            
                if current_time >= step_duration:  # step_duration should be 2.0 seconds
                    step_clock.reset()
                    step_index += 1
            else:
                continueRoutine = False
            
            
            # *griddot_resp3* updates
            waitOnFlip = False
            
            # if griddot_resp3 is starting this frame...
            if griddot_resp3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                griddot_resp3.frameNStart = frameN  # exact frame index
                griddot_resp3.tStart = t  # local t and not account for scr refresh
                griddot_resp3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(griddot_resp3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'griddot_resp3.started')
                # update status
                griddot_resp3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(griddot_resp3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(griddot_resp3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if griddot_resp3 is stopping this frame...
            if griddot_resp3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > griddot_resp3.tStartRefresh + 18-frameTolerance:
                    # keep track of stop time/frame for later
                    griddot_resp3.tStop = t  # not accounting for scr refresh
                    griddot_resp3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'griddot_resp3.stopped')
                    # update status
                    griddot_resp3.status = FINISHED
                    griddot_resp3.status = FINISHED
            if griddot_resp3.status == STARTED and not waitOnFlip:
                theseKeys = griddot_resp3.getKeys(keyList=['left','right'], waitRelease=False)
                _griddot_resp3_allKeys.extend(theseKeys)
                if len(_griddot_resp3_allKeys):
                    griddot_resp3.keys = [key.name for key in _griddot_resp3_allKeys]  # storing all keys
                    griddot_resp3.rt = [key.rt for key in _griddot_resp3_allKeys]
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_3nComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_3n" ---
        for thisComponent in trial_3nComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if griddot_resp3.keys in ['', [], None]:  # No response was made
            griddot_resp3.keys = None
        trials_3nback.addData('griddot_resp3.keys',griddot_resp3.keys)
        if griddot_resp3.keys != None:  # we had a response
            trials_3nback.addData('griddot_resp3.rt', griddot_resp3.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-18.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_3nback'
    
    
    # --- Prepare to start Routine "timebreak" ---
    continueRoutine = True
    # update component parameters for each repeat
    timeout_resp.keys = []
    timeout_resp.rt = []
    _timeout_resp_allKeys = []
    # Run 'Begin Routine' code from countreset
    Nloop = 0
    # keep track of which components have finished
    timebreakComponents = [timeout_txt, timeout_resp]
    for thisComponent in timebreakComponents:
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
    
    # --- Run Routine "timebreak" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *timeout_txt* updates
        
        # if timeout_txt is starting this frame...
        if timeout_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timeout_txt.frameNStart = frameN  # exact frame index
            timeout_txt.tStart = t  # local t and not account for scr refresh
            timeout_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timeout_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            timeout_txt.status = STARTED
            timeout_txt.setAutoDraw(True)
        
        # if timeout_txt is active this frame...
        if timeout_txt.status == STARTED:
            # update params
            pass
        
        # *timeout_resp* updates
        waitOnFlip = False
        
        # if timeout_resp is starting this frame...
        if timeout_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timeout_resp.frameNStart = frameN  # exact frame index
            timeout_resp.tStart = t  # local t and not account for scr refresh
            timeout_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timeout_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            timeout_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(timeout_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(timeout_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if timeout_resp.status == STARTED and not waitOnFlip:
            theseKeys = timeout_resp.getKeys(keyList=['space'], waitRelease=False)
            _timeout_resp_allKeys.extend(theseKeys)
            if len(_timeout_resp_allKeys):
                timeout_resp.keys = _timeout_resp_allKeys[-1].name  # just the last key pressed
                timeout_resp.rt = _timeout_resp_allKeys[-1].rt
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
        for thisComponent in timebreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "timebreak" ---
    for thisComponent in timebreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "timebreak" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'allrep_3nback'


# --- Prepare to start Routine "buffering_3_4" ---
continueRoutine = True
# update component parameters for each repeat
# Run 'Begin Routine' code from countreset_4
Nloop = 0
# keep track of which components have finished
buffering_3_4Components = [buffer34_txt]
for thisComponent in buffering_3_4Components:
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

# --- Run Routine "buffering_3_4" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *buffer34_txt* updates
    
    # if buffer34_txt is starting this frame...
    if buffer34_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        buffer34_txt.frameNStart = frameN  # exact frame index
        buffer34_txt.tStart = t  # local t and not account for scr refresh
        buffer34_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(buffer34_txt, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'buffer34_txt.started')
        # update status
        buffer34_txt.status = STARTED
        buffer34_txt.setAutoDraw(True)
    
    # if buffer34_txt is active this frame...
    if buffer34_txt.status == STARTED:
        # update params
        pass
    
    # if buffer34_txt is stopping this frame...
    if buffer34_txt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > buffer34_txt.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            buffer34_txt.tStop = t  # not accounting for scr refresh
            buffer34_txt.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'buffer34_txt.stopped')
            # update status
            buffer34_txt.status = FINISHED
            buffer34_txt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in buffering_3_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "buffering_3_4" ---
for thisComponent in buffering_3_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# set up handler to look after randomisation of conditions etc
allrep_4nback = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='allrep_4nback')
thisExp.addLoop(allrep_4nback)  # add the loop to the experiment
thisAllrep_4nback = allrep_4nback.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAllrep_4nback.rgb)
if thisAllrep_4nback != None:
    for paramName in thisAllrep_4nback:
        exec('{} = thisAllrep_4nback[paramName]'.format(paramName))

for thisAllrep_4nback in allrep_4nback:
    currentLoop = allrep_4nback
    # abbreviate parameter names if possible (e.g. rgb = thisAllrep_4nback.rgb)
    if thisAllrep_4nback != None:
        for paramName in thisAllrep_4nback:
            exec('{} = thisAllrep_4nback[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_4nback = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('filtered_seq_single_column_4n.csv'),
        seed=None, name='trials_4nback')
    thisExp.addLoop(trials_4nback)  # add the loop to the experiment
    thisTrials_4nback = trials_4nback.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_4nback.rgb)
    if thisTrials_4nback != None:
        for paramName in thisTrials_4nback:
            exec('{} = thisTrials_4nback[paramName]'.format(paramName))
    
    for thisTrials_4nback in trials_4nback:
        currentLoop = trials_4nback
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_4nback.rgb)
        if thisTrials_4nback != None:
            for paramName in thisTrials_4nback:
                exec('{} = thisTrials_4nback[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "fix" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        fixComponents = [fix1]
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
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix1* updates
            
            # if fix1 is starting this frame...
            if fix1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix1.frameNStart = frameN  # exact frame index
                fix1.tStart = t  # local t and not account for scr refresh
                fix1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix1, 'tStartRefresh')  # time at next scr refresh
                # update status
                fix1.status = STARTED
                fix1.setAutoDraw(True)
            
            # if fix1 is active this frame...
            if fix1.status == STARTED:
                # update params
                pass
            
            # if fix1 is stopping this frame...
            if fix1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    fix1.tStop = t  # not accounting for scr refresh
                    fix1.frameNStop = frameN  # exact frame index
                    # update status
                    fix1.status = FINISHED
                    fix1.setAutoDraw(False)
            
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
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "trial_4n" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from griddot4
        # Define grid parameters
        n_rows = 3
        n_cols = 3
        grid_size = 0.65  # size in normalized units (0 to 1)
        cell_size = grid_size / n_rows
        
        # Create grid lines using Rect
        grid_lines = []
        for i in range(n_rows + 1):
            # Horizontal lines
            y = -grid_size/2 + i*cell_size
            line = visual.Rect(win, width=grid_size, height=0.01, pos=(0, y), fillColor='white', lineColor='white')
            grid_lines.append(line)
        
        for j in range(n_cols + 1):
            # Vertical lines
            x = -grid_size/2 + j*cell_size
            line = visual.Rect(win, width=0.01, height=grid_size, pos=(x, 0), fillColor='white', lineColor='white')
            grid_lines.append(line)
        
        # Create the dot
        dot = visual.Circle(win, radius=0.04, fillColor='red', lineColor='red')
        
        step_duration = 2  # seconds per step
        step_index = 0
        step_clock = core.Clock()
        
        if Nloop == 5:
            currentLoop.finished = True
        Nloop = Nloop+1
        griddot_resp4.keys = []
        griddot_resp4.rt = []
        _griddot_resp4_allKeys = []
        # keep track of which components have finished
        trial_4nComponents = [griddot_resp4]
        for thisComponent in trial_4nComponents:
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
        
        # --- Run Routine "trial_4n" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 20.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from griddot4
            if step_index < len(sequence):
                row_index, col_index = sequence[step_index]
                dot.pos = (-grid_size/2 + (col_index + 0.5) * cell_size,
                           -grid_size/2 + (row_index + 0.5) * cell_size)
            
                # Set color for first two dots, else default to red
                if step_index < 4:
                    dot.fillColor = 'yellow'
                    dot.lineColor = 'yellow'
                else:
                    dot.fillColor = 'red'
                    dot.lineColor = 'red'
            
                for line in grid_lines:
                    line.draw()
            
                current_time = step_clock.getTime()
            
                # Draw dot only if within first 1.8 seconds of the step
                if current_time < 1.8:
                    dot.draw()
            
                if current_time >= step_duration:  # step_duration should be 2.0 seconds
                    step_clock.reset()
                    step_index += 1
            else:
                continueRoutine = False
            
            
            # *griddot_resp4* updates
            waitOnFlip = False
            
            # if griddot_resp4 is starting this frame...
            if griddot_resp4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                griddot_resp4.frameNStart = frameN  # exact frame index
                griddot_resp4.tStart = t  # local t and not account for scr refresh
                griddot_resp4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(griddot_resp4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'griddot_resp4.started')
                # update status
                griddot_resp4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(griddot_resp4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(griddot_resp4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if griddot_resp4 is stopping this frame...
            if griddot_resp4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > griddot_resp4.tStartRefresh + 20-frameTolerance:
                    # keep track of stop time/frame for later
                    griddot_resp4.tStop = t  # not accounting for scr refresh
                    griddot_resp4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'griddot_resp4.stopped')
                    # update status
                    griddot_resp4.status = FINISHED
                    griddot_resp4.status = FINISHED
            if griddot_resp4.status == STARTED and not waitOnFlip:
                theseKeys = griddot_resp4.getKeys(keyList=['left','right'], waitRelease=False)
                _griddot_resp4_allKeys.extend(theseKeys)
                if len(_griddot_resp4_allKeys):
                    griddot_resp4.keys = [key.name for key in _griddot_resp4_allKeys]  # storing all keys
                    griddot_resp4.rt = [key.rt for key in _griddot_resp4_allKeys]
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_4nComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial_4n" ---
        for thisComponent in trial_4nComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if griddot_resp4.keys in ['', [], None]:  # No response was made
            griddot_resp4.keys = None
        trials_4nback.addData('griddot_resp4.keys',griddot_resp4.keys)
        if griddot_resp4.keys != None:  # we had a response
            trials_4nback.addData('griddot_resp4.rt', griddot_resp4.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-20.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_4nback'
    
    
    # --- Prepare to start Routine "timebreak" ---
    continueRoutine = True
    # update component parameters for each repeat
    timeout_resp.keys = []
    timeout_resp.rt = []
    _timeout_resp_allKeys = []
    # Run 'Begin Routine' code from countreset
    Nloop = 0
    # keep track of which components have finished
    timebreakComponents = [timeout_txt, timeout_resp]
    for thisComponent in timebreakComponents:
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
    
    # --- Run Routine "timebreak" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *timeout_txt* updates
        
        # if timeout_txt is starting this frame...
        if timeout_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timeout_txt.frameNStart = frameN  # exact frame index
            timeout_txt.tStart = t  # local t and not account for scr refresh
            timeout_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timeout_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            timeout_txt.status = STARTED
            timeout_txt.setAutoDraw(True)
        
        # if timeout_txt is active this frame...
        if timeout_txt.status == STARTED:
            # update params
            pass
        
        # *timeout_resp* updates
        waitOnFlip = False
        
        # if timeout_resp is starting this frame...
        if timeout_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            timeout_resp.frameNStart = frameN  # exact frame index
            timeout_resp.tStart = t  # local t and not account for scr refresh
            timeout_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(timeout_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            timeout_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(timeout_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(timeout_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if timeout_resp.status == STARTED and not waitOnFlip:
            theseKeys = timeout_resp.getKeys(keyList=['space'], waitRelease=False)
            _timeout_resp_allKeys.extend(theseKeys)
            if len(_timeout_resp_allKeys):
                timeout_resp.keys = _timeout_resp_allKeys[-1].name  # just the last key pressed
                timeout_resp.rt = _timeout_resp_allKeys[-1].rt
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
        for thisComponent in timebreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "timebreak" ---
    for thisComponent in timebreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "timebreak" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'allrep_4nback'


# --- Prepare to start Routine "goodbye" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
goodbyeComponents = [bye_txt]
for thisComponent in goodbyeComponents:
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

# --- Run Routine "goodbye" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 2.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *bye_txt* updates
    
    # if bye_txt is starting this frame...
    if bye_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bye_txt.frameNStart = frameN  # exact frame index
        bye_txt.tStart = t  # local t and not account for scr refresh
        bye_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bye_txt, 'tStartRefresh')  # time at next scr refresh
        # update status
        bye_txt.status = STARTED
        bye_txt.setAutoDraw(True)
    
    # if bye_txt is active this frame...
    if bye_txt.status == STARTED:
        # update params
        pass
    
    # if bye_txt is stopping this frame...
    if bye_txt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bye_txt.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            bye_txt.tStop = t  # not accounting for scr refresh
            bye_txt.frameNStop = frameN  # exact frame index
            # update status
            bye_txt.status = FINISHED
            bye_txt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "goodbye" ---
for thisComponent in goodbyeComponents:
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
