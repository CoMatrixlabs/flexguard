from importlib import import_module
from ..system import system
from .. import errors


def analyze(source=None, type=None, **options):
    """analyze resource
    Parameters:
        source (any): data source
        type (str): source type - package, resource or pipeline (default: infer)
        **options (dict): options for the underlaying function

    Returns:
        any: the transform result
    """
    if not type:
        type = "pipeline"
        if options:
            file = system.create_file(source, basepath=options.get("basepath", ""))
            if file.type in ["table", "resource"]:
                type = "resource"
            elif file.type == "package":
                type = "package"
    module = import_module("frictionless.analyze")
    analyze = getattr(module, "analyze_%s" % type, None)
    if analyze is None:
        note = f"Not supported analyze type: {type}"
        raise Exception(errors.GeneralError(note=note))
    return analyze(source, **options)
