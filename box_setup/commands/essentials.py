import subprocess
import click

essential_packages = ['git', 'curl', 'wget', 'bat', 'rip-grep', 'fzf', 'tree']


@click.command()
@click.option('-m',
              '--package_manager',
              required=False,
              default='apt',
              help='Set package manager. Default = apt')
def cli(package_manager):
    '''Install essential packages'''

    base_command = get_command_by_package_manager(package_manager)
    if base_command is not False:
        package_string = ' '
        command = base_command + ' ' + package_string.join(essential_packages)
        try:
            subprocess.run(
                command,
                shell=True,
                check=True,
                stdout=subprocess.PIPE)
        except subprocess.CalledProcessError:
            pass

    else:
        print('[error] Unknown package manager')


def get_command_by_package_manager(name):
    if name == 'apt':
        return 'sudo apt install -y'

    if name == 'pacman':
        return 'sudo pacman -sY'

    return False
