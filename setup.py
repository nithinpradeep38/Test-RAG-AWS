from setuptools import setup, find_packages

setup(
    name="qasystem",
    version="0.0.1",
    author="Nithin",   
    author_email="nithinpradeep38@gmail.com",
    packages=find_packages(),
    install_requires=["langchain","langchainhub","bs4","tiktoken","openai","boto3","langchain_community","chromadb","awscli",
"streamlit",
"pypdf",
"faiss-cpu"]
)
