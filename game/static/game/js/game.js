'use strict'

var ocargo = ocargo || {}

ocargo.Game = function () {
  this.tabs = null
  this.failures = 0
  this.currentlySelectedTab = null

  if (!hasFunctionalCookiesConsent()) {
    deleteCookie('muted')
    deleteCookie('preferredLanguage')
  }
  this.preferredLanguage = Cookies.get('preferredLanguage')
}

ocargo.Game.prototype.setup = function () {
  document.getElementById("language_dropdown").value = this.preferredLanguage ?? navigator.language.toLowerCase()
  gameUpdateBlockLanguage(this.preferredLanguage ?? navigator.language.toLowerCase())
  this.isMuted = Cookies.get('muted') ?? false

  if(new Date().getMonth() === 11) {
    $("#paper").css('background-color', '#eef7ff')
  }

  if (NIGHT_MODE_FEATURE_ENABLED) {
    if (NIGHT_MODE) {
      $('#paper').css('background-color', 'black')
    }

    if (!ANONYMOUS) {
      $('#nightmode_tab').show()
    }
  }


  // Function being called when there is a change in game level.
  ocargo.Game.prototype.onLevelChange = function() {
    const currentLevelId = LEVEL_ID;
    localStorage.setItem('currentEpisode', EPISODE);
  }

  restoreCmsLogin()
  initCustomBlocks()
  ocargo.solutionLoaded = false
  ocargo.blocklyControl = new ocargo.BlocklyControl()
  ocargo.pythonControl = new ocargo.PythonControl()
  ocargo.blocklyCompiler = new ocargo.BlocklyCompiler()
  ocargo.model = new ocargo.Model(
      PATH,
      ORIGIN,
      DESTINATIONS,
      TRAFFIC_LIGHTS,
      COWS,
      MAX_FUEL
  )

  this.drawing = new ocargo.Drawing(ocargo.model.startingPosition())
  this.drawing.preloadRoadTiles()
  ocargo.animation = new ocargo.Animation(ocargo.model, DECOR, this.drawing)
  this.saving = new ocargo.Saving()
  this.sharing = new ocargo.Sharing(
      () => parseInt(LEVEL_ID),
      () => true
  )

  // Setup the blockly workspace
  ocargo.blocklyControl.reset()
  ocargo.blocklyControl.loadPreviousAttempt()
  ocargo.pythonControl.loadPreviousAttempt()

  // Setup the ui
  this._setupConsoleSliderListeners()
  this._setupPythonViewSliderListeners()
  this._setupConsoleLogViewSliderListeners()
  this._setupFuelGauge(ocargo.model.map.nodes, BLOCKS)
  this._setupTabs()

  this.onStopControls()

  // default controller
  if (BLOCKLY_ENABLED) {
    ocargo.controller = ocargo.blocklyControl
  } else {
    ocargo.controller = ocargo.pythonControl
  }

  // Setup blockly to python
  Blockly.Python.init(Blockly.getMainWorkspace())
  window.addEventListener(
      'unload',
      function (event) {
        ocargo.pythonControl.teardown()
        ocargo.blocklyControl.teardown()
      }.bind(this)
  )

  var loggedOutWarning = ''
  // Check if logged on
  if (USER_STATUS == 'UNTRACKED') {
    loggedOutWarning =
        '<br><span class="popup__text--warning">' +
        gettext("You are not logged in. Your progress won't be saved.") +
        '</span>'
  }
  // Start the popup
  var title = gettext('Try solving this one...')
  if (LEVEL_ID) {
    var titlePrefix = ''
    if (NIGHT_MODE) {
      titlePrefix = gettext('Night Level %(level_name)s')
    } else if (DEFAULT_LEVEL) {
      titlePrefix = gettext('Level %(level_name)s')
    }

    let adjusted_level_name = ''
    if (LEVEL_NAME > 1000) {
      adjusted_level_name = LEVEL_NAME - 1000
    } else {
      adjusted_level_name = LEVEL_NAME;
    }

    if (titlePrefix) {
      title = interpolate(titlePrefix, { level_name: adjusted_level_name }, true)
    } else {
      title = LEVEL_NAME
    }
  }

  var message
  if (NIGHT_MODE) {
    message =
        '<br>' +
        gettext(
            'In Night Mode you can only see a very short distance. ' +
            "We've given you more blocks to help you find your way!"
        )
  } else {
    message = loggedOutWarning
  }

  this.drawing.enablePanning()

  const showMascot = BLOCKLY_ENABLED && !PYTHON_VIEW_ENABLED && LEVEL_NAME <= 80; // show mascot on Blockly-only levels that are not above 80

  const subtitle = SUBTITLE == "None" ? "" : "<b>" + SUBTITLE + "</b> <br> <br> ";
  const next_button_html = NEXT_LEVEL_URL == "/pythonden/" 
    ? ocargo.button.episodeRedirectButtonHtml("next_button", NEXT_LEVEL_URL, gettext('Next episode'), NEXT_EPISODE)
    : ocargo.button.dismissButtonHtml("next_button", gettext('Next level'))
  ocargo.Drawing.startPopup(
      title,
      subtitle + LESSON,
      message,
      showMascot,
      [
        ocargo.button.dismissButtonHtml("prev_button", gettext("Previous level")),
        ocargo.button.dismissButtonHtml('play_button', gettext('Play')),
        next_button_html
      ]
  )
}

