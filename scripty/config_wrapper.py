from datacoco_core.config import config
from datacoco_secretsmanager import SecretsManager


class ConfigWrapper:
    """
    Wrapper file for config management for script_runner.
    """

    @staticmethod
    def sm_conf(project_name:str, team_name:str):
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
            help="""
                whether to use secret_manager or
                datacoco_core to retrieve secrets
                """,
            choices=["secret_manager", "core"],
        )

        parser.add_argument(
            "-smp",
            "--secret_project_name",
            default="maximilian3",
            help="""
                secret manager project group
                """
        )

        parser.add_argument(
            "-smt",
            "--secret_team",
            default="data",
            help="""
                secret manager team
                """
        )

        return parser

    @staticmethod
    def process_config(args):
        if args.config == "secret_manager":
            conf = ConfigWrapper.sm_conf(project_name=args.secret_project_name, team_name=args.secret_team)
        elif args.config == "core":
            conf = config()

        db_name = conf[args.database]["db_name"]
        host = conf[args.database]["host"]
        user = conf[args.database]["user"]
        password = conf[args.database]["password"]
        port = conf[args.database]["port"]
        batchy_server = conf["batchy"]["server"]
        batchy_port = conf["batchy"]["port"]

        return db_name, host, user, password, port, batchy_server, batchy_port
