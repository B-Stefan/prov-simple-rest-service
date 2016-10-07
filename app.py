import connexion
from connexion.resolver import RestyResolver
import os
port = int(os.environ.get("PORT", 9090))

app = connexion.App(__name__, port, specification_dir='./')

app.add_api('./app.yaml', arguments={'title': 'Simple Prov-Document rest service'}, resolver=RestyResolver("api"))

if __name__ == '__main__':
    app.run(debug=True)