// Script used to save and check for episode upon loading of the webpage
document.addEventListener("DOMContentLoaded", function() {
  const dataElement = document.getElementById('data');
  const currentEpisode = dataElement ? dataElement.getAttribute('data-episode') : null;
  if (currentEpisode) {
    localStorage.setItem('currentEpisode', currentEpisode);
  }
});

ocargo.Game.prototype.clearWorkspaceNameInputInSaveTab = function () {
  $('#workspaceNameInput').val('')
}

ocargo.Game.prototype.reset = function () {
  ocargo.blocklyControl.clearAllSelections()

  ocargo.animation.resetAnimation()

  // Needed so animation can reset with the right information
  ocargo.model.reset()

  // clear animations and sound
  ocargo.sound.stop_engine()

  this.clearWorkspaceNameInputInSaveTab()
}

ocargo.Game.prototype.runProgramAndPrepareAnimation = function (blocks) {
  this.reset()
  let code = ocargo.pythonControl.getCode()
  ocargo.event.sendEvent('PlayButtonPressed', {
    levelName: LEVEL_NAME,
    defaultLevel: DEFAULT_LEVEL,
    workspace: ocargo.blocklyControl.serialize(),
    failures: this.failures,
    pythonWorkspace: code
  })

  if (code.match(/^\s*from (?!van import Van)|^\s*import (?!van$)/gm)) {
    ocargo.Drawing.startPopup(
      gettext('Oh dear!'),
      "You can only import 'Van' from 'van'",
      ''
    )
    return false
  }

  var result = ocargo.controller.prepare(blocks)
  if (!result.success) {
    ocargo.sound.tension()
    ocargo.Drawing.startPopup(gettext('Oh dear!'), '', result.error)
    return false
  }
  var program = result.program

  ocargo.blocklyControl.resetIncorrectBlock()

  // Starting sound
  ocargo.animation.appendAnimation({
    type: 'callable',
    functionType: 'playSound',
    functionCall: ocargo.sound.starting,
    description: 'starting sound',
    animationLength: 820
  })
  ocargo.animation.startNewTimestamp()

  ocargo.animation.appendAnimation({
    type: 'callable',
    functionType: 'playSound',
    functionCall: ocargo.sound.start_engine,
    description: 'starting engine'
  })

  program.run(ocargo.model)
  // Set controls ready for user to reset
  ocargo.animation.appendAnimation({
    type: 'callable',
    functionType: 'onStopControls',
    functionCall: this.onStopControls.bind(this),
    description: 'onStopControls'
  })

  ocargo.animation.appendAnimation({
    type: 'callable',
    functionType: 'playSound',
    functionCall: ocargo.sound.stop_engine,
    description: 'stopping engine'
  })

  return true
}

ocargo.Game.prototype.sendAttempt = function (score) {
  function csrfSafeMethod (method) {
    // these HTTP methods do not require CSRF protection
    return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method)
  }

  // TODO: Remove below - keeping it for now as a reminder that we need to
  //  implement some kind of algorithm score for Python levels.
  // // hack scores so that it works for demo and python TODO implement max scores and remove this!!
  // if (PYTHON_ENABLED) {
  //   score *= 2
  // }

  // Check that we should actually be sending an attempt - either if only blockly is enabled
  // or if python is enabled and we're on the python tab (assumes they don't change tab quickly...)
  if (
    (BLOCKLY_ENABLED && !PYTHON_ENABLED) ||
    (PYTHON_ENABLED && this.isInPythonWorkspace())
  ) {
    // Send out the submitted data.
    if (LEVEL_ID) {
      var csrftoken = Cookies.get('csrftoken')
      $.ajax({
        url: Urls.submit_attempt(),
        type: 'POST',
        dataType: 'json',
        beforeSend: function (xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken)
          }
        }.bind(this),
        data: {
          nightmode: NIGHT_MODE ? 'True' : 'False',
          level: parseInt(LEVEL_ID),
          score: score,
          workspace: ocargo.blocklyControl.serialize(),
          python_workspace: ocargo.pythonControl.getCode()
        },
        error: function (xhr, errmsg, err) {
          console.error(
            xhr.status + ': ' + errmsg + ' ' + err + ' ' + xhr.responseText
          )
        }.bind(this)
      })
    }
  }
}

ocargo.Game.prototype.registerFailure = function () {
  this.failures += 1
  return this.failures >= 1
}

ocargo.Game.prototype._setupFuelGauge = function (nodes, blocks) {
  if (FUEL_GAUGE) {
    if (CHARACTER_NAME == "Electric van") {
      document.getElementById("electricFuelGauge").style.visibility = "visible"
    } else {
      document.getElementById("fuelGauge").style.visibility = "visible"
    }

    // TODO: Investigate these for loops - are they necessary?
    for (var i = 0; i < blocks.length; i++) {
      if (blocks[i].type === 'turn_around' || blocks[i].type === 'wait') {
        return
      }
    }

    for (var i = 0; i < nodes.length; i++) {
      if (nodes[i].connectedNodes.length > 2) {
        return
      }
    }
  }
}

