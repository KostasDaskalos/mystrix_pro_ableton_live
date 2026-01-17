import Live
from .Mystrix_Pro import Mystrix_Pro


def create_instance(c_instance):
    """ Creates and returns the APC20 script """
    return Mystrix_Pro(c_instance)

# local variables:
# tab-width: 4
