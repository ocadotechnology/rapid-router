from game.models import Workspace
from django.http import Http404, HttpResponse
import json

python_default = (
"""
import van

v = van.Van()
"""
)

solutions = {
            'python_default': python_default,
            '1': '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="230" y="30"><next><block type="move_forwards"></block></next></block></xml>',
            '65': '<xml xmlns="http://www.w3.org/1999/xhtml"><block type="start" deletable="false" x="241" y="386"><next><block type="call_proc"><field name="NAME">left-right</field><next><block type="move_forwards"><next><block type="call_proc"><field name="NAME">right-left</field><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="call_proc"><field name="NAME">left-right</field></block></statement><next><block type="move_forwards"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="move_forwards"><next><block type="turn_right"></block></next></block></statement><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="call_proc"><field name="NAME">left-right</field></block></statement><next><block type="call_proc"><field name="NAME">right-left</field><next><block type="move_forwards"><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="move_forwards"><next><block type="turn_left"></block></next></block></statement><next><block type="call_proc"><field name="NAME">right-left</field><next><block type="call_proc"><field name="NAME">left-right</field><next><block type="controls_repeat"><field name="TIMES">2</field><statement name="DO"><block type="move_forwards"></block></statement><next><block type="call_proc"><field name="NAME">left-right</field></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block><block type="declare_proc" x="498" y="501"><field name="NAME">left-right</field><statement name="DO"><block type="turn_left"><next><block type="turn_right"></block></next></block></statement></block><block type="declare_proc" x="496" y="716"><field name="NAME">right-left</field><statement name="DO"><block type="turn_right"><next><block type="turn_left"></block></next></block></statement></block></xml>',
}

def save_workspace_solutions(request):

    workspace = Workspace(owner=request.user.userprofile)
    workspace.id = '115'
    workspace.name = '115'
    workspace.contents = solutions['1']
    workspace.python_contents = solutions['2']
    workspace.blockly_enabled = True
    workspace.python_enabled = False
    space = {'id': workspace.id, 'name': workspace.name, 'blockly_enabled': workspace.blockly_enabled, 'python_enabled': workspace.python_enabled}
    return space

def load_workspace_solution(request, levelName):
    workspace = Workspace(owner=request.user.userprofile)
    workspace.id = '65'
    workspace.name = '65'
    workspace.contents = solutions['65']
    workspace.python_contents = solutions['python_default']
    workspace.blockly_enabled = True
    workspace.python_enabled = False


    return HttpResponse(json.dumps({'contents': workspace.contents,
                                    'python_contents': workspace.python_contents}),
                        content_type='application/json')

    # return HttpResponse(json.dumps(''), content_type='application/json')