ocargo.Game.prototype._setupConsoleSliderListeners = function () {
  let tabsWidth = $('#tabs').width()

  let startEvents = ['mousedown', 'touchstart']
  let moveEvents = ['mousemove', 'touchmove']
  let endEvents = ['mouseup', 'touchend', 'touchcancel']

  let slider = $('#consoleSlider')
  let tabs = $('#tabs')
  let halfSliderWidth

  let endFunc = function (e) {
    for (let i = 0; i < moveEvents.length; i++) {
      slider.parent().off(moveEvents[i])
      tabs.off(moveEvents[i])
    }

    for (let i = 0; i < endEvents.length; i++) {
      // disable drag when mouse leaves this or the parent
      slider.parent().off(endEvents[i], endFunc)
      tabs.off(endEvents[i], endFunc)
    }

    ocargo.blocklyControl.redrawBlockly()
  }

  let moveFunc = function (e) {
    if (e.type == 'touchmove') {
      e = e.originalEvent.touches[0]
    }

    let consoleSliderPosition = e.pageX - tabsWidth - halfSliderWidth
    let containerWidth = slider.parent().width()

    consoleSliderPosition *= 100.0 / containerWidth

    if (consoleSliderPosition > 100) {
      consoleSliderPosition = 100
    }
    if (consoleSliderPosition < 0) {
      consoleSliderPosition = 0
    }

    $('#consoleSlider').css('left', consoleSliderPosition + '%')
    $('#paper').css('width', 100 - consoleSliderPosition + '%')
    $('#tab_panes').css('width', consoleSliderPosition + '%')

    ocargo.blocklyControl.redrawBlockly()
  }

  let startFunc = function (e) {
    halfSliderWidth = slider.width() / 2

    for (let i = 0; i < moveEvents.length; i++) {
      slider.parent().on(moveEvents[i], moveFunc)
      tabs.on(moveEvents[i], moveFunc)
    }

    for (let i = 0; i < endEvents.length; i++) {
      // disable drag when mouse leaves this or the parent
      slider.parent().on(endEvents[i], endFunc)
      tabs.on(endEvents[i], endFunc)
    }

    // close trashcan flyout on resize as it doesn't redraw with the workspace
    Blockly.mainWorkspace.trashcan.flyout_.setVisible(false)
  }

  for (let i = 0; i < startEvents.length; i++) {
    slider.on(startEvents[i], startFunc)
  }
}

ocargo.Game.prototype._setupConsoleLogViewSliderListeners = function () {
  let startEvents = ['mousedown', 'touchstart']
  let moveEvents = ['mousemove', 'touchmove']
  let endEvents = ['mouseup', 'touchend', 'touchcancel']

  let codeWindow = $("#code").next()
  let slider = $('#consoleLogSlider')
  let wrapper = $('#wrapper')
  let halfSliderHeight = slider.height()

  let endFunc = function (e) {
    moveEvents.map((moveEvent) => wrapper.off(moveEvent))
    endEvents.map((endEvent) => wrapper.off(endEvent, endFunc))

    ocargo.blocklyControl.redrawBlockly()
  }

  let moveFunc = function (e) {
    if (e.type == 'touchmove') {
      e = e.originalEvent.touches[0]
    }

    let pythonSliderPosition = e.pageY - halfSliderHeight
    let containerHeight = slider.parent().height()

    pythonSliderPosition *= 100.0 / containerHeight
    let codeWindowHeight = pythonSliderPosition

    if (pythonSliderPosition > 75) {
      pythonSliderPosition = 75
      codeWindowHeight = 75
    }
    if (pythonSliderPosition < 30) {
      pythonSliderPosition = 30
      codeWindowHeight = 30
    }

    slider.css('top', pythonSliderPosition + '%')
    codeWindow.css("height", `100%`)
    $('#editor').css('height', pythonSliderPosition + '%')

    ocargo.blocklyControl.redrawBlockly()
  }

  let startFunc = function (e) {
    moveEvents.map((moveEvent) => wrapper.on(moveEvent, moveFunc))
    // disable drag when mouse leaves the wrapper
    endEvents.map((endEvent) => wrapper.on(endEvent, endFunc))

    // close trashcan flyout on resize as it doesn't redraw with the workspace
    Blockly.mainWorkspace.trashcan.flyout_.setVisible(false)
  }

  startEvents.map((startEvent) => slider.on(startEvent, startFunc))
}

