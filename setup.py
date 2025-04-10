from setuptools import setup, find_packages

setup(
    name='sniptext',
    version='0.1.0',
    description='A terminal-based tool that summarizes website content in real-time using OpenAI GPT models.',
    author='Ariq',
    author_email='ariqf.lubis@gmail.com',
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "beautifulsoup4>=4.12.0",
        "requests>=2.28.0",
        "tqdm>=4.64.0"
    ],
    entry_points={
        'console_scripts': [
            'sniptext = sniptext.main:main',
        ],
    },
    python_requires='>=3.11',
)
