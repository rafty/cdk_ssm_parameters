from aws_cdk import core as cdk
from aws_cdk import aws_ssm


class CdkSsmParametersStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        email_parameter = aws_ssm.StringParameter(
            scope=self,
            id='alert_email_parameter',
            parameter_name='/my-site/alerts-email-dev',
            string_value='hoge-dev@example.com',
            description='alert on dev to the email',
            type=aws_ssm.ParameterType.STRING,
            tier=aws_ssm.ParameterTier.STANDARD,
            allowed_pattern='.*'
        )

        environments_parameter = aws_ssm.StringListParameter(
            scope=self,
            id='environments_list_parameter',
            parameter_name='/my-site/environments',
            string_list_value=list(('dev', 'staging', 'prod')),
            tier=aws_ssm.ParameterTier.ADVANCED
        )