ocargo.Game.prototype._setupPythonViewSliderListeners = function () {
  let startEvents = ['mousedown', 'touchstart']
  let moveEvents = ['mousemove', 'touchmove']
  let endEvents = ['mouseup', 'touchend', 'touchcancel']

  let slider = $('#pythonViewSlider')
  let wrapper = $('#wrapper')
  let halfSliderHeight = slider.height() / 2

  let endFunc = function (e) {
    moveEvents.map((moveEvent) => wrapper.off(moveEvent))
    endEvents.map((endEvent) => wrapper.off(endEvent, endFunc))

    ocargo.blocklyControl.redrawBlockly()
  }

  let moveFunc = function (e) {
    if (e.type == 'touchmove') {
      e = e.originalEvent.touches[0]
    }

    let pythonSliderPosition = e.pageY - halfSliderHeight
    let containerHeight = slider.parent().height()

    pythonSliderPosition *= 100.0 / containerHeight

    if (pythonSliderPosition > 100) {
      pythonSliderPosition = 100
    }
    if (pythonSliderPosition < 0) {
      pythonSliderPosition = 0
    }

    slider.css('top', pythonSliderPosition + '%')
    $('#blockly_holder').css('height', pythonSliderPosition + '%')
    $('#pythonView_holder').css('height', 100 - pythonSliderPosition + '%')

    ocargo.blocklyControl.redrawBlockly()
  }

  let startFunc = function (e) {
    moveEvents.map((moveEvent) => wrapper.on(moveEvent, moveFunc))
    // disable drag when mouse leaves the wrapper
    endEvents.map((endEvent) => wrapper.on(endEvent, endFunc))

    // close trashcan flyout on resize as it doesn't redraw with the workspace
    Blockly.mainWorkspace.trashcan.flyout_.setVisible(false)
  }

  startEvents.map((startEvent) => slider.on(startEvent, startFunc))
}

const buttonTransit = (buttonElementId, state) => {
    const dir = "/static/game/image/icons/"
    let [firstElement, secondElement] = document.getElementById(buttonElementId).children
    let buttonImage = firstElement.tagName === "IMG" ? firstElement : secondElement
    let buttonSpan = buttonImage === firstElement ? secondElement : firstElement

    if (state === "running") {
        buttonSpan.innerHTML = "Pause"
        buttonImage.src= dir + "pause.svg"
    }
    else {
        buttonSpan.innerHTML = "Run code"
        buttonImage.src = dir + "play.svg"
    }
}

ocargo.Game.prototype.onPlayControls = function () {
  this.disallowCodeChanges()

  this.tabs.play.transitTo('running')
  buttonTransit("run-code-button", "running")
  this.tabs.step.disable()
  this.tabs.fast.enable()

  this.tabs.load.disable()
  this.tabs.save.disable()
  this.tabs.clear_program.disable()
  this.tabs.help.disable()
}

ocargo.Game.prototype.onStepControls = function () {
  this.disallowCodeChanges()

  this.tabs.play.transitTo('paused')
  buttonTransit("run-code-button", "paused")
  this.tabs.step.disable()

  this.tabs.load.disable()
  this.tabs.save.disable()
  this.tabs.clear_program.disable()
  this.tabs.help.disable()
}

ocargo.Game.prototype.onFastControls = function () {
  this.disallowCodeChanges()

  this.tabs.play.transitTo('running')
  buttonTransit("run-code-button", "running")
  this.tabs.fast.transitTo('fast')
  this.tabs.step.disable()

  this.tabs.load.disable()
  this.tabs.save.disable()
  this.tabs.clear_program.disable()
  this.tabs.help.disable()
}

ocargo.Game.prototype.onSlowControls = function () {
  this.disallowCodeChanges()

  this.tabs.play.transitTo('running')
  buttonTransit("run-code-button", "running")
  this.tabs.fast.transitTo('slow')
  this.tabs.step.disable()

  this.tabs.load.disable()
  this.tabs.save.disable()
  this.tabs.clear_program.disable()
  this.tabs.help.disable()
}

ocargo.Game.prototype.mute = function (mute) {
  this.isMuted = mute
  setMutedCookie(mute)
  if (mute) {
    ocargo.sound.mute()
    this.tabs.mute.transitTo('muted')
  } else {
    ocargo.sound.unmute()
    this.tabs.mute.transitTo('unmuted')
  }
}

ocargo.Game.prototype.isInBlocklyWorkspace = function () {
  return this.isInBlocklyWorkspace()
}

ocargo.Game.prototype.isInPythonWorkspace = function () {
  return this.isInPythonWorkspace()
}

