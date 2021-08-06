from os import makedirs
from os.path import dirname, join, sep
import glob
import jinja2
from entity_test import get_entity_mm


def main(debug=False):
    this_folder = dirname(__file__)

    entity_mm = get_entity_mm(debug)

    # Build model from file
    test_model = entity_mm.model_from_file(join(this_folder, 'test.ent'))

    def javatype(s):
        """
        Maps type names from PrimitiveType to Java.
        """
        return {
            'long': 'long',
            'integer': 'int',
            'string': 'String',
            'bool': 'boolean'
        }.get(s.name, s.name)

    output_root = "srcgen"

    packages = [
        "model",
        "dto",
        "repository",
        "controller",
        "service",
        "service/impl"
    ]

    # Create output folder structure
    [makedirs(f"{output_root}/{package}", exist_ok=True)
     for package in packages]

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Register filter for mapping Entity type names to Java type names.
    # Can be used for annotation types?
    jinja_env.filters['javatype'] = javatype

    for template in glob.glob("templates/*.template"):
        # Load a template
        jinja_template = jinja_env.get_template(template.replace("\\", "/"))

        if "model" in template:
            for entity in test_model.entities:
                shared = [x for x in test_model.shared.entities if x.name == entity.name]

                if shared:
                    with open(join(f"{output_root}/model", f"{entity.name.capitalize()}.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, shared=test_model.shared))
                else:
                    with open(join(f"{output_root}/model", f"{entity.name.capitalize()}.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity))
                    

        if "controller" in template:
            for entity in test_model.entities:
                shared = [x for x in test_model.shared.entities if x.name == entity.name]
                
                if shared:
                    with open(join(f"{output_root}/controller", f"{entity.name.capitalize()}Controller.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, shared=test_model.shared))
                else:
                    with open(join(f"{output_root}/controller", f"{entity.name.capitalize()}Controller.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity))

        if "repository" in template:
            for entity in test_model.entities:
                # For each entity generate file
                with open(join(f"{output_root}/repository", f"{entity.name.capitalize()}Repository.java"), 'w') as f:
                    f.write(jinja_template.render(entity=entity))

        if "dto" in template:
            for entity in test_model.entities:
                shared = [x for x in test_model.shared.entities if x.name == entity.name]

                if shared:
                    with open(join(f"{output_root}/dto", f"{entity.name.capitalize()}DTO.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, shared=test_model.shared))
                else:
                    with open(join(f"{output_root}/dto", f"{entity.name.capitalize()}DTO.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity))

        if "service" in template:
            for entity in test_model.entities:
                shared = [x for x in test_model.shared.entities if x.name == entity.name]

                if shared:
                    with open(join(f"{output_root}/service", f"{entity.name.capitalize()}Service.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, shared=test_model.shared))
                else:
                    with open(join(f"{output_root}/service", f"{entity.name.capitalize()}Service.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity))

        if "serviceImpl" in template:
            for entity in test_model.entities:
                shared = [x for x in test_model.shared.entities if x.name == entity.name]

                if shared:
                    with open(join(f"{output_root}/service/impl", f"{entity.name.capitalize()}ServiceImpl.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, shared=test_model.shared))
                else:
                    with open(join(f"{output_root}/service/impl", f"{entity.name.capitalize()}ServiceImpl.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity))


if __name__ == "__main__":
    main()
