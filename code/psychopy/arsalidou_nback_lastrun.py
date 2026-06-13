#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on June 08, 2026, at 13:26
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
expName = 'CMT'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\paper\\OneDrive\\Desktop\\PsychoPy\\masters_imagery\\arsalidou_nback_lastrun.py',
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

# --- Initialize components for Routine "arsalidou_instr" ---
arsalisou_instr = visual.TextStim(win=win, name='arsalisou_instr',
    text='Вам будет показаны 9 цветных квадратов в матрице. Каждые 3 секунды цвета квадратов будут меняться. \n\nВаша задача - ответить, совпадают ли цвета нового набора с прошлым. \nВнимание: считаются все цвета, КРОМЕ зеленого и синего! Эти цвета игнорируйте. Расположение цветов также не имеет значения! \n\nЕсли цвета не совпадают, нажмите "←". \nЕсли совпадают, нажмите "→".\n\nЧтобы начать тренировочный этап, нажмите любую кнопку.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
arsalidou_instr_key = keyboard.Keyboard()

# --- Initialize components for Routine "fix" ---
blank = visual.TextStim(win=win, name='blank',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "arsal_code_task" ---
hintText = visual.TextStim(win=win, name='hintText',
    text='← (НЕТ) Совпадают с предыдущим? (ДА) →',
    font='Open Sans',
    pos=(0, -0.4), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
matrix_resp = keyboard.Keyboard()

# --- Initialize components for Routine "fix" ---
blank = visual.TextStim(win=win, name='blank',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "train_confirm" ---
trainconf_txt = visual.TextStim(win=win, name='trainconf_txt',
    text='Тренировка закончилась.\n\nЕсли вам понятен принцип задачи и вы готовы начать основную часть задачи, нажмите "Y".\nЕсли вы хотите пройти тренировку еще раз, нажмите "N".\n\nВы можете перепройти тренировку 3 раза.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trainconf = keyboard.Keyboard()

# --- Initialize components for Routine "arsalidou_instr_2" ---
arsalisou_instr_2 = visual.TextStim(win=win, name='arsalisou_instr_2',
    text='Тренировка окончена!\n\nЧтобы начать основной этап, нажмите любую кнопку.',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
arsalidou_instr_key_2 = keyboard.Keyboard()

# --- Initialize components for Routine "fix" ---
blank = visual.TextStim(win=win, name='blank',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "arsal_code_task" ---
hintText = visual.TextStim(win=win, name='hintText',
    text='← (НЕТ) Совпадают с предыдущим? (ДА) →',
    font='Open Sans',
    pos=(0, -0.4), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
matrix_resp = keyboard.Keyboard()

# --- Initialize components for Routine "fix" ---
blank = visual.TextStim(win=win, name='blank',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "arsal_code_task_2" ---
hintText_2 = visual.TextStim(win=win, name='hintText_2',
    text='← (НЕТ) Совпадают с предыдущим? (ДА) →',
    font='Open Sans',
    pos=(0, -0.4), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
matrix_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "fix" ---
blank = visual.TextStim(win=win, name='blank',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "arsal_code_task_3" ---
hintText_3 = visual.TextStim(win=win, name='hintText_3',
    text='← (НЕТ) Совпадают с предыдущим? (ДА) →',
    font='Open Sans',
    pos=(0, -0.4), height=0.035, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
matrix_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "finish_goodbye" ---
byebye_text = visual.TextStim(win=win, name='byebye_text',
    text='На этом эта методика окончена.\n\nБольшое спасибо за участие! ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "arsalidou_instr" ---
continueRoutine = True
# update component parameters for each repeat
arsalidou_instr_key.keys = []
arsalidou_instr_key.rt = []
_arsalidou_instr_key_allKeys = []
# keep track of which components have finished
arsalidou_instrComponents = [arsalisou_instr, arsalidou_instr_key]
for thisComponent in arsalidou_instrComponents:
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

# --- Run Routine "arsalidou_instr" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *arsalisou_instr* updates
    
    # if arsalisou_instr is starting this frame...
    if arsalisou_instr.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        arsalisou_instr.frameNStart = frameN  # exact frame index
        arsalisou_instr.tStart = t  # local t and not account for scr refresh
        arsalisou_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arsalisou_instr, 'tStartRefresh')  # time at next scr refresh
        # update status
        arsalisou_instr.status = STARTED
        arsalisou_instr.setAutoDraw(True)
    
    # if arsalisou_instr is active this frame...
    if arsalisou_instr.status == STARTED:
        # update params
        pass
    
    # *arsalidou_instr_key* updates
    waitOnFlip = False
    
    # if arsalidou_instr_key is starting this frame...
    if arsalidou_instr_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        arsalidou_instr_key.frameNStart = frameN  # exact frame index
        arsalidou_instr_key.tStart = t  # local t and not account for scr refresh
        arsalidou_instr_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arsalidou_instr_key, 'tStartRefresh')  # time at next scr refresh
        # update status
        arsalidou_instr_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(arsalidou_instr_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(arsalidou_instr_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if arsalidou_instr_key.status == STARTED and not waitOnFlip:
        theseKeys = arsalidou_instr_key.getKeys(keyList=None, waitRelease=False)
        _arsalidou_instr_key_allKeys.extend(theseKeys)
        if len(_arsalidou_instr_key_allKeys):
            arsalidou_instr_key.keys = _arsalidou_instr_key_allKeys[-1].name  # just the last key pressed
            arsalidou_instr_key.rt = _arsalidou_instr_key_allKeys[-1].rt
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
    for thisComponent in arsalidou_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "arsalidou_instr" ---
for thisComponent in arsalidou_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "arsalidou_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
training = data.TrialHandler(nReps=4.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # set up handler to look after randomisation of conditions etc
    arsal_train = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='arsal_train')
    thisExp.addLoop(arsal_train)  # add the loop to the experiment
    thisArsal_train = arsal_train.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisArsal_train.rgb)
    if thisArsal_train != None:
        for paramName in thisArsal_train:
            exec('{} = thisArsal_train[paramName]'.format(paramName))
    
    for thisArsal_train in arsal_train:
        currentLoop = arsal_train
        # abbreviate parameter names if possible (e.g. rgb = thisArsal_train.rgb)
        if thisArsal_train != None:
            for paramName in thisArsal_train:
                exec('{} = thisArsal_train[paramName]'.format(paramName))
        
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
        
        # --- Prepare to start Routine "arsal_code_task" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from matrix_code
        from psychopy import core
        import random
        
        # Colors
        blue = (-1, -1, 1)
        green = (-1, 1, -1)  # slightly “greener” than (0,1,0)
        variable_colors = [
            (1, 1, -1),   # bright yellow (no blue)
            (1, -1, -1),  # bright red
            (1, -0.2, -1),  # bright orange
            (1, -1, 1)    # bright magenta
        ]
        
        # Grid
        n_rows = 3
        n_cols = 3
        grid_size = 0.65
        cell_size = grid_size / n_rows
        square_size = cell_size * 0.9
        
        # Generate sequence with guaranteed repeat
        matrices = []
        for i in range(7):
            matrix_colors = []
        
            # choose exactly two variable colors for this matrix
            chosen_vars = random.sample(variable_colors, 2)
        
            for j in range(9):
                if random.random() < 0.3:
                    # blue/green as before
                    matrix_colors.append(random.choice([blue, green]))
                else:
                    # only from the two chosen variable colors
                    matrix_colors.append(random.choice(chosen_vars))
        
            matrices.append(matrix_colors)
        
        # Find repeat
        repeat_idx = None
        for i in range(1, 7):
            set_i = frozenset(c for c in matrices[i] if c not in (blue, green))
            for j in range(i):
                set_j = frozenset(c for c in matrices[j] if c not in (blue, green))
                if set_i == set_j:
                    repeat_idx = j
                    break
            if repeat_idx:
                break
        
        if not repeat_idx:
            repeat_idx = random.randint(0, 6)
        
        sequence = matrices + [matrices[repeat_idx]]
        
        # Timing
        step_duration = 3.0
        step_index = 0
        step_clock = core.Clock()
        
        
        matrix_resp.keys = []
        matrix_resp.rt = []
        _matrix_resp_allKeys = []
        # keep track of which components have finished
        arsal_code_taskComponents = [hintText, matrix_resp]
        for thisComponent in arsal_code_taskComponents:
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
        
        # --- Run Routine "arsal_code_task" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 24.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *hintText* updates
            
            # if hintText is starting this frame...
            if hintText.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                hintText.frameNStart = frameN  # exact frame index
                hintText.tStart = t  # local t and not account for scr refresh
                hintText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(hintText, 'tStartRefresh')  # time at next scr refresh
                # update status
                hintText.status = STARTED
                hintText.setAutoDraw(True)
            
            # if hintText is active this frame...
            if hintText.status == STARTED:
                # update params
                pass
            
            # if hintText is stopping this frame...
            if hintText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > hintText.tStartRefresh + 21-frameTolerance:
                    # keep track of stop time/frame for later
                    hintText.tStop = t  # not accounting for scr refresh
                    hintText.frameNStop = frameN  # exact frame index
                    # update status
                    hintText.status = FINISHED
                    hintText.setAutoDraw(False)
            # Run 'Each Frame' code from matrix_code
            # Draw 3x3 colored squares
            colors = sequence[step_index]
            square_idx = 0
            
            for i in range(3):
                for j in range(3):
                    x = -0.325 + j*0.2167 + 0.1083
                    y = -0.325 + i*0.2167 + 0.1083
                    
                    square = visual.Rect(win, width=0.18, height=0.18, 
                                       pos=(x, y), fillColor=colors[square_idx], 
                                       lineColor=colors[square_idx])
                    square.draw()
                    square_idx += 1
            
            # Advance step
            if step_clock.getTime() >= step_duration:
                step_clock.reset()
                step_index += 1
                if step_index >= 8:
                    step_index = 7
            
            
            # *matrix_resp* updates
            waitOnFlip = False
            
            # if matrix_resp is starting this frame...
            if matrix_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                matrix_resp.frameNStart = frameN  # exact frame index
                matrix_resp.tStart = t  # local t and not account for scr refresh
                matrix_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(matrix_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'matrix_resp.started')
                # update status
                matrix_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(matrix_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(matrix_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if matrix_resp is stopping this frame...
            if matrix_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > matrix_resp.tStartRefresh + 24-frameTolerance:
                    # keep track of stop time/frame for later
                    matrix_resp.tStop = t  # not accounting for scr refresh
                    matrix_resp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'matrix_resp.stopped')
                    # update status
                    matrix_resp.status = FINISHED
                    matrix_resp.status = FINISHED
            if matrix_resp.status == STARTED and not waitOnFlip:
                theseKeys = matrix_resp.getKeys(keyList=['left','right'], waitRelease=False)
                _matrix_resp_allKeys.extend(theseKeys)
                if len(_matrix_resp_allKeys):
                    matrix_resp.keys = [key.name for key in _matrix_resp_allKeys]  # storing all keys
                    matrix_resp.rt = [key.rt for key in _matrix_resp_allKeys]
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in arsal_code_taskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "arsal_code_task" ---
        for thisComponent in arsal_code_taskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from matrix_code
        thisExp.addData('sequence', sequence)
        thisExp.addData('repeat_idx', repeat_idx)
        
        # check responses
        if matrix_resp.keys in ['', [], None]:  # No response was made
            matrix_resp.keys = None
        arsal_train.addData('matrix_resp.keys',matrix_resp.keys)
        if matrix_resp.keys != None:  # we had a response
            arsal_train.addData('matrix_resp.rt', matrix_resp.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-24.000000)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'arsal_train'
    
    
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
    
    # --- Prepare to start Routine "train_confirm" ---
    continueRoutine = True
    # update component parameters for each repeat
    trainconf.keys = []
    trainconf.rt = []
    _trainconf_allKeys = []
    # keep track of which components have finished
    train_confirmComponents = [trainconf_txt, trainconf]
    for thisComponent in train_confirmComponents:
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
    
    # --- Run Routine "train_confirm" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trainconf_txt* updates
        
        # if trainconf_txt is starting this frame...
        if trainconf_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trainconf_txt.frameNStart = frameN  # exact frame index
            trainconf_txt.tStart = t  # local t and not account for scr refresh
            trainconf_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trainconf_txt, 'tStartRefresh')  # time at next scr refresh
            # update status
            trainconf_txt.status = STARTED
            trainconf_txt.setAutoDraw(True)
        
        # if trainconf_txt is active this frame...
        if trainconf_txt.status == STARTED:
            # update params
            pass
        
        # *trainconf* updates
        waitOnFlip = False
        
        # if trainconf is starting this frame...
        if trainconf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trainconf.frameNStart = frameN  # exact frame index
            trainconf.tStart = t  # local t and not account for scr refresh
            trainconf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trainconf, 'tStartRefresh')  # time at next scr refresh
            # update status
            trainconf.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(trainconf.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(trainconf.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if trainconf.status == STARTED and not waitOnFlip:
            theseKeys = trainconf.getKeys(keyList=['y','n'], waitRelease=False)
            _trainconf_allKeys.extend(theseKeys)
            if len(_trainconf_allKeys):
                trainconf.keys = [key.name for key in _trainconf_allKeys]  # storing all keys
                trainconf.rt = [key.rt for key in _trainconf_allKeys]
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
        for thisComponent in train_confirmComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "train_confirm" ---
    for thisComponent in train_confirmComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if trainconf.keys in ['', [], None]:  # No response was made
        trainconf.keys = None
    training.addData('trainconf.keys',trainconf.keys)
    if trainconf.keys != None:  # we had a response
        training.addData('trainconf.rt', trainconf.rt)
    # Run 'End Routine' code from confirmation_code
    if 'y' in trainconf.keys:
        training.finished = True
    # the Routine "train_confirm" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 4.0 repeats of 'training'


# --- Prepare to start Routine "arsalidou_instr_2" ---
continueRoutine = True
# update component parameters for each repeat
arsalidou_instr_key_2.keys = []
arsalidou_instr_key_2.rt = []
_arsalidou_instr_key_2_allKeys = []
# keep track of which components have finished
arsalidou_instr_2Components = [arsalisou_instr_2, arsalidou_instr_key_2]
for thisComponent in arsalidou_instr_2Components:
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

# --- Run Routine "arsalidou_instr_2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *arsalisou_instr_2* updates
    
    # if arsalisou_instr_2 is starting this frame...
    if arsalisou_instr_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        arsalisou_instr_2.frameNStart = frameN  # exact frame index
        arsalisou_instr_2.tStart = t  # local t and not account for scr refresh
        arsalisou_instr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arsalisou_instr_2, 'tStartRefresh')  # time at next scr refresh
        # update status
        arsalisou_instr_2.status = STARTED
        arsalisou_instr_2.setAutoDraw(True)
    
    # if arsalisou_instr_2 is active this frame...
    if arsalisou_instr_2.status == STARTED:
        # update params
        pass
    
    # *arsalidou_instr_key_2* updates
    waitOnFlip = False
    
    # if arsalidou_instr_key_2 is starting this frame...
    if arsalidou_instr_key_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        arsalidou_instr_key_2.frameNStart = frameN  # exact frame index
        arsalidou_instr_key_2.tStart = t  # local t and not account for scr refresh
        arsalidou_instr_key_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(arsalidou_instr_key_2, 'tStartRefresh')  # time at next scr refresh
        # update status
        arsalidou_instr_key_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(arsalidou_instr_key_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(arsalidou_instr_key_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if arsalidou_instr_key_2.status == STARTED and not waitOnFlip:
        theseKeys = arsalidou_instr_key_2.getKeys(keyList=None, waitRelease=False)
        _arsalidou_instr_key_2_allKeys.extend(theseKeys)
        if len(_arsalidou_instr_key_2_allKeys):
            arsalidou_instr_key_2.keys = _arsalidou_instr_key_2_allKeys[-1].name  # just the last key pressed
            arsalidou_instr_key_2.rt = _arsalidou_instr_key_2_allKeys[-1].rt
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
    for thisComponent in arsalidou_instr_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "arsalidou_instr_2" ---
for thisComponent in arsalidou_instr_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "arsalidou_instr_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
arsal_s2 = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='arsal_s2')
thisExp.addLoop(arsal_s2)  # add the loop to the experiment
thisArsal_s2 = arsal_s2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisArsal_s2.rgb)
if thisArsal_s2 != None:
    for paramName in thisArsal_s2:
        exec('{} = thisArsal_s2[paramName]'.format(paramName))

for thisArsal_s2 in arsal_s2:
    currentLoop = arsal_s2
    # abbreviate parameter names if possible (e.g. rgb = thisArsal_s2.rgb)
    if thisArsal_s2 != None:
        for paramName in thisArsal_s2:
            exec('{} = thisArsal_s2[paramName]'.format(paramName))
    
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
    
    # --- Prepare to start Routine "arsal_code_task" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from matrix_code
    from psychopy import core
    import random
    
    # Colors
    blue = (-1, -1, 1)
    green = (-1, 1, -1)  # slightly “greener” than (0,1,0)
    variable_colors = [
        (1, 1, -1),   # bright yellow (no blue)
        (1, -1, -1),  # bright red
        (1, -0.2, -1),  # bright orange
        (1, -1, 1)    # bright magenta
    ]
    
    # Grid
    n_rows = 3
    n_cols = 3
    grid_size = 0.65
    cell_size = grid_size / n_rows
    square_size = cell_size * 0.9
    
    # Generate sequence with guaranteed repeat
    matrices = []
    for i in range(7):
        matrix_colors = []
    
        # choose exactly two variable colors for this matrix
        chosen_vars = random.sample(variable_colors, 2)
    
        for j in range(9):
            if random.random() < 0.3:
                # blue/green as before
                matrix_colors.append(random.choice([blue, green]))
            else:
                # only from the two chosen variable colors
                matrix_colors.append(random.choice(chosen_vars))
    
        matrices.append(matrix_colors)
    
    # Find repeat
    repeat_idx = None
    for i in range(1, 7):
        set_i = frozenset(c for c in matrices[i] if c not in (blue, green))
        for j in range(i):
            set_j = frozenset(c for c in matrices[j] if c not in (blue, green))
            if set_i == set_j:
                repeat_idx = j
                break
        if repeat_idx:
            break
    
    if not repeat_idx:
        repeat_idx = random.randint(0, 6)
    
    sequence = matrices + [matrices[repeat_idx]]
    
    # Timing
    step_duration = 3.0
    step_index = 0
    step_clock = core.Clock()
    
    
    matrix_resp.keys = []
    matrix_resp.rt = []
    _matrix_resp_allKeys = []
    # keep track of which components have finished
    arsal_code_taskComponents = [hintText, matrix_resp]
    for thisComponent in arsal_code_taskComponents:
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
    
    # --- Run Routine "arsal_code_task" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 24.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *hintText* updates
        
        # if hintText is starting this frame...
        if hintText.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            hintText.frameNStart = frameN  # exact frame index
            hintText.tStart = t  # local t and not account for scr refresh
            hintText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hintText, 'tStartRefresh')  # time at next scr refresh
            # update status
            hintText.status = STARTED
            hintText.setAutoDraw(True)
        
        # if hintText is active this frame...
        if hintText.status == STARTED:
            # update params
            pass
        
        # if hintText is stopping this frame...
        if hintText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hintText.tStartRefresh + 21-frameTolerance:
                # keep track of stop time/frame for later
                hintText.tStop = t  # not accounting for scr refresh
                hintText.frameNStop = frameN  # exact frame index
                # update status
                hintText.status = FINISHED
                hintText.setAutoDraw(False)
        # Run 'Each Frame' code from matrix_code
        # Draw 3x3 colored squares
        colors = sequence[step_index]
        square_idx = 0
        
        for i in range(3):
            for j in range(3):
                x = -0.325 + j*0.2167 + 0.1083
                y = -0.325 + i*0.2167 + 0.1083
                
                square = visual.Rect(win, width=0.18, height=0.18, 
                                   pos=(x, y), fillColor=colors[square_idx], 
                                   lineColor=colors[square_idx])
                square.draw()
                square_idx += 1
        
        # Advance step
        if step_clock.getTime() >= step_duration:
            step_clock.reset()
            step_index += 1
            if step_index >= 8:
                step_index = 7
        
        
        # *matrix_resp* updates
        waitOnFlip = False
        
        # if matrix_resp is starting this frame...
        if matrix_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            matrix_resp.frameNStart = frameN  # exact frame index
            matrix_resp.tStart = t  # local t and not account for scr refresh
            matrix_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(matrix_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'matrix_resp.started')
            # update status
            matrix_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(matrix_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(matrix_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if matrix_resp is stopping this frame...
        if matrix_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > matrix_resp.tStartRefresh + 24-frameTolerance:
                # keep track of stop time/frame for later
                matrix_resp.tStop = t  # not accounting for scr refresh
                matrix_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'matrix_resp.stopped')
                # update status
                matrix_resp.status = FINISHED
                matrix_resp.status = FINISHED
        if matrix_resp.status == STARTED and not waitOnFlip:
            theseKeys = matrix_resp.getKeys(keyList=['left','right'], waitRelease=False)
            _matrix_resp_allKeys.extend(theseKeys)
            if len(_matrix_resp_allKeys):
                matrix_resp.keys = [key.name for key in _matrix_resp_allKeys]  # storing all keys
                matrix_resp.rt = [key.rt for key in _matrix_resp_allKeys]
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in arsal_code_taskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "arsal_code_task" ---
    for thisComponent in arsal_code_taskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from matrix_code
    thisExp.addData('sequence', sequence)
    thisExp.addData('repeat_idx', repeat_idx)
    
    # check responses
    if matrix_resp.keys in ['', [], None]:  # No response was made
        matrix_resp.keys = None
    arsal_s2.addData('matrix_resp.keys',matrix_resp.keys)
    if matrix_resp.keys != None:  # we had a response
        arsal_s2.addData('matrix_resp.rt', matrix_resp.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-24.000000)
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'arsal_s2'


# set up handler to look after randomisation of conditions etc
arsal_s3 = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='arsal_s3')
thisExp.addLoop(arsal_s3)  # add the loop to the experiment
thisArsal_s3 = arsal_s3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisArsal_s3.rgb)
if thisArsal_s3 != None:
    for paramName in thisArsal_s3:
        exec('{} = thisArsal_s3[paramName]'.format(paramName))

for thisArsal_s3 in arsal_s3:
    currentLoop = arsal_s3
    # abbreviate parameter names if possible (e.g. rgb = thisArsal_s3.rgb)
    if thisArsal_s3 != None:
        for paramName in thisArsal_s3:
            exec('{} = thisArsal_s3[paramName]'.format(paramName))
    
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
    
    # --- Prepare to start Routine "arsal_code_task_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from matrix_code_2
    from psychopy import core
    import random
    
    # Colors
    blue = (-1, -1, 1)
    green = (-1, 1, -1)  # slightly “greener” than (0,1,0)
    variable_colors = [
        (1, 1, -1),   # bright yellow (no blue)
        (1, -1, -1),  # bright red
        (1, -0.2, -1),  # bright orange
        (1, -1, 1)    # bright magenta
    ]
    
    # Grid
    n_rows = 3
    n_cols = 3
    grid_size = 0.65
    cell_size = grid_size / n_rows
    square_size = cell_size * 0.9
    
    # Generate sequence with guaranteed repeat
    matrices = []
    for i in range(7):
        matrix_colors = []
    
        # choose exactly two variable colors for this matrix
        chosen_vars = random.sample(variable_colors, 3)
    
        for j in range(9):
            if random.random() < 0.3:
                # blue/green as before
                matrix_colors.append(random.choice([blue, green]))
            else:
                # only from the two chosen variable colors
                matrix_colors.append(random.choice(chosen_vars))
    
        matrices.append(matrix_colors)
    
    # Find repeat
    repeat_idx = None
    for i in range(1, 7):
        set_i = frozenset(c for c in matrices[i] if c not in (blue, green))
        for j in range(i):
            set_j = frozenset(c for c in matrices[j] if c not in (blue, green))
            if set_i == set_j:
                repeat_idx = j
                break
        if repeat_idx:
            break
    
    if not repeat_idx:
        repeat_idx = random.randint(0, 6)
    
    sequence = matrices + [matrices[repeat_idx]]
    
    # Timing
    step_duration = 3.0
    step_index = 0
    step_clock = core.Clock()
    
    
    matrix_resp_2.keys = []
    matrix_resp_2.rt = []
    _matrix_resp_2_allKeys = []
    # keep track of which components have finished
    arsal_code_task_2Components = [hintText_2, matrix_resp_2]
    for thisComponent in arsal_code_task_2Components:
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
    
    # --- Run Routine "arsal_code_task_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 24.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *hintText_2* updates
        
        # if hintText_2 is starting this frame...
        if hintText_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            hintText_2.frameNStart = frameN  # exact frame index
            hintText_2.tStart = t  # local t and not account for scr refresh
            hintText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hintText_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            hintText_2.status = STARTED
            hintText_2.setAutoDraw(True)
        
        # if hintText_2 is active this frame...
        if hintText_2.status == STARTED:
            # update params
            pass
        
        # if hintText_2 is stopping this frame...
        if hintText_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hintText_2.tStartRefresh + 21-frameTolerance:
                # keep track of stop time/frame for later
                hintText_2.tStop = t  # not accounting for scr refresh
                hintText_2.frameNStop = frameN  # exact frame index
                # update status
                hintText_2.status = FINISHED
                hintText_2.setAutoDraw(False)
        # Run 'Each Frame' code from matrix_code_2
        # Draw 3x3 colored squares
        colors = sequence[step_index]
        square_idx = 0
        
        for i in range(3):
            for j in range(3):
                x = -0.325 + j*0.2167 + 0.1083
                y = -0.325 + i*0.2167 + 0.1083
                
                square = visual.Rect(win, width=0.18, height=0.18, 
                                   pos=(x, y), fillColor=colors[square_idx], 
                                   lineColor=colors[square_idx])
                square.draw()
                square_idx += 1
        
        # Advance step
        if step_clock.getTime() >= step_duration:
            step_clock.reset()
            step_index += 1
            if step_index >= 8:
                step_index = 7
        
        
        # *matrix_resp_2* updates
        waitOnFlip = False
        
        # if matrix_resp_2 is starting this frame...
        if matrix_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            matrix_resp_2.frameNStart = frameN  # exact frame index
            matrix_resp_2.tStart = t  # local t and not account for scr refresh
            matrix_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(matrix_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'matrix_resp_2.started')
            # update status
            matrix_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(matrix_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(matrix_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if matrix_resp_2 is stopping this frame...
        if matrix_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > matrix_resp_2.tStartRefresh + 24-frameTolerance:
                # keep track of stop time/frame for later
                matrix_resp_2.tStop = t  # not accounting for scr refresh
                matrix_resp_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'matrix_resp_2.stopped')
                # update status
                matrix_resp_2.status = FINISHED
                matrix_resp_2.status = FINISHED
        if matrix_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = matrix_resp_2.getKeys(keyList=['left','right'], waitRelease=False)
            _matrix_resp_2_allKeys.extend(theseKeys)
            if len(_matrix_resp_2_allKeys):
                matrix_resp_2.keys = [key.name for key in _matrix_resp_2_allKeys]  # storing all keys
                matrix_resp_2.rt = [key.rt for key in _matrix_resp_2_allKeys]
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in arsal_code_task_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "arsal_code_task_2" ---
    for thisComponent in arsal_code_task_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from matrix_code_2
    thisExp.addData('sequence', sequence)
    thisExp.addData('repeat_idx', repeat_idx)
    
    # check responses
    if matrix_resp_2.keys in ['', [], None]:  # No response was made
        matrix_resp_2.keys = None
    arsal_s3.addData('matrix_resp_2.keys',matrix_resp_2.keys)
    if matrix_resp_2.keys != None:  # we had a response
        arsal_s3.addData('matrix_resp_2.rt', matrix_resp_2.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-24.000000)
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'arsal_s3'


# set up handler to look after randomisation of conditions etc
arsal_s4 = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='arsal_s4')
thisExp.addLoop(arsal_s4)  # add the loop to the experiment
thisArsal_s4 = arsal_s4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisArsal_s4.rgb)
if thisArsal_s4 != None:
    for paramName in thisArsal_s4:
        exec('{} = thisArsal_s4[paramName]'.format(paramName))

for thisArsal_s4 in arsal_s4:
    currentLoop = arsal_s4
    # abbreviate parameter names if possible (e.g. rgb = thisArsal_s4.rgb)
    if thisArsal_s4 != None:
        for paramName in thisArsal_s4:
            exec('{} = thisArsal_s4[paramName]'.format(paramName))
    
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
    
    # --- Prepare to start Routine "arsal_code_task_3" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from matrix_code_3
    from psychopy import core
    import random
    
    # Colors
    blue = (-1, -1, 1)
    green = (-1, 1, -1)  # slightly “greener” than (0,1,0)
    variable_colors = [
        (1, 1, -1),   # bright yellow (no blue)
        (1, -1, -1),  # bright red
        (1, -0.2, -1),  # bright orange
        (1, -1, 1)    # bright magenta
    ]
    
    # Grid
    n_rows = 3
    n_cols = 3
    grid_size = 0.65
    cell_size = grid_size / n_rows
    square_size = cell_size * 0.9
    
    # Generate sequence with guaranteed repeat
    matrices = []
    for i in range(7):
        matrix_colors = []
    
        # choose exactly two variable colors for this matrix
        chosen_vars = random.sample(variable_colors, 4)
    
        for j in range(9):
            if random.random() < 0.3:
                # blue/green as before
                matrix_colors.append(random.choice([blue, green]))
            else:
                # only from the two chosen variable colors
                matrix_colors.append(random.choice(chosen_vars))
    
        matrices.append(matrix_colors)
    
    # Find repeat
    repeat_idx = None
    for i in range(1, 7):
        set_i = frozenset(c for c in matrices[i] if c not in (blue, green))
        for j in range(i):
            set_j = frozenset(c for c in matrices[j] if c not in (blue, green))
            if set_i == set_j:
                repeat_idx = j
                break
        if repeat_idx:
            break
    
    if not repeat_idx:
        repeat_idx = random.randint(0, 6)
    
    sequence = matrices + [matrices[repeat_idx]]
    
    # Timing
    step_duration = 3.0
    step_index = 0
    step_clock = core.Clock()
    
    
    matrix_resp_3.keys = []
    matrix_resp_3.rt = []
    _matrix_resp_3_allKeys = []
    # keep track of which components have finished
    arsal_code_task_3Components = [hintText_3, matrix_resp_3]
    for thisComponent in arsal_code_task_3Components:
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
    
    # --- Run Routine "arsal_code_task_3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 24.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *hintText_3* updates
        
        # if hintText_3 is starting this frame...
        if hintText_3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            hintText_3.frameNStart = frameN  # exact frame index
            hintText_3.tStart = t  # local t and not account for scr refresh
            hintText_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hintText_3, 'tStartRefresh')  # time at next scr refresh
            # update status
            hintText_3.status = STARTED
            hintText_3.setAutoDraw(True)
        
        # if hintText_3 is active this frame...
        if hintText_3.status == STARTED:
            # update params
            pass
        
        # if hintText_3 is stopping this frame...
        if hintText_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hintText_3.tStartRefresh + 21-frameTolerance:
                # keep track of stop time/frame for later
                hintText_3.tStop = t  # not accounting for scr refresh
                hintText_3.frameNStop = frameN  # exact frame index
                # update status
                hintText_3.status = FINISHED
                hintText_3.setAutoDraw(False)
        # Run 'Each Frame' code from matrix_code_3
        # Draw 3x3 colored squares
        colors = sequence[step_index]
        square_idx = 0
        
        for i in range(3):
            for j in range(3):
                x = -0.325 + j*0.2167 + 0.1083
                y = -0.325 + i*0.2167 + 0.1083
                
                square = visual.Rect(win, width=0.18, height=0.18, 
                                   pos=(x, y), fillColor=colors[square_idx], 
                                   lineColor=colors[square_idx])
                square.draw()
                square_idx += 1
        
        # Advance step
        if step_clock.getTime() >= step_duration:
            step_clock.reset()
            step_index += 1
            if step_index >= 8:
                step_index = 7
        
        
        # *matrix_resp_3* updates
        waitOnFlip = False
        
        # if matrix_resp_3 is starting this frame...
        if matrix_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            matrix_resp_3.frameNStart = frameN  # exact frame index
            matrix_resp_3.tStart = t  # local t and not account for scr refresh
            matrix_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(matrix_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'matrix_resp_3.started')
            # update status
            matrix_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(matrix_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(matrix_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if matrix_resp_3 is stopping this frame...
        if matrix_resp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > matrix_resp_3.tStartRefresh + 24-frameTolerance:
                # keep track of stop time/frame for later
                matrix_resp_3.tStop = t  # not accounting for scr refresh
                matrix_resp_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'matrix_resp_3.stopped')
                # update status
                matrix_resp_3.status = FINISHED
                matrix_resp_3.status = FINISHED
        if matrix_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = matrix_resp_3.getKeys(keyList=['left','right'], waitRelease=False)
            _matrix_resp_3_allKeys.extend(theseKeys)
            if len(_matrix_resp_3_allKeys):
                matrix_resp_3.keys = [key.name for key in _matrix_resp_3_allKeys]  # storing all keys
                matrix_resp_3.rt = [key.rt for key in _matrix_resp_3_allKeys]
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in arsal_code_task_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "arsal_code_task_3" ---
    for thisComponent in arsal_code_task_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from matrix_code_3
    thisExp.addData('sequence', sequence)
    thisExp.addData('repeat_idx', repeat_idx)
    
    # check responses
    if matrix_resp_3.keys in ['', [], None]:  # No response was made
        matrix_resp_3.keys = None
    arsal_s4.addData('matrix_resp_3.keys',matrix_resp_3.keys)
    if matrix_resp_3.keys != None:  # we had a response
        arsal_s4.addData('matrix_resp_3.rt', matrix_resp_3.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-24.000000)
    thisExp.nextEntry()
    
# completed 3.0 repeats of 'arsal_s4'


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
