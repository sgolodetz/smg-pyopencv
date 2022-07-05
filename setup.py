import skbuild

with open("README.md", "r") as fh:
    long_description = fh.read()

skbuild.setup(
    name="smg-pyopencv",
    version="0.0.1",
    author="Stuart Golodetz",
    author_email="stuart.golodetz@cs.ox.ac.uk",
    description="Python bindings for OpenCV images",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sgolodetz/smg-pyopencv",
    packages=["smg.pyopencv", "smg.pyopencv.cpp"],
    cmake_install_dir="smg/pyopencv/cpp",
    include_package_data=True,
    install_requires=[
        "numpy"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='==3.7.*',
)
