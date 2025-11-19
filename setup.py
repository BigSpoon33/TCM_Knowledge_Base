from setuptools import setup, find_packages

setup(
    name="capsule-learn",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
        "rich>=13.0.0",
        "pyyaml>=6.0",
        "google-generativeai>=0.3.0",
        "questionary>=2.0.0",
    ],
    entry_points={
        "console_scripts": [
            "capsule=capsule.cli:main",
            "cap=capsule.cli:main",
        ],
    },
    author="TCM Knowledge Base",
    description="AI-powered learning assistant for TCM studies",
    long_description="A unified CLI for generating flashcards, quizzes, slides, and guided conversations for Traditional Chinese Medicine patterns.",
    python_requires=">=3.8",
)
