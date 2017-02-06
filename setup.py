from setuptools import setup
 
setup(
    name = 'monkeys',
    packages = ['monkeys'],
    version = '0.0.4',
    description = 'A genetic programming framework',
    license='MIT',
    author='H. Chase Stevens',
    author_email='chase@chasestevens.com',
    url='https://github.com/hchasestevens/monkeys',
    install_requires=['astor', 'graphviz', 'numpy'],
    keywords='genetic programming optimization',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
    ]
)