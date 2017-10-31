from st22.config import *


# python 3.6
def show_help(actions):
    print('All commands')
    for action in actions:
        print(str(action['value']) + '. ' + action['text'])
    print('exit. To close this thread')


def main():
    RGUNG = University()
    actions = setup(RGUNG)
    while True:
        show_help(actions)
        command = input('wait command...\n')
        if command == 'exit':
            break
        try:
            if 'actions' in actions[int(command)]:
                subactions = actions[int(command)]['actions']
                show_help(subactions)
                sub_command = input('wait sub command...\n')
                if sub_command == 'exit':
                    break
                subactions[int(sub_command)]['func']()
            else:
                actions[int(command)]['func']()
        except ValueError:
            print('Index value is number')
        except IndexError:
            print('Index out of range')