ocargo.Game.prototype._setupTabs = function () {
  this.tabs = []

  this.tabs.blockly = new ocargo.Tab(
    $('#blockly_radio'),
    $('#blockly_radio + label'),
    $('#blockly_pane')
  )
  this.tabs.python = new ocargo.Tab(
    $('#python_radio'),
    $('#python_radio + label'),
    $('#python_pane')
  )

  this.tabs.play = new ocargo.Tab($('#play_radio'), $('#play_radio + label'))
  this.tabs.play
    .addState(
      'readyToPlay',
      ocargo.Drawing.imageDir + 'icons/play.svg',
      gettext('Play')
    )
    .addState(
      'running',
      ocargo.Drawing.imageDir + 'icons/pause.svg',
      gettext('Pause')
    )
    .addState(
      'paused',
      ocargo.Drawing.imageDir + 'icons/play.svg',
      gettext('Resume')
    )

  this.tabs.stop = new ocargo.Tab($('#stop_radio'), $('#stop_radio + label'))
  this.tabs.fast = new ocargo.Tab($('#fast_radio'), $('#fast_radio + label'))
  this.tabs.fast
    .addState(
      'slow',
      ocargo.Drawing.imageDir + 'icons/fast.svg',
      gettext('Fast')
    )
    .addState(
      'fast',
      ocargo.Drawing.imageDir + 'icons/slow.svg',
      gettext('Slow')
    )
  this.tabs.step = new ocargo.Tab($('#step_radio'), $('#step_radio + label'))

  this.tabs.load = new ocargo.Tab(
    $('#load_radio'),
    $('#load_radio + label'),
    $('#load_pane')
  )
  this.tabs.save = new ocargo.Tab(
    $('#save_radio'),
    $('#save_radio + label'),
    $('#save_pane')
  )
  this.tabs.clear_program = new ocargo.Tab(
    $('#clear_program_radio'),
    $('#clear_program_radio + label')
  )

  // this.tabs.big_code_mode = new ocargo.Tab($('#big_code_mode_radio'), $('#big_code_mode_radio + label'));
  // this.tabs.big_code_mode.addState('normal_code_mode', ocargo.Drawing.imageDir + 'icons/big_code_mode.svg', gettext('Enlarge'))
  //                        .addState('big_code_mode', ocargo.Drawing.imageDir + 'icons/big_code_mode.svg', gettext('Shrink'));
  // this.tabs.print = new ocargo.Tab($('#print_radio'), $('#print_radio + label'));
  this.tabs.mute = new ocargo.Tab($('#mute_radio'), $('#mute_radio + label'))
  this.tabs.mute
    .addState(
      'muted',
      ocargo.Drawing.imageDir + 'icons/muted.svg',
      gettext('Unmute')
    )
    .addState(
      'unmuted',
      ocargo.Drawing.imageDir + 'icons/unmuted.svg',
      gettext('Mute')
    )
  this.tabs.help = new ocargo.Tab($('#help_radio'), $('#help_radio + label'))
  this.tabs.quit = new ocargo.Tab($('#quit_radio'), $('#quit_radio + label'))
  this.tabs.nightmode = new ocargo.Tab(
    $('#nightmode_radio'),
    $('#nightmode_radio + label')
  )

  this._setupBlocklyTab()
  this._setupPythonTab()
  this._setupClearTab()
  this._setupPlayTab()
  this._setupStopTab()
  this._setupFastTab()
  this._setupStepTab()

  this._setupLoadTab()
  this._setupSaveTab()
  //this._setupPrintTab();
  this._setupHelpTab()
  this._setupMuteTab()
  this._setupQuitTab()
  this._setupNightModeTab()

  if (USER_STATUS === 'TEACHER' && DEFAULT_LEVEL) {
    this.tabs.solution = new ocargo.Tab(
      $('#solution_radio'),
      $('#solution_radio + label')
    )
    this._setupSolutionTab()
    $('#solution_tab').show()
  }

  if (USER_STATUS === 'TEACHER' && !DEFAULT_LEVEL) {
    this.tabs.share = new ocargo.Tab(
      $('#share_radio'),
      $('#share_radio + label'),
      $('#share_pane')
    )
    this._setupShareTab()
  }

  if (!BLOCKLY_ENABLED) {
    $('#python_radio').click()
  }
}

ocargo.Game.prototype.changeTabSelectionTo = function (tab) {
  var previouslySelected = this.currentlySelectedTab
  previouslySelected.setPaneEnabled(false)
  tab.setPaneEnabled(true)
  this.currentlySelectedTab = tab
  return previouslySelected
}

ocargo.Game.prototype.isInBlocklyWorkspace = function () {
  return this.currentlySelectedTab == this.tabs.blockly
}

ocargo.Game.prototype.isInPythonWorkspace = function () {
  return this.currentlySelectedTab == this.tabs.python
}

ocargo.Game.prototype.onResumeControls = function () {
  this.tabs.play.transitTo('running')
  buttonTransit("run-code-button", "running")
  this.tabs.step.disable()
}

ocargo.Game.prototype.onPauseControls = function () {
  this.tabs.play.transitTo('paused')
  buttonTransit("run-code-button", "paused")
  this.tabs.step.enable()
}

ocargo.Game.prototype.onStopControls = function () {
  this.allowCodeChanges()

  this.tabs.play.transitTo('readyToPlay')
  buttonTransit("run-code-button", "readyToPlay")
  this.tabs.fast.transitTo('slow')
  ocargo.animation.setRegularSpeed()
  this.tabs.step.enable()

  this.tabs.load.enable()
  this.tabs.save.enable()
  this.tabs.clear_program.enable()
  this.tabs.help.enable()
}

ocargo.Game.prototype._setupBlocklyTab = function () {
  this.tabs.blockly.setOnChange(
    function () {
      var tab = this.tabs.blockly

      this.changeTabSelectionTo(tab)

      ocargo.blocklyControl.redrawBlockly()
      // reset blockly to python converter
      Blockly.Python.init(Blockly.getMainWorkspace())
      ocargo.controller = ocargo.blocklyControl
    }.bind(this)
  )

  this.currentlySelectedTab = this.tabs.blockly
  this.tabs.blockly.select()
}

ocargo.Game.prototype.allowCodeChanges = function () {
  this._setCodeChangesAllowed(true)
}

ocargo.Game.prototype.disallowCodeChanges = function () {
  this._setCodeChangesAllowed(false)
}

// function to enable or disable pointerEvents on running python or blockly code
ocargo.Game.prototype._setCodeChangesAllowed = function (changesAllowed) {
  ocargo.blocklyControl.setCodeChangesAllowed(changesAllowed)

  var codeMirrors = document.getElementsByClassName('CodeMirror')
  for (i = 0; i < codeMirrors.length; i++) {
    codeMirrors[i].style.pointerEvents = changesAllowed ? '' : 'none'
  }
}

