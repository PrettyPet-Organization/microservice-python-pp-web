import inspect
import logging.config
from functools import wraps


from django.conf import settings
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from rest_framework.views import APIView


class CheckSystem(APIView):
    """
    Class for checking system settings and their status.

    Inherits from `APIView` and provides methods for performing checks, such as logging configuration.
    Uses a decorator to execute checks and handle error and success messages.
    """

    def __init__(self, **kwargs):
        """
        Initializes the CheckSystem class.

        Sets default values for error and success messages and initializes an empty dictionary for storing
        data.
        """

        super().__init__(**kwargs)
        self.DEFAULT_ERROR_MESSAGE = _("Check {item} failed.")
        self.DEFAULT_SUCCESS_MESSAGE = _("Successfully configured!")
        self.data = {}

    @staticmethod
    def _check_method(data_item_name: str, error_message=None, success_message=None):
        """
        Decorator for checking methods.

        Uses the provided check method to perform a check, marks the wrapper method with a custom attribute. If the
        check fails, raises an exception with the specified error message or a default message. Updates the `self.data`
        dictionary with the success message if the check passes.

        :param data_item_name: Name of the data item to store in `self.data`.
        :type data_item_name: str
        :param error_message: Error message to raise if the check fails. Defaults to None.
        :type error_message: str
        :param success_message: Success message to store in `self.data`. Defaults to None.
        :type success_message: str

        :return: Decorated method that performs the check and updates `self.data`.
        :rtype: function

        :raises Exception: If the check method fails.
        """

        def decorator(check_method):
            @wraps(check_method)
            def wrapper(self):
                if not check_method(self):
                    # If the error message is not specified, uses the default
                    raise Exception(
                        error_message
                        if error_message
                        else self.DEFAULT_ERROR_MESSAGE.format(
                            item=check_method.__name__
                        )
                    )

                # If the success message is not specified, uses the default
                self.data[data_item_name] = (
                    success_message if success_message else self.DEFAULT_SUCCESS_MESSAGE
                )

            # Marks the wrapper method with a custom attribute
            wrapper.__is_check_method__ = True
            return wrapper

        return decorator

    @_check_method(
        data_item_name="logs",
        error_message=_("Logging is not configured in the project."),
        success_message=_("Logging is working!"),
    )
    def check_logs(self) -> bool:
        """
        Checks the logging configuration.

        Processes examples of logs of different levels. Initializes the logger based on the settings.LOGGING
        configuration and processes logs of various levels: DEBUG, INFO, WARNING, ERROR, and CRITICAL. Handles
        exceptions that may occur during the setup.

        :return: True if logging is configured correctly, False otherwise.
        :rtype: bool

        :raises ImportError: If the logging.config module could not be imported.
        :raises KeyError: If a required key is missing from the logging configuration.
        :raises Exception: To handle any other exceptions that may occur during setting up or using logging.
        """

        logging_conf = settings.LOGGING
        logging.config.dictConfig(logging_conf)
        logger = logging.getLogger(__name__)

        try:
            logger.debug("example DEBUG message")
            logger.info("example INFO message")
            logger.warning("example WARNING message")
            logger.error("example ERROR message")
            logger.critical("example CRITICAL message")
            return True

        except ImportError as e:
            print(_(f"Module import exception: {e}"))
        except KeyError as e:
            print(_(f"Logging configuration error: missing key {e}"))
        except Exception as e:
            print(_(f"An error occurred while setting up logging: {e}"))

    def get(self, request) -> JsonResponse:
        """
        Performs all checks and returns their results as a JSON response.

        :param request: The HTTP request object.
        :type request: HttpRequest

        :return: JsonResponse with the results of all checks.
        :rtype: JsonResponse
        """

        # Finds all methods that are checks (decorated with _check_method)
        checks = [
            method
            for name, method in inspect.getmembers(self, predicate=inspect.ismethod)
            if getattr(
                method, "__is_check_method__", False
            )  # Checks for the custom attribute
        ]
        for check in checks:
            check()

        return JsonResponse(self.data)
