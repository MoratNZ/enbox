import pynetbox


def init(config):
    """Provide an initialised API endpoint

    Arguments:
        config {configParser} -- The enbox config object

    Returns:
        pynetbox.api.Api -- an iniitalised pynetbox API instance
    """
    return pynetbox.api(
        config['NetBox']['Url'],
        token=config['NetBox']['Token']
    )
