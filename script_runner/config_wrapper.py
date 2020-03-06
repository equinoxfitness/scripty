'''
Wrapper file for config management for script_runner
'''
from datacoco_core.config import config
from datacoco_secretsmanager import SecretsManager


class ConfigWrapper:

    @staticmethod
    def sm_conf(project_name='maximilian', team_name='data'):
        """
        simple config wrapper for using secrets manager
        :return:
        """
        c = SecretsManager().get_config(project_name, team_name)
        return c

    @staticmethod
    def extend_parser(parser):
        parser.add_argument(
            "-c",
            "--config",
            default="secret_manager",
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
        host = conf[args.database]["user"]
        user = conf[args.database]["host"]
        password = conf[args.database]["password"]
        port = conf[args.database]["port"]

        return db_name, host, user, password, port