ocargo.Game.prototype._setupPythonTab = function () {
  $('#clear_console').click(
    function (e) {
      $('#consoleOutput').text('')
    }.bind(this)
  )
// --------- Commands for popup ---------------------------------------------------
  var leadMsg =
    '<p style="font-size: 20px;">' +
    interpolate(
      gettext(
        'Run the following commands on the van object %(var_name)s, e.g. %(example)s'
      ),
      { var_name: 'v', example: 'my_van.move_forwards()' },
      true
    ) +
    '</p>' +
    COMMANDS
// -----------------------------------------------------------------------------
  $('#van_commands_help').click(
    function (e) {
      ocargo.Drawing.startPopup(gettext('Python Commands'), leadMsg, '')
    }.bind(this)
  )

  $('#convert_from_blockly').click(
    function (e) {
      ocargo.pythonControl.appendCode(
        ocargo.blocklyCompiler.workspaceToPython()
      )
    }.bind(this)
  )

  this.tabs.python.setOnChange(
    function () {
      // Only clear console when changing *to* python?
      if (!this.isInPythonWorkspace()) {
        $('#clear_console').click()
      }
      this.changeTabSelectionTo(this.tabs.python)

      ocargo.controller = ocargo.pythonControl
    }.bind(this)
  )
}

ocargo.Game.prototype._setupClearTab = function () {
  this.tabs.clear_program.setOnChange(
    function () {
      if (this.isInBlocklyWorkspace()) {
        ocargo.blocklyControl.reset()
      }
      if (this.isInPythonWorkspace()) {
        ocargo.pythonControl.reset()
      }
      this.reset()

      this._selectPreviousTab()
    }.bind(this)
  )
}

ocargo.Game.prototype._resetAndPrepareAnimation = function (
  onSuccess,
  onFailure
) {
  this.reset()
  if (this.runProgramAndPrepareAnimation()) {
    $('#clear_console').click()
    if (onSuccess) {
      onSuccess()
    }
  } else if (onFailure) {
    onFailure()
  }
}

ocargo.Game.prototype._setupPlayTab = function () {
  this.tabs.play.setOnChange(
    function () {
      if (this.tabs.play.isInState('readyToPlay')) {
        this._resetAndPrepareAnimation(
          function () {
            this.onPlayControls()
            ocargo.animation.playAnimation()
          }.bind(this)
        )
      } else if (this.tabs.play.isInState('running')) {
        this.onPauseControls()
        ocargo.animation.pauseAnimation()
      } else if (this.tabs.play.isInState('paused')) {
        // Important ordering
        this.onResumeControls()
        ocargo.animation.playAnimation()
      }

      this._selectPreviousTab()
    }.bind(this)
  )
}

ocargo.Game.prototype._setupStopTab = function () {
  this.tabs.stop.setOnChange(
    function () {
      this.reset()
      this.onStopControls()

      this._selectPreviousTab()
    }.bind(this)
  )
}

ocargo.Game.prototype._setupFastTab = function () {
  this.tabs.fast.setOnChange(
    function () {
      var flipFastSlow = function () {
        if (this.tabs.fast.isInState('slow')) {
          this.onFastControls()
          ocargo.animation.setHighSpeed()
        } else {
          this.onSlowControls()
          ocargo.animation.setRegularSpeed()
        }
      }.bind(this)

      if (this.tabs.play.isInState('readyToPlay')) {
        this._resetAndPrepareAnimation(
          function () {
            flipFastSlow()
            ocargo.animation.playAnimation()
          }.bind(this)
        )
      } else if (this.tabs.play.isInState('paused')) {
        flipFastSlow()
        ocargo.animation.playAnimation()
      } else if (this.tabs.play.isInState('running')) {
        flipFastSlow()
      }

      this._selectPreviousTab()
    }.bind(this)
  )
}

ocargo.Game.prototype._setupStepTab = function () {
  this.tabs.step.setOnChange(
    function () {
      if (this.tabs.play.isInState('readyToPlay')) {
        this._resetAndPrepareAnimation()
      }

      ocargo.animation.stepAnimation(
        function () {
          if (ocargo.animation.isFinished()) {
            this.onStopControls()
          } else {
            this.onPauseControls()
          }
        }.bind(this)
      )

      this.onStepControls()
      this._selectPreviousTab()
    }.bind(this)
  )
}

ocargo.Game.prototype._selectPreviousTab = function () {
  this.currentlySelectedTab.select()
}

ocargo.Game.prototype._setupSolutionTab = function () {
  this.tabs.solution.setOnChange(
    function () {
      this._goToWorkspace()

      this.saving.loadSolution(
        LEVEL_NAME,
        function (err, workspace) {
          if (err !== null) {
            ocargo.Drawing.startInternetDownPopup()
            console.error(err)
            return
          }
          if (BLOCKLY_ENABLED) {
            ocargo.blocklyControl.deserialize(workspace.contents)
            ocargo.blocklyControl.redrawBlockly()
          }
          if (PYTHON_ENABLED) {
            ocargo.pythonControl.setCode(workspace.python_contents)
          }
          ocargo.solutionLoaded = true
        }.bind(this)
      )
    }.bind(this)
  )
}

