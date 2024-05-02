from constants import MODELS


class PromptDataValidator:
    """Validates prompt data integrity and consistency."""

    @staticmethod
    def verify_model(model: str) -> bool:
        """
        Verifies if the provided model is valid.

        Args:
            model (str): The model string to be validated.

        Returns:
            bool: True if the model is valid, False otherwise.
        """
        try:
            if not isinstance(model, str):
                raise TypeError("Model must be a string")
            if model not in MODELS:
                raise ValueError(
                    f"Model '{model}' is not valid. Allowed models: {MODELS}"
                )
        except (TypeError, ValueError):
            return False
        return True
