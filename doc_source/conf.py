# -*- coding: utf-8 -*-

#
# General information about the project.
#

# Optional service/SDK name, typically the three letter acronym (TLA) that
# represents the service, such as 'SWF'. If this is an SDK, you can use 'SDK'
# here.
service_name = "service_name" # "SDK"

# The long version of the service or SDK name, such as "Amazon Simple Workflow
# Service", "AWS Flow Framework for Ruby", or "AWS SDK for Java".
service_name_long = u'AWS Cloud9'

# The landing page for the service documentation.
service_docs_home = u'https://aws.amazon.com/documentation/cloud9/'

# The project type, such as "Developer Guide", "API Reference", "User Guide",
# or whatever.
project = u'User Guide'

# A short description of the project.
project_desc = "AWS Cloud9 User Guide"

# The output will be generated in latest/<project_basename> and will appear on
# the web using the same basename.
project_basename = 'user-guide'

# This name is used as the manual / PDF name. Don't include the extension
# (.pdf) here.
man_name = 'aws-cloud9-ug'

# The language for this version of the docs. Typically 'en'. For a full list of
# values, see: http://sphinx-doc.org/config.html#confval-language
language = u'en'

# Whether or not to show the PDF link. If you generate a PDF for your
# documentation, set this to True.
show_pdf_link = True
rst2pdf_style = 'aws-pdf-beta-style'

# Don't show the language selector (yet).
show_lang_selector = True

# The link to the top of the doc source tree on GitHub. This allows generation
# of per-page "Edit on GitHub" links.
github_doc_url = 'https://github.com/awsdocs/aws-cloud9-user-guide/tree/master/doc_source'

# This allows the "Feedback" button to create a new issue on GitHub.
#doc_feedback_url = 'https://github.com/awsdocs/aws-java-developer-guide/issues/new'

#
# Version Information
#

# The version info for the project you're documenting, acts as replacement for
# |version| and |release| substitutions in the documentation, and is also used
# in various other places throughout the built documents.
#
# The short X.Y version.

version = '1.0'

# The full version, including alpha/beta/rc tags.

release = '1.0'

#
# Forum Information
#

# Optional forum ID. If there's a relevant forum at forums.aws.amazon.com, then
# set the ID here. If not set, then no forum ID link will be generated.
#

forum_id = '268'

# Whether to build a Kindle version of the content (and, if so, the Kindle ASIN). 
# Comment out the next line to not build a Kindle version.
build_mobi = 'B078XBZMWS' 

#
# Extra Navlinks
#

# Extra navlinks. You can specify additional links to appear in the top bar here
# as navlink name / url pairs. If extra_navlinks is not set, then no extra
# navlinks will be generated.
#
# extra_navlinks = [
#         ('API Reference', 'http://path/to/api/reference'),
#         ('GitHub', 'http://path/to/github/project'),
#         ]
extra_navlinks = [
        ]

build_html = True
build_pdf = True #Or False if you don't build a pdf
# build_mobi = True #Or the Kindle ASIN if you need a Kindle build

# Route customer feedback internally to AWS.
# Uncomment the following line to specify routing to a folder in classic SIM.
# feedback_folder_id = 'ea85bca2-658d-40f4-900f-65193653578a'

# Uncomment the following line to specify routing to a CTI in SIM Ticketing.
feedback_name = 'Cloud9'

# For the url docs.aws.amazon.com/docset-root/version/guide-name
docset_path_slug = 'cloud9'
version_path_slug = 'latest'
guide_path_slug = 'user-guide'

#
# EXTRA_CONF_CONTENT -- don't change, move or remove this line!
#
# Any settings *below* this act as overrides for the default config content.
# Declare extlinks <http://sphinx-doc.org/latest/ext/extlinks.html> and
# additional configuration details specific to this documentation set here.
#

# default code language for syntax highlighting
highlight_language = 'java'

if 'extlinks' not in vars():
    extlinks = {}

print(pdf_stylesheets)

extlinks['api-gateway-dev-guide'] = ('https://docs.aws.amazon.com/apigateway/latest/developerguide/%s', '')
extlinks['aws-gen-ref'] = ('https://docs.aws.amazon.com/general/latest/gr/%s', '')
extlinks['cfn-cli'] = ('https://docs.aws.amazon.com/cli/latest/reference/cloudformation/%s', '')
extlinks['cli-user-guide'] = ('https://docs.aws.amazon.com/cli/latest/userguide/%s', '')
extlinks['codecommit-user-guide'] = ('https://docs.aws.amazon.com/codecommit/latest/userguide/%s', '')
extlinks['codepipeline-user-guide'] = ('https://docs.aws.amazon.com/codepipeline/latest/userguide/%s', '')
extlinks['codestar-user-guide'] = ('https://docs.aws.amazon.com/codestar/latest/userguide/%s', '')
extlinks['console-getting-started'] = ('https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/%s', '')
extlinks['dynamodb-cli-ref'] = ('https://docs.aws.amazon.com/cli/latest/reference/dynamodb/%s', '')
extlinks['dynamodb-dev-guide'] = ('https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/%s', '')
extlinks['ec2-user-guide'] = ('https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/%s', '')
extlinks['iam-user-guide'] = ('https://docs.aws.amazon.com/IAM/latest/UserGuide/%s', '')
extlinks['lam-cli'] = ('https://docs.aws.amazon.com/cli/latest/reference/lambda/%s', '')
extlinks['lambda-dev-guide'] = ('https://docs.aws.amazon.com/lambda/latest/dg/%s', '')
extlinks['lightsail-docs'] = ('https://lightsail.aws.amazon.com/ls/docs/%s', '')
extlinks['s3-getting-started-guide'] = ('https://docs.aws.amazon.com/AmazonS3/latest/gsg/%s', '')
extlinks['sdk-for-go-api-ref'] = ('https://docs.aws.amazon.com/sdk-for-go/api/%s', '')
extlinks['sdk-for-go-dev-guide-v1'] = ('https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/%s', '')
extlinks['sdk-for-javascript-api-ref'] = ('https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/%s', '')
extlinks['sdk-for-javascript-dev-guide-v2'] = ('https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/%s', '')
extlinks['sdk-for-php-api-ref'] = ("https://docs.aws.amazon.com/aws-sdk-php/v3/api/%s", '')
extlinks['sdk-for-python-api-ref'] = ("https://boto3.readthedocs.io/en/latest/reference/%s", '')
extlinks['sdk-for-ruby-api-ref'] = ("https://docs.aws.amazon.com/sdk-for-ruby/v3/api/%s", '')
extlinks['sdk-for-ruby-dev-guide-v3'] = ("https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/%s", '')
extlinks['vpc-user-guide'] = ('https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/%s', '')