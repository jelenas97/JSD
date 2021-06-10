from __future__ import unicode_literals
import os
from os.path import dirname, join
from textx import metamodel_from_file
from textx.export import metamodel_export, model_export
from metamodel import SimpleType, AnnotationName


this_folder = dirname(__file__)


def get_entity_mm(debug=False):
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
        'bool': SimpleType(None, 'bool'),
        'Column': AnnotationName(None, 'Column'),
        'ManyToMany': AnnotationName(None, 'ManyToMany')
    }
    entity_mm = metamodel_from_file(join(this_folder, 'entity.tx'),
                                    classes=[SimpleType, AnnotationName],
                                    builtins=type_builtins,
                                    debug=debug)

    return entity_mm


def main(debug=False):

    entity_mm = get_entity_mm(debug)

    # Export to .dot file for visualization
    dot_folder = join(this_folder, 'dotexport')
    if not os.path.exists(dot_folder):
        os.mkdir(dot_folder)

    metamodel_export(entity_mm, join(dot_folder, 'entity_meta.dot'))

    # Build Person model from person.ent file
    person_model = entity_mm.model_from_file(join(this_folder, 'test.ent'))

    # Export to .dot file for visualization
    model_export(person_model, join(dot_folder, 'test.dot'))


if __name__ == "__main__":
    main()
