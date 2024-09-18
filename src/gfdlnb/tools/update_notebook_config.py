import os
import yaml


def update_notebook_config(config=None):
    """
    MAR will pass for environment variables to the script when running via the web engine:

        * `MAR_STARTYR`: Beginning year of analysis from model
        * `MAR_ENDYR`: Ending year of analysis from model
        * `MAR_DORA_ID`: The experiment ID in the database
        * `MAR_PATHPP`: The top-level path to the post-processing experiment directory of the experiment

    The block below will use values passed in by Dora but default to the values defined above in `config`. This is useful for interactive usage and debugging.

    If executed from Dora, there will also be a `DORA_EXECUTE` variable that is set.
    """
    if config is None:
        config = {
            "startyr": None,
            "endyr": None,
            "dora_id": None,
        }

    if os.path.exists("mar_config.yaml"):
        with open("mar_config.yaml", "r") as file:
            mar_config = yaml.safe_load(file)
        if "experiment" in mar_config:
            config["dora_id"] = mar_config["experiment"]
        if "start_year" in mar_config:
            config["startyr"] = mar_config["start_year"]
        if "end_year" in mar_config:
            config["endyr"] = mar_config["end_year"]

    for k, v in config.items():
        config[k] = (
            os.environ[f"MAR_{k.upper()}"]
            if f"MAR_{k.upper()}" in os.environ.keys()
            else v
        )

    return config
