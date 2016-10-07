import connexion
from connexion.resolver import RestyResolver
from provdbconnector import ProvApi
from provdbconnector.db_adapters import SimpleInMemoryAdapter
import os
prov_api = ProvApi(adapter=SimpleInMemoryAdapter, auth_info=None)

port = int(os.environ.get("PORT", 9090))

app = connexion.App(__name__, port, specification_dir='./',host='0.0.0.0')

app.add_api('example.yaml', arguments={'title': 'Simple Prov-Document rest service'}, resolver=RestyResolver("api"))

app.run()