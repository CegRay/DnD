import yaml


class Dumper(yaml.Dumper):

    def increase_indent(self, flow: bool = False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)
