from os import makedirs
from os.path import dirname, join
import glob
import jinja2
from textx.registration import LanguageDesc
from entity_test import get_entity_mm
from datetime import datetime
import click
from textx import  generator

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
            'bool': 'boolean',
        }.get(s.name, s.name)

    projectName="medication"
    output_root = projectName+"/src/main/"
    package="jsd/tim/"
    folder_structure="java/"+package

    packages = [
        folder_structure+"model",
        folder_structure+"dto",
        folder_structure+"repository",
        folder_structure+"controller",
        folder_structure+"service",
        folder_structure+"service/impl",
        "resources",
        "webapp/WEB-INF/jsp"
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
                    with open(join(f"{output_root}{folder_structure}/model", f"{entity.name.capitalize()}.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, shared=test_model.shared, time=datetime.now()))
                else:
                    with open(join(f"{output_root}{folder_structure}/model", f"{entity.name.capitalize()}.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, time=datetime.now()))
                    

        if "controller" in template:
            for entity in test_model.entities:
                shared = [x for x in test_model.shared.entities if x.name == entity.name]

                if shared:
                    with open(join(f"{output_root}{folder_structure}/controller", f"{entity.name.capitalize()}Controller.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, shared=test_model.shared, time=datetime.now()))
                else:
                    with open(join(f"{output_root}{folder_structure}/controller", f"{entity.name.capitalize()}Controller.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, time=datetime.now()))

        if "repository" in template:
            for entity in test_model.entities:
                # For each entity generate file
                with open(join(f"{output_root}{folder_structure}/repository", f"{entity.name.capitalize()}Repository.java"), 'w') as f:
                    f.write(jinja_template.render(entity=entity, time=datetime.now()))

        if "dto" in template:
            for entity in test_model.entities:
                shared = [x for x in test_model.shared.entities if x.name == entity.name]

                if shared:
                    with open(join(f"{output_root}{folder_structure}/dto", f"{entity.name.capitalize()}DTO.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, shared=test_model.shared, time=datetime.now()))
                else:
                    with open(join(f"{output_root}{folder_structure}/dto", f"{entity.name.capitalize()}DTO.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, time=datetime.now()))

        if "service" in template:
            for entity in test_model.entities:
                shared = [x for x in test_model.shared.entities if x.name == entity.name]

                if shared:
                    with open(join(f"{output_root}{folder_structure}/service", f"{entity.name.capitalize()}Service.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, shared=test_model.shared, time=datetime.now()))
                else:
                    with open(join(f"{output_root}{folder_structure}/service", f"{entity.name.capitalize()}Service.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, time=datetime.now()))

        if "implService" in template:
            for entity in test_model.entities:
                shared = [x for x in test_model.shared.entities if x.name == entity.name]

                if shared:
                    with open(join(f"{output_root}{folder_structure}/service/impl", f"{entity.name.capitalize()}ServiceImpl.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, shared=test_model.shared, time=datetime.now()))
                else:
                    with open(join(f"{output_root}{folder_structure}/service/impl", f"{entity.name.capitalize()}ServiceImpl.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, time=datetime.now()))

        
        if "appProperties" in template:
            for entity in test_model.entities:
                with open(join(f"{output_root}/resources", f"application.properties"), 'w') as f:
                    f.write(jinja_template.render(entity=entity, projectName=projectName, time=datetime.now()))

        if "pomFile" in template:
            for entity in test_model.entities:
                with open(join(f"{projectName}/", f"pom.xml"), 'w') as f:
                    f.write(jinja_template.render(entity=entity,projectName=projectName, time=datetime.now()))

        if "mainClass" in template:
            for entity in test_model.entities:
                with open(join(f"{output_root}{folder_structure}", f"{projectName.capitalize()}.java"), 'w') as f:
                    f.write(jinja_template.render(projectName=projectName, pack="jsd.tim"))

        if "homeController" in template:
            for entity in test_model.entities:
                with open(join(f"{output_root}{folder_structure}/controller", f"HomeController.java"), 'w') as f:
                    f.write(jinja_template.render(projectName=projectName, pack="jsd.tim", time=datetime.now()))

        if "navbar" in template:
            entities = test_model.pages.entities
            pages = test_model.pages.pagesTypePart
            with open(join(f"{output_root}webapp/WEB-INF/jsp", f"navbar.jsp"), 'w') as f:
                f.write(jinja_template.render(entities=entities, pages=pages, time=datetime.now()))

        if "homePage" in template:
            entities = test_model.pages.entities
            pages = test_model.pages.pagesTypePart
            with open(join(f"{output_root}webapp/WEB-INF/jsp", f"homePage.jsp"), 'w') as f:
                f.write(jinja_template.render(entities=entities, pages=pages, time=datetime.now()))

        if "formJspPage" in template:
            for entity in test_model.entities:
                shared = [x for x in test_model.shared.entities if x.name == entity.name]

                if shared:
                    with open(join(f"{output_root}webapp/WEB-INF/jsp",
                                   f"{entity.name}Form.jsp"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, shared=test_model.shared, time=datetime.now()))
                else:
                    with open(join(f"{output_root}webapp/WEB-INF/jsp",
                                   f"{entity.name}Form.jsp"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, time=datetime.now()))

        if "viewJspPage" in template:
            for entity in test_model.entities:
                shared = [x for x in test_model.shared.entities if x.name == entity.name]

                pages = test_model.pages.pagesTypePart

                if shared:
                    with open(join(f"{output_root}webapp/WEB-INF/jsp",
                                   f"{entity.name}View.jsp"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, shared=test_model.shared, pages=pages, time=datetime.now()))
                else:
                    with open(join(f"{output_root}webapp/WEB-INF/jsp",
                                   f"{entity.name}View.jsp"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, pages=pages, time=datetime.now()))

        if "updateFormJspPage" in template:
            for entity in test_model.entities:
                shared = [x for x in test_model.shared.entities if x.name == entity.name]

                pages = test_model.pages.pagesTypePart

                if shared:
                    with open(join(f"{output_root}webapp/WEB-INF/jsp",
                                   f"{entity.name}UpdateForm.jsp"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, shared=test_model.shared, pages=pages, time=datetime.now()))
                else:
                    with open(join(f"{output_root}webapp/WEB-INF/jsp",
                                   f"{entity.name}UpdateForm.jsp"), 'w') as f:
                        f.write(jinja_template.render(entity=entity, pages=pages, time=datetime.now()))

@generator('springr_language', 'java')
def app_generator(metamodel, model, output_path, overwrite, debug, **custom_args):
    input_file = model._tx_filename

    base_dir = output_path if output_path else os.path.dirname(input_file)
    base_name, _ = os.path.splitext(os.path.basename(input_file))
    output_file = os.path.abspath(
        os.path.join(base_dir, "{}.{}".format(base_name, 'sql'))
    )

    if overwrite or not os.path.exists(output_file):
        click.echo('-> {}'.format(output_file))
        entities, database_name = main(input_file)

        if entities == None:
            return

        sql_template = init_template_engine(this_folder, 'sql_create.template')

        data = sql_template.render(
            entities=entities,
            database_name=database_name,
            time=get_current_time()
        )

        write_to_file(output_file, data)
        print('Successful compilation')
        print(f'SQL Script generated at: {output_file}')
    else:
        click.echo('-- Skipping: {}'.format(output_file))


@generator('springr_language', 'dot')
def dot_generator(metamodel, model, output_path, overwrite, debug, **custom_args):
    input_file = model._tx_filename

    base_dir = output_path if output_path else os.path.dirname(input_file)
    base_name, _ = os.path.splitext(os.path.basename(input_file))
    output_file = os.path.abspath(
        os.path.join(base_dir, "{}.{}".format(base_name, 'dot'))
    )

    if overwrite or not os.path.exists(output_file):
        click.echo('-> {}'.format(output_file))
        entities, database_name = main(input_file)

        if entities == None:
            return

        dot_template = init_template_engine(this_folder, 'dot_create.template')

        data = dot_template.render(
            entities=entities,
            database_name=database_name,
            time=get_current_time()
        )

        write_to_file(output_file, data)
        print('Successful compilation')
        print(f'ER diagram generated at: {output_file}')

        click.echo('   To convert to png run "dot -Tpng -O {}"'
                   .format(os.path.basename(output_file)))
    else:
        click.echo('-- Skipping: {}'.format(output_file))


jsd_lang = LanguageDesc('springr_language',
                        pattern='*.sr',
                        description='Spring Boot app language',
                        metamodel=get_mm)