import json
from typing import Any, Dict, Optional

class DataParser:
    @staticmethod
    def parse_json(data: str) -> Optional[Dict[str, Any]]:
        try:
            return json.loads(data)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            return None

    @staticmethod
    def parse_iot_data(data: str) -> Optional[Dict[str, Any]]:
        # This is a simple example. In a real-world scenario, 
        # you'd need to implement specific parsing logic for your IoT devices.
        try:
            # Assume IoT data is in format: "key1:value1;key2:value2"
            pairs = data.split(';')
            return {k: v for k, v in (pair.split(':') for pair in pairs)}
        except Exception as e:
            print(f"Error parsing IoT data: {e}")
            return None

    @staticmethod
    def validate_data(data: Dict[str, Any], schema: Dict[str, type]) -> bool:
        try:
            for key, expected_type in schema.items():
                if key not in data:
                    print(f"Missing key: {key}")
                    return False
                if not isinstance(data[key], expected_type):
                    print(f"Invalid type for {key}. Expected {expected_type}, got {type(data[key])}")
                    return False
            return True
        except Exception as e:
            print(f"Error validating data: {e}")
            return False
