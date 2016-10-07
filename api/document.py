from logging import Logger

from connexion import NoContent, problem
from  provdbconnector.provapi import ProvApiException

from simple_rest_service import prov_api

pets = {}

logger = Logger(__name__)

def problem_exception(e):
    """
    Returns a problem description for the http response
    :param e:
    :type Exception
    :return: problem instance for http response
    """
    return problem(500,"Prov-Connector Error",str(e),str(type(e)))


def post(document):
    """
    Convert a string to prov and save this prov document
    :param document:
    :type: str
    :return:id
    :type str
    """
    try:
        id = prov_api.create_document(document)
    except ProvApiException as e:
        logger.debug(e)
        return problem_exception(e)
    except NotImplementedError as e:
        logger.debug(e)
        return problem_exception(e)

    return id, 201

def get(id):
    """
    Get method for prov documents
    :param id:
    :type str
    :return: Return a str in prov-n
    :type str
    """
    try:
        provn = prov_api.get_document_as_provn(id)
    except ProvApiException as e:
        logger.debug(e)
        return problem_exception(e)
    except NotImplementedError as e:
        logger.debug(e)
        return problem_exception(e)

    return provn, 200


###UNSUPPORTED METHODS###
def put(id, document):
    """
    Updated a prov document
    :param id:
    :param document:
    :return:
    """

    return NoContent,501


def delete(id):
    """
    Delete command for prov documents

    :param id:
    :return:
    """
    return NoContent, 501

def search():
    # NOTE: we need to wrap it with list for Python 3 as dict_values is not JSON serializable
    return list(pets.values())