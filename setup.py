from setuptools import setup, find_packages

__version__ = '0.0.0.0'

REPO_NAME = "personality_prediction"
AUTHOR_USER_NAME = "HimmatMagar"
SRC_REPO = "personalityPrediction"
AUTHOR_EMAIL = "himmatmagar007@gmail.com"


setup(
      name="personalityPrediction",
      version=__version__,
      author=AUTHOR_USER_NAME,
      author_email=AUTHOR_EMAIL,
      description="End to End ML implementation to perdict the personality of a person",
      long_description_content_type='text/markdown',
      url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
      project_urls={
            "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue"
      },
      package_dir={"": "src"},
      packages=find_packages(where='src')
)