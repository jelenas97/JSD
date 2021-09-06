from setuptools import find_packages, setup

setup(
    name="springR",
    author="Tim 5",
    license="MIT",
    description="Spring Boot CRUD app generator",
    keywords="DSL, Java Spring Boot, Entity",
    url="https://github.com/jelenas97/JSD",
    long_description="file: README.md",
    long_description_content_type="text/markdown",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["*.tx", "springr_generator/**/*.template", "springr_generator/**/*.py"]},
    install_requires=["Arpeggio", "textX[cli]", "Jinja2", "future", "textX"],
    entry_points={
        "textx_languages": [
            "springr_language = springr_generator.model:springr_language",
        ],
        "textx_generators": [
            "springr_app = springr_generator.generator:app_generator",
            "springr_dot = springr_generator.model:dot_generator"
        ]
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers"
    ],
)
