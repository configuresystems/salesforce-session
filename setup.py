from setuptools import setup

def readme():
    with open('README.md','w') as f:
        return f.read()


setup(name='SalesForceSession',
      version='0.1',
      description='A wrapper for simple-salesforce that creates a session and build valid SQL queries by passing query params rather than the raw sql.',
      classifiers=[
          'Environment :: SalesForce Integration',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      keywords=['salesforce', 'simple-salesforce', 'sql generator', 'salesforce sessions'],
      url='https://github.com/configuresystems/salesforce-session',
      author='John Martin',
      author_email='john.martin@configure.systems',
      license='MIT',
      py_modules=['salesforce_session'],
      install_requires=[
          'simple-salesforce',
          ],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose']
      )
