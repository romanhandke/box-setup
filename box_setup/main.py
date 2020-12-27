import os
import click

plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')


class BoxSetup(click.MultiCommand):
    def list_commands(self, ctx):
        commands = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py'):
                commands.append(filename[:-3])
        commands.sort()
        return commands

    def get_command(self, ctx, cmd_name):
        command = {}
        file_name = os.path.join(plugin_folder, cmd_name + '.py')
        with open(file_name) as file:
            code = compile(file.read(), file_name, 'exec')
            eval(code, command, command)
        return command['cli']


@click.command(cls=BoxSetup, help='Installs packages and configuration files')
def cli():
    pass


if __name__ == '__main__':
    cli()
