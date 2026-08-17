import unittest

from umai.serving import InferenceRequest, LocalEndpoint


class ServingTests(unittest.TestCase):
    def test_successful_request(self) -> None:
        endpoint = LocalEndpoint(lambda payload: {"value": int(payload["value"]) * 2})
        request = InferenceRequest("req-1", "model-1", {"value": 3})
        response = endpoint.handle(request)
        self.assertTrue(response.ok)
        self.assertEqual(response.output["value"], 6)
        self.assertEqual(response.model_version, "model-1")

    def test_invalid_request_is_bounded_error(self) -> None:
        endpoint = LocalEndpoint(lambda payload: {"value": payload["missing"]})
        response = endpoint.handle(InferenceRequest("req-2", "model-1", {}))
        self.assertFalse(response.ok)
        self.assertEqual(response.error_code, "INVALID_REQUEST")

    def test_empty_request_id_rejected(self) -> None:
        with self.assertRaises(ValueError):
            InferenceRequest("", "model-1", {})


if __name__ == "__main__":
    unittest.main()
