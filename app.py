#!/usr/bin/env python3
import os
from aws_cdk import core as cdk
from cdk_ssm_parameters.cdk_ssm_parameters_stack import CdkSsmParametersStack
from cdk_ssm_parameters.get_value_from_ssm_parameter_store_stack import GetValueFromSsmParameterStoreStack

env = cdk.Environment(
    account=os.environ.get("CDK_DEPLOY_ACCOUNT", os.environ["CDK_DEFAULT_ACCOUNT"]),
    region=os.environ.get("CDK_DEPLOY_REGION", os.environ["CDK_DEFAULT_REGION"]),
)

app = cdk.App()

CdkSsmParametersStack(
    scope=app,
    construct_id="CdkSsmParametersStack",
    env=env
)

GetValueFromSsmParameterStoreStack(
    scope=app,
    construct_id="GetValueFromSsmParameterStoreStack",
    env=env
)

app.synth()
