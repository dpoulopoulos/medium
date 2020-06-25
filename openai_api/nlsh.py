prompt = """
    Input: Print the current directory
    Output: pwd

    Input: List files
    Output: ls -l

    Input: Change directory to /tmp
    Output: cd /tmp

    Input: Count files
    Output: ls -l | wc -l

    Input: Replace foo with bar in all python files
    Output: sed -i .bak -- 's/foo/bar/g' *.py

    Input: Push to master
    Output: git push origin master
"""

template = """
    Input: {}
    Output:
"""

import os, click, openai


while True:
    request = input(click.style('nlsh> ', 'red', bold=True))
    prompt += template.format(request)
    result = openai.Completion.create(
        model='davinci', prompt=prompt, stop='/n', max_tokens=100, temperature=.0
    )

    command = result.choices[0]['text']
    prompt += command

    if click.confirm(f'>>> Run: {click.style(command, "blue")}', default=True):
        os.system(command)