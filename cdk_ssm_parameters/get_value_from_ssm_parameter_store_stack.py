from aws_cdk import core as cdk
from aws_cdk import aws_ssm


class GetValueFromSsmParameterStoreStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        email = aws_ssm.StringParameter.from_string_parameter_name(
            scope=self,
            id='GetEmailFromSsmParameter',
            string_parameter_name='/my-site/alerts-email-dev'
        )

        environment = aws_ssm.StringListParameter.from_string_list_parameter_name(
            scope=self,
            id='GetEnvironmentFromSsmParameter',
            string_list_parameter_name='/my-site/environments',
        )

        cdk.CfnOutput(
            scope=self,
            id='parameter-email',
            value=email.string_value
        )


