from distutils.core import setup

setup(
    name='cv_utils',
    packages=['cv_utils'],
    version='0.1',
    description='Computer Vision or OpenCV python utility functions. '
                'It also includes basic utilities for image processing and '
                'computer vision related tasks.',
    long_description=open('README.md').read(),
    author='Michael Jaison Gnanasekar, Shreyas Joshi',
    author_email='gmichaeljaison@gmail.com, shreyasvj25@gmail.com',
    url='https://github.com/gmichaeljaison/cv-utils',
    download_url='https://github.com/gmichaeljaison/cv-utils/tarball/0.1',
    keywords=['computer vision', 'image processing', 'utility', 'template matching'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities"
    ],
    requires=['numpy', 'cv2', 'matplotlib', 'scipy', 'skimage', 'theano'],
    license='LICENSE'
)