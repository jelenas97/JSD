from os import makedirs
from os.path import dirname, join
import glob
from pathlib import Path

import jinja2
from springr_generator.model import get_entity_mm
from datetime import datetime
from textx import generator


def generate_folders(root):
    output_root = root + "/src/main/"
    package = "jsd/tim/"
    folder_structure =  "java/" + package

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


    return folder_structure, output_root


def app_generation(model, output_path, project_name):
    this_folder = Path(__file__).parent.parent

    # Build model from file
    test_model = model


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

    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    jinja_env.filters['javatype'] = javatype

    folder_structure, output_root = generate_folders(project_name)

    print("Generating app... Output folder: " + output_root +
          " Folder structure: " + folder_structure)
    for template in glob.glob("springr_generator/templates/*.template"):
        # Load a template
        jinja_template = jinja_env.get_template(template.replace("\\", "/"))

        if "model" in template:
            for entity in test_model.entities:

                shared = [
                    x for x in test_model.shared.entities if x.name == entity.name]

                if shared:
                    with open(join(f"{output_root}{folder_structure}/model", f"{entity.name.capitalize()}.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity,
                                shared=test_model.shared, time=datetime.now()))
                else:
                    with open(join(f"{output_root}{folder_structure}/model", f"{entity.name.capitalize()}.java"), 'w') as f:
                        f.write(jinja_template.render(
                            entity=entity, time=datetime.now()))

        if "controller" in template:
            for entity in test_model.entities:
                shared = [
                    x for x in test_model.shared.entities if x.name == entity.name]

                if shared:
                    with open(join(f"{output_root}{folder_structure}/controller", f"{entity.name.capitalize()}Controller.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity,
                                shared=test_model.shared, time=datetime.now()))
                else:
                    with open(join(f"{output_root}{folder_structure}/controller", f"{entity.name.capitalize()}Controller.java"), 'w') as f:
                        f.write(jinja_template.render(
                            entity=entity, time=datetime.now()))

        if "repository" in template:
            for entity in test_model.entities:
                # For each entity generate file
                with open(join(f"{output_root}{folder_structure}/repository", f"{entity.name.capitalize()}Repository.java"), 'w') as f:
                    f.write(jinja_template.render(
                        entity=entity, time=datetime.now()))

        if "dto" in template:
            for entity in test_model.entities:
                shared = [
                    x for x in test_model.shared.entities if x.name == entity.name]

                if shared:
                    with open(join(f"{output_root}{folder_structure}/dto", f"{entity.name.capitalize()}DTO.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity,
                                shared=test_model.shared, time=datetime.now()))
                else:
                    with open(join(f"{output_root}{folder_structure}/dto", f"{entity.name.capitalize()}DTO.java"), 'w') as f:
                        f.write(jinja_template.render(
                            entity=entity, time=datetime.now()))

        if "service" in template:
            for entity in test_model.entities:
                shared = [
                    x for x in test_model.shared.entities if x.name == entity.name]

                if shared:
                    with open(join(f"{output_root}{folder_structure}/service", f"{entity.name.capitalize()}Service.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity,
                                shared=test_model.shared, time=datetime.now()))
                else:
                    with open(join(f"{output_root}{folder_structure}/service", f"{entity.name.capitalize()}Service.java"), 'w') as f:
                        f.write(jinja_template.render(
                            entity=entity, time=datetime.now()))

        if "implService" in template:
            for entity in test_model.entities:
                shared = [
                    x for x in test_model.shared.entities if x.name == entity.name]

                if shared:
                    with open(join(f"{output_root}{folder_structure}/service/impl", f"{entity.name.capitalize()}ServiceImpl.java"), 'w') as f:
                        f.write(jinja_template.render(entity=entity,
                                shared=test_model.shared, time=datetime.now()))
                else:
                    with open(join(f"{output_root}{folder_structure}/service/impl", f"{entity.name.capitalize()}ServiceImpl.java"), 'w') as f:
                        f.write(jinja_template.render(
                            entity=entity, time=datetime.now()))

        if "appProperties" in template:
            for entity in test_model.entities:
                with open(join(f"{output_root}/resources", f"application.properties"), 'w') as f:
                    f.write(jinja_template.render(entity=entity,
                            projectName=project_name, time=datetime.now()))

        if "pomFile" in template:
            for entity in test_model.entities:
                with open(join(f"{project_name}/", f"pom.xml"), 'w') as f:
                    f.write(jinja_template.render(entity=entity,
                            projectName=project_name, time=datetime.now()))

        if "mainClass" in template:
            for entity in test_model.entities:
                with open(join(f"{output_root}{folder_structure}", f"{project_name.capitalize()}.java"), 'w') as f:
                    f.write(jinja_template.render(
                        projectName=project_name, pack="jsd.tim"))

        if "homeController" in template:
            with open(join(f"{output_root}{folder_structure}/controller", f"HomeController.java"), 'w') as f:
                f.write(jinja_template.render(
                    projectName=project_name, pack="jsd.tim", time=datetime.now()))

        if "navbar" in template:
            entities = test_model.pages.entities
            pages = test_model.pages.pagesTypePart
            with open(join(f"{output_root}webapp/WEB-INF/jsp", f"navbar.jsp"), 'w') as f:
                f.write(jinja_template.render(entities=entities,
                        pages=pages, time=datetime.now()))

        if "homePage" in template:
            entities = test_model.pages.entities
            pages = test_model.pages.pagesTypePart
            with open(join(f"{output_root}webapp/WEB-INF/jsp", f"homePage.jsp"), 'w') as f:
                f.write(jinja_template.render(entities=entities,
                        pages=pages, time=datetime.now()))

        if "formJspPage" in template:
            for entity in test_model.entities:
                shared = [
                    x for x in test_model.shared.entities if x.name == entity.name]

                if shared:
                    with open(join(f"{output_root}webapp/WEB-INF/jsp",
                                   f"{entity.name}Form.jsp"), 'w') as f:
                        f.write(jinja_template.render(entity=entity,
                                shared=test_model.shared, time=datetime.now()))
                else:
                    with open(join(f"{output_root}webapp/WEB-INF/jsp",
                                   f"{entity.name}Form.jsp"), 'w') as f:
                        f.write(jinja_template.render(
                            entity=entity, time=datetime.now()))

        if "viewJspPage" in template:
            for entity in test_model.entities:
                shared = [
                    x for x in test_model.shared.entities if x.name == entity.name]

                pages = test_model.pages.pagesTypePart

                if shared:
                    with open(join(f"{output_root}webapp/WEB-INF/jsp",
                                   f"{entity.name}View.jsp"), 'w') as f:
                        f.write(jinja_template.render(
                            entity=entity, shared=test_model.shared, pages=pages, time=datetime.now()))
                else:
                    with open(join(f"{output_root}webapp/WEB-INF/jsp",
                                   f"{entity.name}View.jsp"), 'w') as f:
                        f.write(jinja_template.render(entity=entity,
                                pages=pages, time=datetime.now()))

        if "updateFormJspPage" in template:
            for entity in test_model.entities:
                shared = [
                    x for x in test_model.shared.entities if x.name == entity.name]

                pages = test_model.pages.pagesTypePart

                if shared:
                    with open(join(f"{output_root}webapp/WEB-INF/jsp",
                                   f"{entity.name}UpdateForm.jsp"), 'w') as f:
                        f.write(jinja_template.render(
                            entity=entity, shared=test_model.shared, pages=pages, time=datetime.now()))
                else:
                    with open(join(f"{output_root}webapp/WEB-INF/jsp",
                                   f"{entity.name}UpdateForm.jsp"), 'w') as f:
                        f.write(jinja_template.render(entity=entity,
                                pages=pages, time=datetime.now()))


@generator("springr_language", "App")
def app_generator(metamodel, model, output_path, overwrite, debug, **custom_args):
    '''Generate full-stack Spring Boot/JSP app'''
    try:
        if "/" in output_path:
            project_name = output_path.split("/")[0]
        else:
            project_name = output_path
        app_generation(model, output_path, project_name)
    except Exception as e:
        print("App generator failed due to: \n\n" + e.__str__())
