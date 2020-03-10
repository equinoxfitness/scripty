from datacoco_core.config import config
from datacoco_secretsmanager import SecretsManager

'''
Wrapper file for config management for script_runner.
'''

class ConfigWrapper:

    @staticmethod
    def sm_conf(project_name='maximilian', team_name='data'):
        """
        Simple config wrapper for using secrets manager.
        """
        c = SecretsManager().get_config(project_name, team_name)
        return c

    @staticmethod
    def extend_parser(parser):
        parser.add_argument(
            "-c",
            "--config",
            default="core",
            help="""whether to use secret_manager or datacoco_core to retrieve secrets""",
            choices=['secret_manager', 'core']
        )

        return parser

    @staticmethod
    def process_config(args):
        if args.config == "secret_manager":
            conf = ConfigWrapper.sm_conf()
        elif args.config == "core":
            conf = config()

        db_name = conf[args.database]["db_name"]
        host = conf[args.database]["host"]
        user = conf[args.database]["user"]
        password = conf[args.database]["password"]
        port = conf[args.database]["port"]

        return db_name, host, user, password, port

