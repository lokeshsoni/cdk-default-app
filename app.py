import aws_cdk as cdk

from config import *
from tags import TAGS
from stacks.stack import Stack

account = ""
region = ""

app = cdk.App()

for tag_name, tag_value in TAGS.items():
    cdk.Tags.of(app).add(tag_name, tag_value)

Stack(
    app,
    STACK_NAME,
    description=STACK_DESCRIPTION,
    env=cdk.Environment(
        account=account, 
        region=region
    ),
)

app.synth()
