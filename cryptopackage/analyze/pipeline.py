# from ..pipeline import Pipeline


# def analyze_pipeline(source=None, *, parallel=False, **options):
#     """Analyze package

#     API      | Usage
#     -------- | --------
#     Public   | `from frictionless import analyze_package`

#     Parameters:
#         source (any): a pipeline descriptor
#         **options (dict): Pipeline constructor options

#     Returns:
#         any: the pipeline output
#     """
#     native = isinstance(source, Pipeline)
#     pipeline = source if native else Pipeline(source)
#     return pipeline.run(parallel=parallel)
