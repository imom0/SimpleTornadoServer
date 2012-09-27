from setuptools import setup

install_requires = [
    'tornado>=2.0',
]

setup(
    name='SimpleTornadoServer',
    version='0.1',
    description='better SimpleHTTPServer using tornado',
    author='iMom0',
    author_email='mobeiheart@gmail.com',
    url='https://github.com/imom0/SimpleTornadoServer',
    license='BSD',
    py_modules=['SimpleTornadoServer'],
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Utilities',
    ]
)
