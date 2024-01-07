import unittest
from pytfvars import tfvars
import hcl


class DictWithList(unittest.TestCase):

    def setUp(self):
        self.values = {}
        l1 = ["v1", "v2", "v3"]
        self.values["l1"] = l1

    def testConvert(self):
        result = tfvars.convert(self.values)
        hcl.loads(result)


class DictWithBlocks(unittest.TestCase):
    def setUp(self):
        self.values = {}
        d1 = {}
        d2 = {"d2_k1": "d2_v1", "d2_k2": "d2_v2", "d2_k3": "d2_v3"}
        d3 = {"d3_k1": "d3_v1", "d3_k2": "d3_v2", "d3_k3": "d3_v3"}
        d1["d2"] = d2
        d1["d3"] = d3
        self.values["d1"] = d1

    def testConvert(self):
        result = tfvars.convert(self.values)
        hcl.loads(result)


class DictWithListOfBlocks(unittest.TestCase):
    def setUp(self):
        self.values = {}
        d1 = {"d1_k1": "d1_v1", "d1_k2": "d1_v2", "d1_k3": "d1_v3"}
        d2 = {"d2_k1": "d2_v1", "d2_k2": "d2_v2", "d2_k3": "d2_v3"}
        d3 = {"d3_k1": "d3_v1", "d3_k2": "d3_v2", "d3_k3": "d3_v3"}
        l1 = [d1, d2, d3]
        self.values["l1"] = l1

    def testConvert(self):
        result = tfvars.convert(self.values)
        hcl.loads(result)


class PropertyWithMultilineStringValue(unittest.TestCase):
    def setUp(self):
        self.values = {}
        d1 = {"d1_k1": "d1_v1", "d1_k2": "d1_v2", "d1_k3": "d1_v3"}
        d2 = {"d2_k1": "d2_v1", "d2_k2": "d2_v2", "d2_k3": "d2_v3"}
        d3 = {"d3_k1": "d3_v1", "d3_k2": "d3_v2", "d3_k3": "d3_v3"}
        l1 = [d1, d2, d3]
        s1 = """
        This
        is
        multiline
        string
        """
        self.values["l1"] = l1
        self.values["s1"] = s1

    def testConvert(self):
        result = tfvars.convert(self.values)
        hcl.loads(result)


class MultiplePropertiesWithMapAndPropertyAndListOfBlocks(unittest.TestCase):
    def setUp(self):
        self.values = {}
        stage_variables = {}
        log_group_arn = "arn:aws:logs:ap-northeast-2:AWS_ACCOUNT:log-group:LOG_GROUP_NAME"
        self.values["stage"] = {
            "stage_variables": stage_variables,
            "log_group_arn": log_group_arn
        }

        alb_integration_values = {}
        aiv1 = {}
        aiv1_name = "test1_proxy"
        aiv1_description = "test1 proxy every request starts with /test1"
        aiv1_route1 = {
            "route_key": "ANY /test1/{proxy+}",
            "authorization_type": "CUSTOM",
            "authorizer": "jwt-authorizer",
            "create_alarm": True,
            "is_admin_or_depends_on_idc": False
        }

        aiv1_route2 = {
            "route_key": "OPTION /test1/{proxy+}",
            "authorization_type": "CUSTOM",
            "authorizer": "NONE",
            "create_alarm": False,
            "is_admin_or_depends_on_idc": False
        }

        aiv1_routes = [aiv1_route1, aiv1_route2]
        aiv1_integration_uri = "arn:aws:elasticloadbalancing:ap-northeast-2:AWS_ACCOUNT:listener/TARGET_GROUP_LISTENER"
        aiv1_integration_method = "ANY"
        aiv1_tls_config = "YOUR_DOMAIN"
        aiv1_request_parameters = {
            "overwrite:header.user-id" : "$context.authorizer.userId",
            "overwrite:path" : "/$request.path.proxy"
        }
        aiv1_response_parameters = []
        aiv1["name"] = aiv1_name
        aiv1["description"] = aiv1_description
        aiv1["routes"] = aiv1_routes
        aiv1["integration_uri"] = aiv1_integration_uri
        aiv1["integration_method"] = aiv1_integration_method
        aiv1["tls_config"] = aiv1_tls_config
        aiv1["request_parameters"] = aiv1_request_parameters
        aiv1["response_parameters"] = aiv1_response_parameters
        alb_integration_values[aiv1_name] = aiv1

        self.values["alb_integration_values"] = alb_integration_values

        http_integration_values = {}
        self.values["http_integration_values"] = http_integration_values

    def testConvert(self):
        result = tfvars.convert(self.values)
        hcl.loads(result)


if __name__ == '__main__':
    unittest.main()
