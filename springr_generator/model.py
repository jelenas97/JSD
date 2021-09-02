from __future__ import unicode_literals
import os
from os.path import dirname, join
from textx import metamodel_from_file, language, generator
from textx.export import metamodel_export, model_export
from springr_generator.metamodel import SimpleType, AnnotationName


def get_entity_mm():
    metamodel_path = dirname(__file__)
    """
    Builds and returns a meta-model for Entity language.
    """
    # Built-in simple types
    # Each model will have this simple types during reference resolving but
    # these will not be a part of `types` list of EntityModel.
    type_builtins = {
        'long': SimpleType(None, 'long'),
        'integer': SimpleType(None, 'integer'),
        'string': SimpleType(None, 'string'),
        'date': SimpleType(None, 'date'),
        'bool': SimpleType(None, 'boolean'),
        'Column': AnnotationName(None, 'Column'),
        'ManyToMany': AnnotationName(None, 'ManyToMany'),
        'Id': AnnotationName(None, 'Id')
    }

    entity_mm = metamodel_from_file(metamodel_path,
                                    classes=[SimpleType, AnnotationName],
                                    builtins=type_builtins)

    return entity_mm


def dot_model_export(model_path, output_path):
    entity_mm = get_entity_mm()

    # Export to .dot file for visualization
    dot_folder = join(output_path)
    if not os.path.exists(dot_folder):
        os.mkdir(dot_folder)

    print("Exporting metamodel and model to folder: " + dot_folder)

    metamodel_export(entity_mm, join(dot_folder, 'metamodel.dot'))

    # Build Person model from person.ent file
    person_model = entity_mm.model_from_file(model_path)

    # Export to .dot file for visualization
    model_export(person_model, join(dot_folder, 'model.dot'))

    print("Done exporting Dot")


@language("springr_language", "*.ent")
def springr_language():
    '''A language for entity description'''
    return get_entity_mm()

@generator("springr_language", "Dot")
def dot_generator(metamodel, model, output_path, overwrite, debug, **custom_args):
    '''Generating dot visualizations from SpringR grammars'''
    try:
        dot_model_export(model, output_path)
    except Exception as e:
        print("Dot generator failed due to: \n\n" + e)