ocargo.Game.prototype._setupLoadTab = function () {
  var selectedWorkspace = null
  this.tabs.load.setOnChange(
    function () {
      this.changeTabSelectionTo(this.tabs.load)

      selectedWorkspace = null
      // TODO Disable the tab to stop users clicking it multiple times
      // whilst waiting for the table data to load
      // JQuery currently throwing errors :(

      this.saving.retrieveListOfWorkspaces(
        function (err, workspaces) {
          if (err !== null) {
            ocargo.Drawing.startInternetDownPopup()
            console.error(err)
            return
          }

          loadInWorkspaces.call(this, workspaces)
        }.bind(this)
      )
    }.bind(this)
  )

  function loadSelectedWorkspace () {
    if (selectedWorkspace) {
      // Blockly or Python tab must be selected before domToWorkspace is called
      // Otherwise blocks will be chopped off or python editor will not be updated
      this._goToWorkspace()

      this.saving.retrieveWorkspace(
        selectedWorkspace,
        function (err, workspace) {
          if (err !== null) {
            ocargo.Drawing.startInternetDownPopup()
            console.error(err)
            return
          }
          if (BLOCKLY_ENABLED) {
            ocargo.blocklyControl.deserialize(workspace.contents)
            ocargo.blocklyControl.redrawBlockly()
          }
          if (PYTHON_ENABLED) {
            ocargo.pythonControl.setCode(workspace.python_contents)
          }
        }.bind(this)
      )
    }
  }

  $('#loadWorkspace').click(loadSelectedWorkspace.bind(this))

  $('#deleteWorkspace').click(
    function () {
      if (selectedWorkspace) {
        this.saving.deleteWorkspace(selectedWorkspace, function (
          err,
          workspaces
        ) {
          if (err !== null) {
            ocargo.Drawing.startInternetDownPopup()
            console.error(err)
            return
          }

          loadInWorkspaces.call(this, workspaces)
        }.bind(this)
        )
      }
    }.bind(this)
  )

  function loadInWorkspaces (workspaces) {
    this._populateTable('loadWorkspaceTable', workspaces)

    // Add click listeners to all rows
    var rows = $('#loadWorkspaceTable tr')
    rows.on('click', function () {
      rows.attr('selected', false)
      $(this).attr('selected', true)
      selectedWorkspace = $(this).attr('value')
      $('#loadWorkspace').removeAttr('disabled')
      $('#deleteWorkspace').removeAttr('disabled')
    })

    // Add double click listener to load the workspace selected by the first click
    rows.on('dblclick', loadSelectedWorkspace.bind(this))

    var empty = workspaces.length === 0
    $('#load_pane .scrolling-table-wrapper').css(
      'display',
      empty ? 'none' : 'block'
    )
    $('#load_pane #does_not_exist').css('display', empty ? 'block' : 'none')

    // But disable all the modal buttons as nothing is selected yet
    selectedWorkspace = null
    $('#loadWorkspace').attr('disabled', 'disabled')
    $('#deleteWorkspace').attr('disabled', 'disabled')
  }
}

ocargo.Game.prototype._setupSaveTab = function () {
  var selectedWorkspace = null

  this.tabs.save.setOnChange(
    function () {
      this.changeTabSelectionTo(this.tabs.save)

      selectedWorkspace = null

      // TODO Disable the tab to stop users clicking it multiple times
      // whilst waiting for the table data to load
      // JQuery currently throwing errors :()

      this.saving.retrieveListOfWorkspaces(
        function (err, workspaces) {
          if (err !== null) {
            ocargo.Drawing.startInternetDownPopup()
            console.error(err)
            return
          }

          loadInWorkspaces.call(this, workspaces)
        }.bind(this)
      )
    }.bind(this)
  )

  function saveWorkspace () {
    var newName = $('#workspaceNameInput').val()
    if (newName && newName !== '') {
      var table = $('#saveWorkspaceTable')
      var existingID = null

      for (var i = 0; i < table[0].rows.length; i++) {
        var row = table[0].rows[i]
        var existingName = row.cells[0].innerHTML
        if (existingName === newName) {
          existingID = row.getAttribute('value')
          break
        }
      }
      var workspace = {
        name: newName,
        contents: ocargo.blocklyControl.serialize(),
        python_contents: ocargo.pythonControl.getCode(),
        blockly_enabled: BLOCKLY_ENABLED,
        python_enabled: PYTHON_ENABLED,
        python_view_enabled: PYTHON_VIEW_ENABLED
      }

      this.saving.saveWorkspace(
        workspace,
        existingID,
        function (err, workspaces) {
          if (err !== null) {
            ocargo.Drawing.startInternetDownPopup()
            console.error(err)
            loadInWorkspaces.call(this, workspaces)
          } else {
            // Blockly or Python tab must be selected before domToWorkspace is called
            // Otherwise blocks will be chopped off or python editor will not be updated
            this._goToWorkspace()
          }
        }.bind(this)
      )
    }
  }

  $('#saveWorkspace').click(saveWorkspace.bind(this))

  // If the user pressed the enter key in the textbox, should be the same as clicking the button
  $('#newWorkspaceName').on('keypress', function (e) {
    if (e.which == 13) {
      $('#saveWorkspace').trigger('click')
    }
  })

  function loadInWorkspaces (workspaces) {
    this._populateTable('saveWorkspaceTable', workspaces)

    // Add click listeners to all rows
    var rows = $('#saveWorkspaceTable tr')
    rows.on('click', function (event) {
      rows.attr('selected', false)
      $(this).attr('selected', true)
      selectedWorkspace = $(event.target).attr('value')
      var workspaceName = $(event.target)[0].innerHTML
      document.getElementById('workspaceNameInput').value = workspaceName
    })

    // Add double click listener to save the workspace selected by the first click
    rows.on('dblclick', saveWorkspace.bind(this))

    $('#save_pane .scrolling-table-wrapper').css(
      'display',
      workspaces.length === 0 ? 'none' : 'block'
    )
    // But disable all the modal buttons as nothing is selected yet
    selectedWorkspace = null
  }
}

