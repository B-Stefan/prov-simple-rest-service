import connexion
from connexion.resolver import RestyResolver
from provdbconnector import ProvApi
from provdbconnector.db_adapters import SimpleInMemoryAdapter
import os
prov_api = ProvApi(adapter=SimpleInMemoryAdapter, auth_info=None)

port = os.environ.get("PORT", 9090)

if __name__ == '__main__':

    app = connexion.App(__name__, port, specification_dir='./')
    app.add_api('simple_rest_service.yaml', arguments={'title': 'Simple Prov-Document rest service'}, resolver=RestyResolver("api"))
    app.run()