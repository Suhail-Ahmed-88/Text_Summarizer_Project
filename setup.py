import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

Repo_Name = "Text_Summarizer_Project"
Author_UserName = "Suhail-Ahmed-88"
Src_Repo = "textSummarizer"
Author_Email = "rajpar.suhail.ahmed@gmail.com"

setuptools.setup(
    name=Src_Repo,
    version=__version__,
    author=Author_UserName,
    author_email=Author_Email,
    description = "A small python package for NLP app",
    long_description=long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{Author_UserName}/{Repo_Name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{Author_UserName}/{Repo_Name}/issues",
    },
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where = "src")
)

