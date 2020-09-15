import argparse

class Arguments:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", "--interface", metavar="IFACE", help="interface for put to monitor mode")
        self.args = parser.parse_args()

        if "None" in str(vars(self.args)):
            parser.print_help()

    def param(self, param):
        if param == "interface":
            return self.args.interface

Arguments()