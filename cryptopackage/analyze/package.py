# import types
# from ..step import Step
# from ..system import system
# from ..package import Package
# from ..helpers import get_name
# from ..exception import FrictionlessException
# from .. import errors


# def analyze_package(source=None, *, steps, **options):
#     """Analyze package

#     API      | Usage
#     -------- | --------
#     Public   | `from frictionless import analyze_package`

#     Parameters:
#         source (any): data source
#         steps (Step[]): analyze steps
#         **options (dict): Package constructor options

#     Returns:
#         Package: the transform result
#     """

#     # Prepare package
#     native = isinstance(source, Package)
#     package = source.to_copy() if native else Package(source, **options)
#     package.infer()

#     # Prepare steps
#     for index, step in enumerate(steps):
#         if not isinstance(step, Step):
#             steps[index] = (
#                 Step(function=step)
#                 if isinstance(step, types.FunctionType)
#                 else system.create_step(step)
#             )

#     # Validate steps
#     for step in steps:
#         if step.metadata_errors:
#             raise FrictionlessException(step.metadata_errors[0])

#     # Run analyze
#     for step in steps:

#         # analyze
#         try:
#             step.analyze_package(package)
#         except Exception as exception:
#             error = errors.StepError(note=f'"{get_name(step)}" raises "{exception}"')
#             raise FrictionlessException(error) from exception

#     return package