ocargo.Game.prototype._setupShareTab = function () {
  // Setup the behaviour for when the tab is selected
  this.tabs.share.setOnChange(function() {
    this.saving.getSharingInformation(parseInt(LEVEL_ID), function(error, validRecipients) {
          if(error) {
              console.error(error);
              return;
          }

          this.changeTabSelectionTo(this.tabs.share);
          this.sharing.processSharingInformation(error, validRecipients);
      }.bind(this));
  }.bind(this));

  this.sharing.setupTeacherPanel();
  this.sharing.setupSelectAllButton();
}

ocargo.Game.prototype._setupHelpTab = function () {
  this.tabs.help.setOnChange(
    function () {
      this._selectPreviousTab()
      ocargo.Drawing.startPopup('', '', HINT)
    }.bind(this)
  )
}

ocargo.Game.prototype._setupMuteTab = function () {
  this.tabs.mute.setOnChange(
    function () {
      this.mute(!this.isMuted)
      this._selectPreviousTab()
    }.bind(this)
  )
}

ocargo.Game.prototype._setupQuitTab = function () {
  this.tabs.quit.setOnChange(
    function () {
      window.location.href = RETURN_URL
    }.bind(this)
  )
}

ocargo.Game.prototype._setupNightModeTab = function () {
  this.tabs.nightmode.setOnChange(
    function () {
      window.location.href = FLIP_NIGHT_MODE_URL
    }.bind(this)
  )
}

// Helper method for load and save tabs
ocargo.Game.prototype._populateTable = function (tableName, workspaces) {
  var table = $('#' + tableName),
    sortedWorkspaces = []

  // Remove click listeners to avoid memory leak and remove all rows
  $('#' + tableName + ' td').off('click')
  table.empty()

  // Order them alphabetically
  sortedWorkspaces = ocargo.utils.sortObjects(workspaces, 'name')
  workspaces = sortedWorkspaces

  // Add a row to the table for each workspace saved in the database
  for (var i = 0, ii = workspaces.length; i < ii; i++) {
    var workspace = workspaces[i]
    if (
      (!workspace.blockly_enabled && !workspace.python_enabled) ||
      (workspace.blockly_enabled && BLOCKLY_ENABLED) ||
      (workspace.python_enabled && PYTHON_ENABLED)
    ) {
      var row = $('<tr></tr>')
        .attr({ value: workspace.id })
        .appendTo(table)
      $('<td></td>')
        .attr({ id: workspace.name })
        .text(workspace.name)
        .appendTo(row)
    }
    // Add a function to make it work for old levels with defaults to false.
  }
}

ocargo.Game.prototype._goToWorkspace = function () {
  if (PYTHON_ENABLED) {
    this.tabs.python.select()
  }
  if (BLOCKLY_ENABLED) {
    this.tabs.blockly.select()
  }
}

function restoreCmsLogin () {
  $('#id_cms-password')
    .css('height', '20px')
    .css('display', 'inline')
  $('#id_cms-username')
    .css('height', '20px')
    .css('display', 'inline')
}

function hasFunctionalCookiesConsent() {
  try {
    return OnetrustActiveGroups.split(',').includes('C0003')
  } catch (e) {
    console.error(e)
  }
  return false
}

function setMutedCookie(mute) {
  if (hasFunctionalCookiesConsent()) {
    if (mute) {
      Cookies.set('muted', true)
    }
    else {
      deleteCookie('muted')
    }
  }
}

function deleteCookie(name) {
  // Set cookie expiry to yesterday, browser will remove the cookie.
  // https://www.quirksmode.org/js/cookies.html
  Cookies.set(name, "", { expires: -1 })
}

function gameUpdateBlockLanguage (language_code) {
  loadLanguage("/static/game/js/blockly/msg/js/", language_code, function() {
    reloadWorkspace(Blockly.mainWorkspace);
  });
}

function gameUpdateBlockLanguageAndCookie (language_code) {
  if (hasFunctionalCookiesConsent()) {
    Cookies.set("preferredLanguage", language_code)
  }
  gameUpdateBlockLanguage(language_code)
}

$(document).ready(function () {
  ocargo.game = new ocargo.Game()
  ocargo.game.setup()
  ocargo.game.mute(ocargo.game.isMuted)
})
