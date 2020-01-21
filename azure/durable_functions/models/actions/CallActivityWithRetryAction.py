from typing import Any, Dict

from .ActionType import ActionType
from ..RetryOptions import RetryOptions
from ..utils.json_utils import add_attrib, add_json_attrib


class CallActivityWithRetryAction:
    def __init__(self, function_name: str,
                 retry_options: RetryOptions, input_=None):
        self.action_type: ActionType = ActionType.CALL_ACTIVITY_WITH_RETRY
        self.function_name: str = function_name
        self.retry_options: RetryOptions = retry_options
        self.input_ = input_

        if not self.function_name:
            raise ValueError("function_name cannot be empty")

    def to_json(self) -> Dict[str, Any]:
        json_dict = {}

        add_attrib(json_dict, self, 'action_type', 'actionType')
        add_attrib(json_dict, self, 'function_name', 'functionName')
        add_attrib(json_dict, self, 'input', 'input')
        add_json_attrib(json_dict, self, 'retry_options', 'retryOptions')
        return json_dict
